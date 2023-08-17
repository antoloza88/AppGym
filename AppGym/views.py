from django.shortcuts import render
from AppGym.models import Rutina
from django.http import HttpResponse

# Create your views here.
def rutina(self):

    rutina = Rutina(nombre = "Piernas", duracion = "40")
    rutina.save()
    documentoDeTexto = f"---> Rutina: {rutina.nombre}, Duracion: {rutina.duracion}."

    return HttpResponse (documentoDeTexto)