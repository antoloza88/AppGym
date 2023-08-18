from django.shortcuts import render
from AppGym import models
from django.http import HttpResponse

# Create your views here.
def inicio(request):
   return HttpResponse('Vista de Inicio')

def inicio(request):
   return render(request, "AppGym/Inicio.html")

def rutinas(request):
   return render(request, "AppGym/Rutina.html")

def clientas(request):
   return render(request, "AppGym/Clientas.html")

def profesoras(request):
   return render(request, "AppGym/Profesoras.html")

