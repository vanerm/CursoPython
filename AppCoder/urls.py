from django.urls import path
from .import views

urlpatterns = [
    # Home page
    path('', views.inicio, name='inicio'),
    path('padre/', views.inicio, name='padre'),
    #CURSOS
    path('cursos/', views.cursos, name='cursos'),
    #path('alta_curso/<nombre>', views.alta_curso, name='alta_curso'),
    path('alta_curso', views.curso_formulario, name='curso_formulario'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
    path('buscar', views.buscar, name='buscar'),
    # PROFESORES
    path('profesores/', views.profesores, name='profesores'),
    # ALUMNOS
    path('alumnos/', views.alumnos, name='alumnos'),
    # LOGIN
    path('login/', views.inicio, name='login'),
    # SIGNUP
    path('signup/', views.inicio, name='signup'),
    # CONTACTO
    path('contacto/', views.contacto, name='contacto')
    ]