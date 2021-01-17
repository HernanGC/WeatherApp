from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #routes
    path('', views.index),
    #api
    path('api/add', views.ajaxAddSearch),
    path('api/get/latestsearch', views.ajaxLatestSearch)
]
