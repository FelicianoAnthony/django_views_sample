from rest_framework import viewsets, mixins
from .serializers import ComputerSerializer
from .models import Computer
from rest_framework import viewsets
from rest_framework import generics
import pdb
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED


#from rest_framework.permissions import AllowAny


# class TestGenericsView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ComputerSerializer
#     queryset = Computer.objects.all()


#     def get_object(self):
#         import pdb; pdb.set_trace()




##############################################################################################################


class ComputerList(generics.ListCreateAPIView):


    serializer_class = ComputerSerializer
    queryset = Computer.objects.all()

    # def get(self, request, *args, **kwargs):
    #     """
    #     GET to computers/
    #     """
    # def create(self, request, *args, **kwargs):
    #     """
    #     POST to computers/ 
    #     data stored in self.request.data
    #     """

    



class ComputerDetail(generics.RetrieveAPIView):

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    lookup_field='computer_name'
    

    # def get_queryset(self):
    #     pdb.set_trace()

    def get_object(self): 
        pdb.set_trace()

    # def get(self, request, *args, **kwargs):
    #     pdb.set_trace()


    # def retrieve(self, request, *args, **kwargs):
    #     pdb.set_trace()

    




# class ComputerList(generics.UpdateAPIView, generics.ListCreateAPIView):

#     serializer_class = ComputerSerializer
#     queryset = Computer.objects.all()

#     def list(self, request, *args, **kwargs):
#         import pdb; pdb.set_trace()


#     def put(self, request, *args, **kwargs):
#         import pdb; pdb.set_trace()






##############################################################################################################

class ComputerListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def get(self, request, *args, **kwargs):
        #pdb.set_trace()
        return self.list(request, *args, **kwargs)

    def post(self,request,*args, **kwargs):
        #pdb.set_trace()
        return self.create(request, *args, **kwargs)



class ComputerDetailSearchMixin(generics.RetrieveUpdateDestroyAPIView):
    
    # dont need queryset if you define self.queryset
    serializer_class = ComputerSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        send GET to computer_name/dev400/ 
        computer_name comes from urls.py & must be a url to use regex & not path 
        but why does int pk work with path? 
        """



        self.lookup_field = self.kwargs['computer_name']
        self.queryset = Computer.objects.filter(computer_name=self.lookup_field)
        serializer = ComputerSerializer(self.queryset, many=True)
        return Response(serializer.data)



#class ComputerDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
# this one is broken ... 
class ComputerDetailMixin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    # why not set lookup_field = self.kwarg here so dont have to in each method?
    #lookup_field = 'bfid'

    # def get_queryset(self):
    #     pdb.set_trace()


    def check_request_params(self, request):
        """
        helper function for update() to check dictionary in request.data
        """
        required_fields = ['computer_name', 'bfid', 'description']
        request_keys = request.data.keys()
        missing_fields = list(set(request_keys) ^ set(required_fields))
        if len(missing_fields) > 0:
           return missing_fields

    def retrieve(self, request, *args, **kwargs):
        """
        send GET to /computer/400/ where 400 is bfid 
        self.kwargs  = is set in urls.py

        """

        #pdb.set_trace()
        self.lookup_field = self.kwargs['bfid']
        queryset = Computer.objects.filter(bfid=self.lookup_field)
        serializer = ComputerSerializer(queryset, many=True)
        return Response(serializer.data)



    def update(self, request, *args, **kwargs):
        """
        send PUT  to computer/400/ where 400 is bfid 
        1. get PUT data from request
        2. check for required params
        3. filter the queryset for the bfid thats at the end of the url (bfid=400)
        4. overwrite everything 
        5. save & pass to serialzier to return 
        """

        # get PUT data
        data = self.request.data 

        # check for all required parameters
        #pdb.set_trace()
        self.check_request_params(self.request)

        # check if bfid to be looked up exists
        queryset = Computer.objects.filter(bfid=self.kwargs['bfid'])
        #pdb.set_trace()

        if queryset:
            queryset[0].computer_name = data.get('computer_name')
            queryset[0].bfid = data.get('bfid')
            queryset[0].description = data.get('description')
            queryset[0].save()
            serializer = ComputerSerializer(queryset[0])
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response({'Unsuccessful': "BFID {} doesnt exist".format(self.kwargs['bfid'])}, status=HTTP_400_BAD_REQUEST)






        # # if bfid exists then update everything 
        # if queryset:
        #     serializer = ComputerSerializer(queryset, data=data)
        #     #pdb.set_trace()
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=HTTP_201_CREATED)


        #     new_computer = Computer.objects.create(
        #         computer_name=data['computer_name'],
        #         bfid=data['bfid'],
        #         description=data['description']
        #     )
        #     serializer = ComputerSerializer(new_computer)
        #     self.perform_update(serializers)
        #     return Response(serializer.data, status=HTTP_201_CREATED)
        # # if not then return bfid that doesnt exist 
        # return Response({'Unsuccessful': "BFID {} doesnt exist".format(self.data['bfid'])}, status=HTTP_400_BAD_REQUEST)




        #pdb.set_trace()

    # def delete(self, request, *args, **kwargs): 
    #     pdb.set_trace()





# class TestViewMixin(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    viewsets.GenericViewSet):




#     def get_queryset(self, *args, **kwargs):
#         # might be able to add comp_name=None to args 
#         comp_name = self.kwargs['comp_name']
#         return Computer.objects.filter(computer_name=comp_name)
#         #import pdb; pdb.set_trace()


##############################################################################################################

# class ComputerListViewSet(viewsets.ModelViewSet):
#     """computers/"""
#     serializer_class = ComputerSerializer
#     queryset = Computer.objects.all()


    # self.action 




    # def list(self, request, *args, **kwargs):
    #     """
    #     send GET to /api/computers/
    #     """
    #     pdb.set_trace()


    # def create (self, *args, **kwargs):
    #     """
    #     send POST to /api/computers/
    #     """
    #     import pdb; pdb.set_trace()


    # def update(self, *args, **kwargs):
    #     """
    #     send PUT to /api/computers/1/
    #     """
    #     import pdb; pdb.set_trace()


    # def retrieve(self, request, *args, **kwargs):
    #     """
    #     send GET to /api/computers/1/ 
    #     """
    #     import pdb; pdb.set_trace()

    # def destroy(self, request, *args, **kwargs):
    #     """
    #     send GET to /api/computers/1/
    #     """#
    #     pdb.set_trace()











