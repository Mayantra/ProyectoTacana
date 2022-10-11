import email
from hashlib import md5
from operator import mod
from pyexpat import model
from re import T
from django.db import models

# Create your models here.
class oficina(models.Model):
    nombre=models.CharField(max_length=250, verbose_name='Nombre', blank=True)
    descripcion= models.TextField(max_length=1500, verbose_name='Descripcion', blank=True)
    direccion = models.CharField(max_length=45, verbose_name='Direccion', blank=True)
    horario = models.CharField(max_length=50, verbose_name='Horario', blank=True)
    diasH = models.CharField(max_length=50, verbose_name='Dias', blank=True)
    foto = models.FileField(upload_to="images/",verbose_name='Foto', blank=True)


    fecha_alta= models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')

    def __str__(self):
        return self.nombre

class encargados(models.Model):
    nombre= models.CharField(max_length=60, verbose_name='Nombre', blank=True)
    dpi =models.CharField(max_length=15, verbose_name='DPI', blank=True)
    telefono = models.CharField(max_length=15, verbose_name='Telefono', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    profesion = models.CharField(max_length=35, verbose_name='Profesion', blank=True)


    fecha_alta= models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')

    def __str__(self):
        return self.nombre

class tipoProyecto(models.Model):
    nombre =models.CharField(max_length=25, verbose_name='Nombre', blank=True)
    descripcion = models.TextField(verbose_name='Descripcion', blank=True)

    fecha_alta= models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')

    def __str__(self):
        return self.nombre

class proyectoslist(models.Model):
    nombre =models.CharField(max_length=250, verbose_name='Nombre',blank=True)
    lugar= models.CharField(max_length=200, verbose_name='Lugar', blank=True)
    fechaApertura = models.DateField(verbose_name="FechaApertura", blank=True)
    fechaFinal = models.DateField(verbose_name='FechaFinal', blank=True)
    presupuesto = models.DecimalField(max_digits=20,decimal_places=3,verbose_name='Presupuesto', blank=True)

    encargado  = models.ForeignKey(encargados, on_delete=models.CASCADE, blank=True)
    tipoProyecto = models.ForeignKey(tipoProyecto, on_delete=models.CASCADE, blank=True, default=1)

    tiempo = models.CharField(max_length=30, verbose_name='Tiempo', blank=True)
    descripcio = models.TextField(verbose_name='Descripcio',blank=True)
    foto = models.FileField(upload_to="images/",verbose_name='Foto', blank=True)




    fecha_alta= models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')

    def __str__(self):
        return self.nombre