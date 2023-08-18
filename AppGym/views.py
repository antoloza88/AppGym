from django.shortcuts import render
from AppGym.models import Clientes, Rutina, Profesora
from django.http import HttpResponse
from AppGym.forms import NuevaClientaFormulario

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

def nuevaclientaformulario(request):
 
      if request.method == "POST":
 
            miFormulario = NuevaClientaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  nuevaclienta = Clientes(usuario=informacion['usuario'], nombre=informacion['nombre'], apellido=informacion['apellido'], fecha_de_nacimiento=informacion['fecha_de_nacimiento'], email=informacion['email'], celular=informacion['celular'], contraseña=informacion['contraseña'])
                  nuevaclienta.save()
                  return render(request, "AppGym/Inicio.html")
      else:
            miFormulario=NuevaClientaFormulario()
 
      return render(request, "AppGym/NuevaClientaFormulario.html", {"miFormulario":miFormulario})


def busquedaClienta(request):
    return render(request, "AppGym/BusquedaClienta.html")

def buscar(request):

    if request.GET["usuario"]:

      usuario = request.GET['usuario']
      email = Clientes.objects.filter(usuario__icontains=usuario)

      return render(request, "AppGym/resultadosBusqueda.html", {"usuario":usuario, "email":email})
    
    else:

        respuesta = "No existe el usuario"

    #return HttpResponse(respuesta)
    return render(request, "AppGym/resultadosBusqueda.html", {"respuesta":respuesta})
