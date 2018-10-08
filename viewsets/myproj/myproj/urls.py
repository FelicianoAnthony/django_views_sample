"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from myapp.views import EmployeeListMixin, EmployeeJobListMixin

from myapp.views import EmployeeListNoModelView,EmployeeDetailNoModelView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('employees/', EmployeeListMixin.as_view()),
    #path('employees/<int:pk>/', EmployeeJobListMixin.as_view()),

    # tst urls 
    path('employees/', EmployeeListNoModelView.as_view({'get' : 'list', 'post':'create'})),
    path('employees/<int:pk>/', EmployeeDetailNoModelView.as_view({'get' : 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]
