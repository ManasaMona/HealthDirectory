from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^validate/$', views.validate, name='validate'),
        url(r'validatelogin/$', views.validatelogin, name='validatelogin'),
        url(r'regislogin/$', views.regislogin, name='regislogin'),
        url(r'searchresults/$', views.searchresults, name='searchresults'),
        url(r'editprofile/$', views.editprofile, name='editprofile'),
        url(r'updateprofile/$', views.updateprofile, name='updateprofile'),
        

]