from django import forms    
from AppCoder.models import Curso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

   
