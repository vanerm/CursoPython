from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Alumno, Profesor
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumno_formulario, Profesor_formulario 

# Create your views here.
def inicio(request):
    return render(request, "padre.html")

# CURSOS
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
        return HttpResponse("No se ha encontrado cursos con ese nombre")

# ALUMNOS
def alumnos(request):
    alumnos_list = Alumno.objects.all()
    alumnos_dictionary = {
        "alumnos": alumnos_list
    }
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(alumnos_dictionary, request)
    return HttpResponse(documento)




def alta_alumno(request, nombre, dni):
    nuevo_alumno = Alumno(nombre=nombre, dni=dni)
    nuevo_alumno.save()
    return HttpResponse(f"Alumno {nuevo_alumno.nombre} agregado con éxito")

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=datos["nombre"], dni=datos["dni"])
            alumno.save()
            return render(request, "padre.html")
    else:
        mi_formulario = Alumno_formulario()
    return render(request, "alumno_formulario.html", {"alumno_formulario": mi_formulario})

def buscar_alumno(request):
    return render(request, "buscar_alumno.html")

def buscar_alumno_resultado(request):
    if request.POST["nombre"]:
        alumnos = Alumno.objects.filter(nombre__icontains=request.POST["nombre"])
        return render(request, "resultado_busqueda_alumno.html", {"alumnos": alumnos})
    else:
        return HttpResponse("No se ha encontrado alumnos con ese nombre")
    
# PROFESORES
def profesores(request):
    return render(request, "profesores.html")

# Contacto
def contacto(request):
    return render(request, "contacto.html")