from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# CURSOS
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.camada}"
    
# PROFESORES
class Profesor(models.Model):   
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

# ALUMNOS
class Alumno(models.Model): 
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} - {self.dni}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            # Si no hay avatar, usar las iniciales con UI Avatars
            return f"https://ui-avatars.com/api/?name={self.user.username}&background=random&color=fff"