# class ComputerByBfidViewSet(viewsets.ModelViewSet):
#     """computer/bfid/789 -- GET/DELETE/POST/PATCH/PUT"""
#     serializer_class = ComputerSerializer
#     lookup_field = 'bfid' # dont think this is needed?????


#     def check_request_params(self, request):
#         """
#         helper function for create() & update() to check dictionary in request.data
#         """
#         required_fields = ['computer_name', 'bfid', 'description']
#         request_keys = request.data.keys()
#         missing_fields = list(set(request_keys) ^ set(required_fields))
#         if len(missing_fields) > 0:
#            return missing_fields


#     def get_queryset(self, *args, **kwargs):
#         """
#         this method is not fired during POST request??
#         """

#         try:
#             #pdb.set_trace()
#             # this is a GET detail view & grabs object form create/update/delete 
#             bfid_kwargs = self.kwargs['bfid']
#             queryset = Computer.objects.filter(bfid=bfid_kwargs)
#             return queryset
#         except Exception as e:
#             # if exception then no BFID parameter passed & GET list 
#             # GET - LIST -  /api/computer/bfid/
#             return Computer.objects.all() 


    # def create(self, *args, **kwargs): 
    #     """
    #     send POST to api/computer/bfid/  -- to create a new computer using its bfid 
    #     1. check to see if all required fields are present 
    #     2. (dont need to validate bfid is unique since unique=True in models.py)
    #     3. create new entry in DB, save, pass to serializer.
    #     """

    #     # validate required fields are there 
    #     bad_data = self.check_request_params(self.request)
    #     if bad_data:
    #          return Response({'Unsuccessful': 'HTTP method - {} -- Missing field - {}'\
    #                 .format(self.action, ", ".join(bad_data))}, status=HTTP_400_BAD_REQUEST) 

    #     # check for unique BFID if unique=True WAS NOT THE CASE 

    #     # if all required fields present -- create new entry in DB, save, & pass to serializer 
    #     data = self.request.data
    #     new_computer = Computer.objects.create(
    #         computer_name=data['computer_name'],
    #         bfid=data['bfid'],
    #         description=data['description']
    #     )
    #     new_computer.save()
    #     serializer = ComputerSerializer(new_computer)
    #     return Response(serializer.data)


    # def update(self,*args, **kwargs):
    #     """
    #     send PUT to - /api/computer/bfid/400/
    #     1. checks to see if all required fields are present
    #     2. checks to see if that bfid exists 
    #     3. gets the object associated with that bfid and overwrite everything 
    #     """

    #     # check if all args are there 
    #     bad_data = self.check_request_params(self.request)
    #     if bad_data:
    #          return Response({'Unsuccessful': 'HTTP method - {} - Missing field - {}'\
    #                 .format(self.action, ", ".join(bad_data))}, status=HTTP_400_BAD_REQUEST) 

    #     # get PUT data
    #     data = self.request.data
    #     # check to see if BFID exists
    #     bfid_exists = Computer.objects.filter(bfid=self.kwargs['bfid'])

    #     # if it does then overwrite everything in that object 
    #     if bfid_exists: 
    #         computer = self.get_object() 
    #         computer.computer_name=data['computer_name']
    #         computer.bfid=data['bfid']
    #         computer.description=data['description']
    #         computer.save()
    #         serializer = ComputerSerializer(computer)
    #         return Response(serializer.data, status=HTTP_201_CREATED)
    #     # if not then return bfid that doesnt exist 
    #     return Response({'Unsuccessful': "BFID {} doesnt exist".format(self.kwargs['bfid'])}, status=HTTP_400_BAD_REQUEST)

    # # delete?? 




# class ComputerByNameViewSet(viewsets.ModelViewSet):
#     """computer/(?P<comp_name>.+) -- GET/POST """ 
#     serializer_class = ComputerSerializer


#     def get_queryset(self, *args, **kwargs):
#         #import pdb; pdb.set_trace()
#         comp_name = self.kwargs['comp_name']
#         queryset = Computer.objects.filter(computer_name=comp_name)
#         # import pdb; pdb.set_trace()
#         return queryset


#     def perform_destroy(self, *args, **kwargs): 
#         pdb.set_trace()


    # def list(self, request, *args, **kwargs):
    #     pdb.set_trace()

    # def retrieve(self, request, *args, **kwargs): 


    


    