VIEWSETS - LIST & DETAIL view 



IN VIEWS.PY 

class CoinViewSet(viewsets.ViewSet):


	def list(self, request):
	def retrieve(self, request, pk=None):
	def update(self, request, pk=None):
	def partial_update(self, request, pk=None):
	def destroy(self, request, pk=None):




IN URLS.PY 

	If using routers dont need to specify ...as_view({'get': 'list'...}) & can just do ... 
		router = routers.DefaultRouter()
		router.register(r'coins', CoinViewSet, base_name='coins')

	If not using routers ... 
		path('employees/', EmployeeListViewSet.as_view({'get' : 'list', 'post':'create'})),
		path('employees/<int:pk>/', EmployeeListViewSet.as_view({'get' : 'retrieve', 'put': 'update', 'delete': 'destroy'})),



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

MIXINS - LIST VIEW 

IN VIEWS.PY 


class ComputerListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
    def post(self,request,*args, **kwargs):


IN URLS.PY 

	path('computers/', ComputerListMixin.as_view()),



MIXINS - DETAIL VIEW 
	



class ComputerDetailSearchMixin(generics.RetrieveUpdateDestroyAPIView): # & maybe generics.ListCreateAPIView)

	def retrieve(self, request, *args, **kwargs):
	def update(self, request, *args, **kwargs):
	def delete(self, request, *args, **kwargs)

IN URLS.PY 

	from django.conf.urls import url
	url(r'^computer_name/(?P<computer_name>.+)/$', ComputerDetailSearchMixin.as_view()),




>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

MODELVIEWSETS - LISTN & DETAIL VIEW 

IN VIEWS.PY 

	class ComputerByNameViewSet(viewsets.ModelViewSet):
		def list(self, request, *args, **kwargs):
		def create (self, *args, **kwargs):
		def update(self, *args, **kwargs):
		def retrieve(self, request, *args, **kwargs):
		def destroy(self, request, *args, **kwargs):






















