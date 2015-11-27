from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validate/$', views.validate, name='validate'),
    url(r'^validatelogin/$', views.validatelogin, name='validatelogin'),
    url(r'^home/$', views.home, name='home'),
]