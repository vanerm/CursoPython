from django import forms    
from AppCoder.models import Curso

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.camada}"

   
