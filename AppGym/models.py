from django.db import models

# Create your models here.

class Rutina(models.Model):
    ID_rutina = models.IntegerField()
    rutina = models.CharField(max_length=50)
    duracion = models.IntegerField()

class Clientes(models.Model):
    usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField()
    celular = models.IntegerField()
    contraseña = models.IntegerField()

class Profesora(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)



