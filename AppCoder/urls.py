from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = 'AppCoder.urls.custom_404'

urlpatterns = [
    # Home page
    path('', views.inicio, name='inicio'),
    path('padre/', views.inicio, name='padre'),
    # CURSOS
    path('cursos/', views.cursos, name='cursos'),
    #path('alta_curso/<nombre>', views.alta_curso, name='alta_curso'),
    path('alta_curso', views.curso_formulario, name='curso_formulario'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
    path('buscar', views.buscar, name='buscar'),
    path('eliminar_curso/<int:id>', views.eliminar_curso, name='eliminar_curso'),
    path('editar_curso/<int:id>', views.editar_curso, name='editar_curso'),
    # PROFESORES
    path('profesores/', views.profesores, name='profesores'),
    path('alta_profesor', views.profesor_formulario, name='profesor_formulario'),
    path('buscar_profesor/', views.buscar_profesor, name='buscar_profesor'),
    path('buscar_profesor_resultado', views.buscar_profesor_resultado, name='buscar_profesor_resultado'),
    path('eliminar_profesor/<int:id>', views.eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor/<int:id>', views.editar_profesor, name='editar_profesor'),
    # ALUMNOS
    path('alumnos/', views.alumnos, name='alumnos'),
    path('alta_alumno', views.alumno_formulario, name='alumno_formulario'),
    path('buscar_alumno/', views.buscar_alumno, name='buscar_alumno'),
    path('buscar_alumno_resultado', views.buscar_alumno_resultado, name='buscar_alumno_resultado'),
    path('eliminar_alumno/<int:id>', views.eliminar_alumno, name='eliminar_alumno'),
    path('editar_alumno/<int:id>', views.editar_alumno, name='editar_alumno'),
    # LOGIN
    path('login/', views.login_request, name='login'),
    # LOGOUT
    #path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('logout/', views.logout_request, name='logout'),
    # SIGNUP
    path('signup/', views.signup, name='signup'),
    # CONTACTO
    path('contacto/', views.contacto, name='contacto'),
    # PERFIL
    path('perfil/', views.perfil, name='perfil'),
    # EDITAR PERFIL
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    # Page 404 Not Found
    path('test404/', views.error_personalizado, name='test404')
    ]