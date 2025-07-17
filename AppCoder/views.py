from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Alumno, Profesor
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumno_formulario, Profesor_formulario, UserEditForm 
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

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
           # Use messages framework to show success message  
           messages.success(request, f"Curso {curso.nombre} agregado con éxito")
           return redirect('cursos')           
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
    
@login_required    
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    # Use messages framework to show success message
    messages.success(request, f"Curso {curso.nombre} eliminado con éxito")
    return redirect('cursos')

@login_required
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
            # Use messages framework to show success message
            messages.success(request, f"Alumno {alumno.nombre} agregado con éxito")
            return redirect('alumnos')
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

@login_required 
def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    # Use messages framework to show success message
    messages.success(request, f"Alumno {alumno.nombre} eliminado con éxito")
    return redirect('alumnos')

@login_required 
def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        alumno.nombre = request.POST["nombre"]
        alumno.dni = request.POST["dni"]
        alumno.save()
        # Use messages framework to show success message
        messages.success(request, f"Alumno {alumno.nombre} editado con éxito")
        return redirect('alumnos')
    return render(request, "editar_alumno.html", {"alumno": alumno})

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
            # Use messages framework to show success message
            messages.success(request, f"Profesor {profesor.nombre} agregado con éxito")
            return redirect('profesores')
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

@login_required 
def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    # Use messages framework to show success message
    messages.success(request, f"Profesor {profesor.nombre} eliminado con éxito")
    return redirect('profesores')

@login_required 
def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        profesor.nombre = request.POST["nombre"]
        profesor.especialidad = request.POST["especialidad"]
        profesor.save()
        # Use messages framework to show success message
        messages.success(request, f"Profesor {profesor.nombre} editado con éxito")
        return redirect('profesores')
    return render(request, "editar_profesor.html", {"profesor": profesor})

# Contacto
def contacto(request):
    return render(request, "contacto.html")

# Login
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {username}")
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {username}"})
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
                return render(request, "error.html", {"mensaje":f"Usuario no encontrado: {username}"})
        else:
            messages.error(request, "Formulario inválido")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# Logout
def logout_request(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente")
    return render(request, "logout.html")

#Signup
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente")
            return redirect('login')
    else:
        form = UserCreationForm()   
    return render(request, "signup.html", {"form":form})

# Editar perfil

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            messages.success(request, "Perfil actualizado exitosamente")
            return redirect('inicio')
            
    else:
        mi_formulario = UserEditForm(initial={
            "email": usuario.email
        })
    return render(request, "editar_perfil.html", {"miFormulario": mi_formulario, "usuario": usuario})
