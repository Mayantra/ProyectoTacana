from string import Template
from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.views import *

from .models import *

# Create your views here.

#Se encuentra el principal de la página
class indexView (TemplateView):
    template_name = 'index.html'

#Encotramos el apartado donde estarán todos los proyectos
class proyectosView(ListView):
    model =proyectoslist
    template_name = 'proyectosA.html'

#apartado donde estaran la descripción especifica de cada proyecto
class detallesProject(TemplateView):
    template_name = 'detallesProject.html'

#Pagina para ponerse en contacto
class contactoView(TemplateView):
    template_name = 'contact.html'

class oficinaView(ListView):
    model = oficina
    template_name = 'oficinas.html'

    

class loginView(LoginView):
    template_name = 'registro/login.html'

class avancesProyecto(TemplateView):
    template_name = 'avances.html'

    
#-------------------------------------------------
#Formularios del perfil de encargados 
class formularioAView(TemplateView):
    template_name = 'formAvances.html'

class formProView(TemplateView):
    template_name = 'formProyecto.html'

class formTipoView(TemplateView):
    template_name = 'formTipo.html'
#-----------------------------------------------



class verView(TemplateView):
    template_name = 'avances.html'