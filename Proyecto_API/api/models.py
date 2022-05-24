from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.

class Registro(models.Model):
    paciente = models.CharField(max_length=50)
    prescripcion = models.CharField(max_length=200)
    fecha_venc = models.CharField(max_length=20)

class Medicamento(models.Model):
    codigo = models.CharField(max_length=50)
    remedio = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200)
    contenido = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=20)
    gramaje = models.CharField(max_length=20)
    caducidad = models.CharField(max_length=20)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class InsumoMedico(models.Model):
    insumo = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)


    