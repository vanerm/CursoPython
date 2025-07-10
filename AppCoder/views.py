from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Alumno, Profesor
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumno_formulario, Profesor_formulario 
from django.contrib import messages
from django.shortcuts import redirect

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
    
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    # Use messages framework to show success message
    messages.success(request, f"Curso {curso.nombre} eliminado con éxito")
    return redirect('cursos')

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.nombre = request.POST["nombre"]
        curso.camada = request.POST["camada"]
        curso.save()
        messages.success(request, f"Curso {curso.nombre} editado con éxito")
        return redirect('cursos')
    return render(request, "editar_curso.html", {"curso": curso})

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
    profesores_list = Profesor.objects.all()
    profesores_dictionary = {
        "profesores": profesores_list
    }
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(profesores_dictionary, request)
    return HttpResponse(documento)

def alta_profesor(request, nombre, especialidad):
    nuevo_profesor = Profesor(nombre=nombre, especialidad=especialidad)
    nuevo_profesor.save()
    return HttpResponse(f"Profesor {nuevo_profesor.nombre} agregado con éxito")

def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre=datos["nombre"], especialidad=datos["especialidad"])
            profesor.save()
            return render(request, "padre.html")
    else:
        mi_formulario = Profesor_formulario()
    return render(request, "profesor_formulario.html", {"profesor_formulario": mi_formulario})

# Buscar profesor
def buscar_profesor(request):
    return render(request, "buscar_profesor.html")
def buscar_profesor_resultado(request):
    if request.POST["nombre"]:
        profesores = Profesor.objects.filter(nombre__icontains=request.POST["nombre"])
        return render(request, "resultado_busqueda_profesor.html", {"profesores": profesores})
    else:
        return HttpResponse("No se ha encontrado profesores con ese nombre")

# Contacto
def contacto(request):
    return render(request, "contacto.html")