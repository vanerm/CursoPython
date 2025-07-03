from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from django.template import loader

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenidos a la AppCoder")

def cursos(request):
    cursos_list = Curso.objects.all()
    cursos_dictionary = {
        "cursos": cursos_list
    }
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(cursos_dictionary, request)
    return HttpResponse(documento)


def alta_curso(request, nombre):
    nuevo_curso = Curso(nombre=nombre, camada=1234)
    nuevo_curso.save()
    return HttpResponse(f"Curso {nuevo_curso.nombre} agregado con éxito")

def profesores(request):
    return render(request, "profesores.html")

def alumnos(request):
    return render(request, "alumnos.html")