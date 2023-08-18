from django.urls import path
from AppGym import views
from django.contrib import admin


urlpatterns = [
    path('Inicio', views.inicio, name="Inicio"),
    path('Rutinas', views.rutinas, name="Rutinas"),
    path('Clientas', views.clientas, name="Clientas"),
    path('Profesoras', views.profesoras, name="Profesoras"),
        
]