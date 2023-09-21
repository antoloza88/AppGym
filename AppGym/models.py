from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rutina(models.Model):
    ID_rutina = models.IntegerField()
    rutina = models.CharField(max_length=50)
    duracion = models.IntegerField()

    def __str__(self):
        return f"ID_rutina: {self.ID_rutina} - Rutina: {self.rutina} - Duracion: {self.duracion}"

class Clientes(models.Model):
    usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField()
    celular = models.IntegerField()
    contraseña = models.IntegerField()

    def __str__(self):
        return f"Usuario: {self.usuario} - Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesora(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)


class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)