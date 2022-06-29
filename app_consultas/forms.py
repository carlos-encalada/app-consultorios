from cProfile import label
from email.mime import image
from tokenize import Name
from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class Consulta_formulario(forms.Form):

    fecha_cita = forms.DateField()
    hora = forms.TimeField()
    nombre_paciente = forms.CharField(max_length=50)
    apellido_paciente = forms.CharField(max_length=50)
    email = forms.EmailField()
    tel = forms.IntegerField()

class Paciente_formulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    prescripcion = forms.CharField(max_length=50)
    diagnostico = forms.CharField(max_length=50)
    fecha_proxima_cita = forms.DateField()
    hora_proxima_cita = forms.TimeField()

class Doctor_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    especialidad = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    
class Register_form(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30 , label="Nombre:")
    last_name = forms.CharField(max_length=30 , label="Apellido:")
    password1 = forms.CharField(label="Contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña:", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username' , 'password1', 'password2' , 'email' , 'first_name', 'last_name']
        help_texts = {
            'username': None
        }

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=30)
    first_name = forms.CharField(max_length=30 , label="Nombre:")
    last_name = forms.CharField(max_length=30 , label="Apellido:")
    password1= forms.CharField(label="Contraseña:", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar la contraseña:", widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k:"" for k in fields}
        