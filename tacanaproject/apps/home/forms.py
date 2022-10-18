from dataclasses import fields
from inspect import Attribute
from pyexpat import model
from django import forms
from .models import *

#Formulario para agregar los avances de cada proyecto
class formAvances(forms.ModelForm):
    class Meta:
        model = avances
        fields=[
            'titulo',
            'proyecto',
            'descripcion',
            'fechas',
            'foto',
        ]
        widgets ={
            'titulo': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Titulo del Avance',
                    'required':'required',
                }
            ),
            'proyecto': forms.Select(
                attrs ={
                    'class':'form-control',
                    'required':'required',
                }
            ),
            'fechas': forms.DateInput(
                attrs ={
                    'class':'form-control',
                    'type':'date',
                    'required':'required',

                }
            ),
            'foto': forms.FileInput(
                attrs ={
                    'class':'form-control',
                    'type':'file', 
                    'accept':'image/png,image/jpeg,image/jpg',	
                    'required':'required',

                }
            ),
            'descripcion': forms.Textarea(
                attrs ={
                    'class':'form-control',
                    'rows':'8',
                    'required':'required',
                    'placeholder':'Descripción',
                    

                }
            ),

        }

#Formulario para agregar nuevos proyectos 
class formProyectos(forms.ModelForm):
    class Meta:
        model = proyectoslist
        fields =[
            'nombre',
            'lugar',
            'fechaApertura',
            'fechaFinal',
            'presupuesto',
            'encargado',
            'tipoProyecto',
            'tiempo',
            'descripcio',
            'foto',
        ]
        widgets ={
            'nombre': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Nombre del Proyecto',
                    'required':'required',
                }
            ),
            'lugar': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Direccion completa: Zona, Av, Aldea, Municipio',
                    'required':'required',
                }
            ),
            'fechaApertura':forms.DateInput(
                attrs ={
                    'class':'form-control',
                    'type':'date',
                    'required':'required',
                    

                }
            ),
            'fechaFinal':forms.DateInput(
                attrs ={
                    'class':'form-control',
                    'type':'date',
                    'required':'required',

                }
            ),
            'presupuesto': forms.NumberInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'250700.55',
                    'required':'required',
                }
            ),
            'encargado': forms.Select(
                attrs ={
                    'class':'form-control',
                    'required':'required',
                }
            ),
            'tipoProyecto': forms.Select(
                attrs ={
                    'class':'form-control',
                    'required':'required',
                }
            ),
            'tiempo': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Ejemplo: 2 meses, 20 días',
                    'required':'required',
                }
            ),
            'descripcio': forms.Textarea(
                attrs ={
                    'class':'form-control',
                    'rows':'8',
                    'required':'required',
                    'placeholder':'Descripción específica del proyecto',
                    

                }
            ),
            'foto': forms.FileInput(
                attrs ={
                    'class':'form-control',
                    'type':'file', 
                    'accept':'image/png,image/jpeg,image/jpg',	
                    'required':'required',

                }
            ),
        }

#Formulario para los tipos de proyectos
class formTipo(forms.ModelForm):
    class Meta:
        model = tipoProyecto
        fields=[
            'nombre',
            'descripcion',
        ]
        widgets ={
            'nombre': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Nombre del TIPO de proyecto',
                    'required':'required',
                }
            ),
            'descripcion': forms.Textarea(
                attrs ={
                    'class':'form-control',
                    'rows':'8',
                    'required':'required',
                    'placeholder':'Descripción específica del tipo de proyecto',
                }
            ),
        }
