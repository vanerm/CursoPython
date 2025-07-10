from django.contrib import admin
from .models import *   # Import all models from the current app

admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Profesor)

# Register your models here.
