from django.urls import path
from AppGym import views
from django.contrib import admin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Rutinas', views.rutinas, name="Rutinas"),
    path('Clientas', views.clientas, name="Clientas"),
    path('Profesoras', views.profesoras, name="Profesoras"),
    path('NuevaClientaFormulario', views.nuevaclientaformulario, name="NuevaClientaFormulario"),
    path('busquedaClienta', views.busquedaClienta, name="BusquedaClienta"),
    path('buscar/', views.buscar),
    path('leerClientas', views.leerClientas, name="LeerClientas"),
    path('eliminarClienta/<clienta_usuario>/', views.eliminarClienta, name="EliminarClienta"),
    path('editarClienta/<clienta_usuario>/', views.editarClienta, name= "EditarClienta"),
    path('login', views.login_request, name = 'Login'),
    path("registro" , views.register, name="registro"),
    path('logout', LogoutView.as_view(template_name="AppGym/logout.html"), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil")
]