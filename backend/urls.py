from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #routes
    path('', views.index),
    #api
    path('api/get/latestsearch', views.ajaxLatestSearch),
    path('api/searchrequest', views.searchRequest),
    path('api/searchbyid', views.ajaxGetSearchById)
]
