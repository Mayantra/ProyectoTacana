from string import Template
from django.shortcuts import render
from django.views.generic import *

# Create your views here.

class indexView (TemplateView):
    template_name = 'index.html'

class proyectosView(TemplateView):
    template_name = 'proyectosA.html'

class verView(TemplateView):
    template_name = 'service.html'