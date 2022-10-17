from django.views.generic import *
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.

#Se encuentra el principal de la página
class indexView (TemplateView):
    template_name = 'index.html'

#Encotramos el apartado donde estarán todos los proyectos
class proyectosView(ListView):
    model =proyectoslist
    template_name = 'proyectosA.html'

    queryset = proyectoslist.objects.order_by('-fecha_actualizacion')



#apartado donde estaran la descripción especifica de cada proyecto
class detallesProject(DetailView):
    model =proyectoslist
    template_name = 'detallesProject.html'



    

#Pagina para ponerse en contacto
class contactoView(TemplateView):
    template_name = 'contact.html'



class oficinaView(ListView):
    model = oficina
    template_name = 'oficinas.html'


    

class loginView(LoginView):
    template_name = 'registro/login.html'



class avancesProyecto(ListView):
    model = avances
    template_name = 'avances.html'

    

    queryset = avances.objects.order_by('-id')
    
    queryset = avances.objects.filter(proyecto='1')



    
#-------------------------------------------------
#Formularios del perfil de encargados 
class formularioAView(CreateView):
    model = avances
    form_class = formAvances
    template_name = 'formAvances.html'
    success_url = reverse_lazy('home:formAvances')
    

class formProView(TemplateView):
    template_name = 'formProyecto.html'

class formTipoView(TemplateView):
    template_name = 'formTipo.html'
#-----------------------------------------------



class verView(TemplateView):
    template_name = 'avances.html'