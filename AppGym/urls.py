from django.urls import path
from AppGym import views
from django.contrib import admin


urlpatterns = [
    path('Inicio', views.inicio, name="Inicio"),
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
    
]