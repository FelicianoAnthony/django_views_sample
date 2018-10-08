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
from django.urls import path, include ## add include import 
from myapp.views import CoinViewSet, SearchCoinsViewSet
from rest_framework import routers

from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'coins', CoinViewSet, base_name='coins')

#router.register(r'^coins/(?P<cname>.+)/$', SearchCoinsViewSet.as_view(), base_name='coin_search')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^coins/(?P<coin_name>.+)/$', SearchCoinsViewSet.as_view({'get':'retrieve'}))
    #url(r'^coins/(?P<cname>.+)/$', SearchCoinsViewSet)
]


# router = routers.DefaultRouter()
# router.register(r'coins', CoinViewSet, base_name='coins')
# urlpatterns = router.urls