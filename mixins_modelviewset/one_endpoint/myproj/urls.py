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
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


# from myapp.views import (
#                         ComputerListViewSet, 
#                         ComputerByBfidViewSet, 
#                         ComputerByNameViewSet
#                         )


from myapp.views import ComputerListMixin, ComputerDetailMixin, ComputerDetailSearchMixin
import re
from django.conf.urls import url
# from myapp.views import TestGenericsView

#from myapp.views import ComputerList, ComputerDetail




router = routers.DefaultRouter()
# this goes with generics in views.py -- probably have to define it as path in url_patterns
#router.register(r'computers/', TestGenericsView, base_name='computers')


# this goes with mixins in views.py
# router.register(r'computers/(?P<comp_name>.+)', TestViewMixin, base_name='computers')
# router.register('computers/', TestViewMixin, base_name='computers')





# this goes with viewsets in views.py 
# router.register('computers', ComputerListViewSet, base_name='all_computers'),
# # this is the incorrect way but I get all HTTP methods
# router.register('computer/bfid', ComputerByBfidViewSet, base_name='bfid')
# # this is the correct way but I only GET & POST 
# router.register(r'computer/(?P<comp_name>.+)', ComputerByNameViewSet, base_name='bfid')




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    #path('computers/', TestGenericsView.as_view()),
    #path('computers/', ComputerList.as_view()), # GET/POST 
    #path('computer/(?P<pk>\d+)$', ComputerDetail.as_view()), # GET(detail)/PUT/PATCH/DELETE
    path('computers/', ComputerListMixin.as_view()),
    path('computer/<int:bfid>/', ComputerDetailMixin.as_view()),
    url(r'^computer_name/(?P<computer_name>.+)/$', ComputerDetailSearchMixin.as_view()),

    # JWT permissions 
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
]