from dataclasses import fields
from inspect import Attribute
from django import forms
from .models import *

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
                }
            ),
            'proyecto': forms.Select(
                attrs ={
                    'class':'form-control',
                }
            ),
            'fechas': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'type':'date',

                }
            ),
            'foto': forms.FileInput(
                attrs ={
                    'class':'form-control',
                    'type':'file', 
                    'accept':'image/png,image/jpeg,image/jpg',	

                }
            ),
            'descripcion': forms.Textarea(
                attrs ={
                    'class':'form-control',
                    'rows':'8',
                    

                }
            ),

        }