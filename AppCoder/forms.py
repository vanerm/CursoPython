from django import forms    
from AppCoder.models import Curso

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.camada}"
    
class Alumno_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    dni = forms.CharField(max_length=15)
    def __str__(self):
        return f"{self.nombre} - {self.dni}"
    
class Profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    especialidad = forms.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

   
