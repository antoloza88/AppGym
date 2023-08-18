from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import datetime

def saludo(request):
    return HttpResponse("Bienvenidos a mi primera pagina WEB")

def ProbandoTemplate(self):
    nom = "Antonella"
    ap = "Loza"
    dia = datetime.datetime.now()

    diccionario = {"nombre":nom, "apellido":ap, "dia":dia}
    #miHtml = open("C:/Users/antonella.loza/Documents/Training/Curso_Coder_Python/Tercera_pre-entrega+Loza/tercera_pre-entrega/TerceraPreEntrega/TerceraPreEntrega/plantillas/template1.html")
    #plantilla = Template(miHtml.read())
    #miHtml.close()
    #miContexto = Context(diccionario)
    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)



