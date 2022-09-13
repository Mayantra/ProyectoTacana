from string import Template
from django.shortcuts import render
from django.views.generic import *

# Create your views here.

#Se encuentra el principal de la página
class indexView (TemplateView):
    template_name = 'index.html'

#Encotramos el apartado donde estarán todos los proyectos
class proyectosView(TemplateView):
    template_name = 'proyectosA.html'

#apartado donde estaran la descripción especifica de cada proyecto
class detallesProject(TemplateView):
    template_name = 'detallesProject.html'

#Pagina para ponerse en contacto
class contactoView(TemplateView):
    template_name = 'contact.html'

class verView(TemplateView):
    template_name = 'service.html'