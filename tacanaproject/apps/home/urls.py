from django.contrib import admin
from django.urls import path 
from .views import *



app_name = 'home'
urlpatterns =[
    path('index/', indexView.as_view(), name='index'),

    path('proyectosA/', proyectosView.as_view(), name='proyectosA'),
    path('detallesproject/<int:pk>/', detallesProject.as_view(), name='detallesproject'),

    path('contacto/', contactoView.as_view(), name='contacto'),
    path('oficinas/', oficinaView.as_view(), name='oficinas'),
    path('login/', loginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('form/', formularioAView.as_view(), name='formAvances'),
    path('formProyecto/', formProView.as_view(), name='formProyecto'),
    path('formTipo/', formTipoView.as_view(), name='formTipo'),


    path('avances/', avancesProyecto.as_view(), name='avances'),
    path('ver/', verView.as_view(), name='ver'),

] 
