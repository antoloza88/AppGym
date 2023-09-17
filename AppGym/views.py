from django.shortcuts import render
from AppGym.models import Clientes, Rutina, Profesora
from django.http import HttpResponse
from AppGym.forms import NuevaClientaFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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
  
def leerClientas (request):
   clientas = Clientes.objects.all()
   contexto = {"Clientas": clientas}
   return render(request, "AppGym/leerClientas.html", contexto)

def eliminarClienta(request, clienta_usuario):
   clienta = Clientes.objects.get(usuario = clienta_usuario)
   clienta.delete()

   clientas =Clientes.objects.all()
   contexto = {"Clientas": clientas}

   return render(request, "AppGym/leerClientas.html", contexto)

def editarClienta(request, clienta_usuario):
   clienta = Clientes.objects.get(usuario=clienta_usuario)

   if request.method == 'POST':
      miFormulario = NuevaClientaFormulario(request.POST)
      print(miFormulario)
      
      if miFormulario.is_valid:
         
         informacion = miFormulario.cleaned_data
         clienta.usuario = informacion['usuario']
         clienta.nombre = informacion['nombre']
         clienta.apellido = informacion['apellido']
         clienta.fecha_de_nacimiento = informacion['fecha_de_nacimiento']
         clienta.email = informacion['email']
         clienta.celular = informacion['celular']
         clienta.contraseña = informacion['contraseña']

         clienta.save()

         return render(request, "AppGym/Inicio.html")
   else:
       miFormulario= NuevaClientaFormulario(initial={'usuario': clienta.usuario, 'nombre': clienta.nombre, 'apellido': clienta.apellido, 'fecha_de_nacimiento': clienta.fecha_de_nacimiento, 'email': clienta.email, 'celular': clienta.celular, 'contraseña': clienta.contraseña})

   return render(request, "AppGym/NuevaClientaFormulario.html", {"miFormulario":miFormulario, "clienta_usuario":clienta_usuario})


def login_request(request):
    
   if request.method == "POST":
      form = AuthenticationForm(request, data = request.POST)

      if form.is_valid():
         usuario = form.cleaned_data.get("username")
         contra = form.cleaned_data.get("password")

         user = authenticate(username=usuario, password=contra)

         
         if user is not None:
            login(request, user)

            return render(request, "AppGym/Inicio.html", {"mensaje": f"Bienvenida {usuario}"})

         else:
            
            return HttpResponse(f"Error, datos incorrectos")
      
      else:
        return HttpResponse(f"Error, formulario erroneo")
   
   form = AuthenticationForm()

   return render(request, "AppGym/login.html", {'fomr':form})

