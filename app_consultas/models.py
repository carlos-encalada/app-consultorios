import email
from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Consulta(models.Model):
    fecha_cita = models.DateField()
    hora = models.TimeField()
    nombre_paciente = models.CharField(max_length=50)
    apellido_paciente = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.IntegerField()

    def __str__(self):
        return f" {self.nombre_paciente} {self.apellido_paciente}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    prescripcion = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=50)
    fecha_proxima_cita = models.DateField()
    hora_proxima_cita = models.TimeField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg' , upload_to='avatars', null=True, blank=True)
    
    def __srt__(self):
        return f'{self.image} Avatar'