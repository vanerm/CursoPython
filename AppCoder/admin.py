from django.contrib import admin
from AppCoder.models import Curso, Alumno, Profesor, Profile

# Register your models here.
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Profile)
