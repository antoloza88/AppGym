from django.db import models

# Create your models here.

class Rutina(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField

class Profesora(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)



