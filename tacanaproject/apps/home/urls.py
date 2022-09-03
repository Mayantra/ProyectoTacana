from django.contrib import admin
from django.urls import path 
from .views import *

app_name = 'home'
urlpatterns =[
    path('index/', indexView.as_view(), name='index'),
    path('proyectosA/', proyectosView.as_view(), name='proyectosA'),
    path('ver/', verView.as_view(), name='ver'),
]