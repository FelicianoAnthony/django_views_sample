from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Employee, EmployeeJob
from .serializers import EmployeeSerializer, EmployeeJobSerializer
from rest_framework import viewsets, status
import pdb
from rest_framework.response import Response


class EmployeeListNoModelView(viewsets.ViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	#pdb.set_trace()

	def list(self, request): 
		queryset = Employee.objects.all()
		serializer = EmployeeSerializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request): 
		serializer = EmployeeSerializer(data=self.request.data, many=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeDetailNoModelView(viewsets.ViewSet):

		queryset = Employee.objects.all()
		serializer_class = EmployeeSerializer

		#def retrieve(self, request, pk=None):
		def retrieve(self, request, *args, **kwargs):
			"""
			send GET to employees/5/
			"""
			
			pk = self.kwargs['pk']
			queryset = Employee.objects.filter(id=pk)
			serializer = EmployeeSerializer(queryset, many=True)
			return Response(serializer.data)


		def update(self, request, *args, **kwargs):
		"""
		send POST to employees/5/
		
		"""
			

			# find by pk 
			pk = self.kwargs['pk']
			self.queryset = Employee.objects.filter(id=pk)
			#pdb.set_trace()

			if self.queryset:
				data = self.request.data.copy()
				self.queryset[0].first_name = data.pop('first_name', None)
				self.queryset[0].last_name = data.pop('last_name', None)
				self.queryset[0].hire_date = data.pop('hire_date', None)
				self.queryset[0].current_employee = data.pop('current_employee', True)

				# but if this were updated this would be done differently
				# cant just use pk of department -- need to get employeejob INSTANCE 
				job_instance = EmployeeJob.objects.filter(id=data.pop('department'))
				self.queryset[0].department = job_instance[0]
				self.queryset[0].save()

				# ser
				serializer = EmployeeSerializer(self.queryset, many=True)
				return Response(serializer.data)

		def destroy(self, request, *args, **kwargs):
			#pdb.set_trace()

			pk = self.kwargs['pk']
			qs_remove = Employee.objects.filter(id=pk)
			if qs_remove:
				qs_remove.delete()
				return Response(status=status.HTTP_204_NO_CONTENT)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








   



	# def list(self, request, *args, **kwargs):
	#     queryset = self.filter_queryset(self.get_queryset())

	#     page = self.paginate_queryset(queryset)
	#     if page is not None:
	#         serializer = self.get_serializer(page, many=True)
	#         return self.get_paginated_response(serializer.data)

	#     serializer = self.get_serializer(queryset, many=True)
	#     return Response(serializer.data)







#class EmployeeListMixin (mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin):
# this will not work but below will -- why?
# class EmployeeListMixin(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

	# def get(self, request, *args, **kwargs):
	#     #pdb.set_trace()
	#     return self.list(request, *args, **kwargs)

	# def post(self,request,*args, **kwargs):
	#     #pdb.set_trace()
	#     return self.create(request, *args, **kwargs)


class EmployeeJobListMixin(generics.RetrieveUpdateDestroyAPIView):
#class EmployeeJobListMixin(generics.RetrieveAPIView):
	queryset = EmployeeJob.objects.all()
	serializer_class = EmployeeJobSerializer

	# retrieve update

	# def retrieve(request, *args, **kwargs):
	# 	pdb.set_trace()