from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from django.template import loader
from AppCoder.forms import Curso_formulario 

# Create your views here.
def inicio(request):
    return render(request, "padre.html")

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

def contacto(request):
    return render(request, "contacto.html")

def curso_formulario(request):
    if request.method == "POST":
       mi_formulario = Curso_formulario( request.POST )
       if mi_formulario.is_valid():
           datos = mi_formulario.cleaned_data 
           curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
           curso.save()
           return render(request, "padre.html")           
    else:
       mi_formulario = Curso_formulario()
    return render( request , "formulario.html", {"formulario": mi_formulario})

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    if request.POST["nombre"]:
        cursos = Curso.objects.filter(nombre__icontains=request.POST["nombre"])
        return render(request, "resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("No se ha encontrado nada")