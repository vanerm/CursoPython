from django.urls import path
from .import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('padre/', views.inicio, name='padre'),
    path('cursos/', views.cursos, name='cursos'),
    path('alta_curso/<nombre>', views.alta_curso, name='alta_curso'),
    path('profesores/', views.profesores, name='profesores'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('login/', views.inicio, name='login'),
    path('signup/', views.inicio, name='signup'),
    path('contacto/', views.contacto, name='contacto')
]