from django.db import models

# Create your models here.
# CURSOS
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.camada}"
    
# PROFESORES
class Profesor(models.Model):   
    nombre = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

# ALUMNOS
class Alumno(models.Model): 
    nombre = models.CharField(max_length=40)
    dni = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} - {self.dni}"
