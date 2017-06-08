#coding=utf-8

from  webapp import views
from django.conf.urls import url, include


urlpatterns = [

    url(r'^$', views.view_get_example, name='example'),
    url(r'^readme.json/$', views.view_get_json, name='getJson'),
]



