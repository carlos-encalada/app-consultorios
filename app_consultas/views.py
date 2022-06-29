from email import message
import re
from django.http import HttpResponse
from django.shortcuts import render
from app_consultas.models import Consulta, Paciente, Doctor, Avatar
from django.template import loader
from .forms import Consulta_formulario, Paciente_formulario, Doctor_formulario, UserEditForm, Register_form
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from django.forms import forms 
from django.contrib.auth.models import User


# Create your views here.

# View Inicio--------------------------------------
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request,  'padre.html', {'url':avatares[0].image.url})
    else:
        sin_avatar =    '/static/app_consultas/assets/img/blank.png'
        return render (request,'padre.html', {'url':sin_avatar})  
#View Alta------------------------------------------
@login_required
def alta(request):
         return render(request , "alta.html")
    
#View Alta Consulta----------------------------------------------
@login_required
def consulta(request):
    if request.method == 'POST':
         mi_formulario = Consulta_formulario(request.POST)
         if mi_formulario.is_valid():
          datos= mi_formulario.cleaned_data
          consulta = Consulta(fecha_cita=datos['fecha_cita'] , hora=datos['hora'] , nombre_paciente=datos['nombre_paciente'] , apellido_paciente=datos['apellido_paciente'] , email=datos['email'] , tel=datos['tel'] )
          consulta.save()
         return render(request, 'alta.html')
    return render(request, 'consulta.html')


#View Alta Paciente---------------------------------------------------
@login_required
def paciente(request):
    if request.method == 'POST':
         mi_formulario = Paciente_formulario(request.POST)
         if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            paciente = Paciente(nombre=datos['nombre'] , apellido=datos['apellido'] , prescripcion=datos['prescripcion'] , diagnostico=datos['diagnostico'] , fecha_proxima_cita=datos['fecha_proxima_cita'] , hora_proxima_cita=datos['hora_proxima_cita'] )
            paciente.save()
         return render(request, 'alta.html')
    
    return render(request, 'paciente.html')  


#View Alta Doctor----------------------------------------------
@login_required
def doctor(request):
    if request.method == 'POST':
        mi_formulario = Doctor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            doctor = Doctor(nombre=datos['nombre'] , apellido=datos['apellido'] , especialidad=datos['especialidad'] , email=datos['email'] , telefono=datos['telefono'])
            doctor.save()
        return render(request, 'alta.html')
    
    return render(request, 'doctor.html')


#View Busqueda----------------------------------------------
@login_required
def busqueda(request):
    return render(request, 'busqueda.html')


#Buscar consulta----------------------------------------------------------------
@login_required
def buscar_consulta(request):
    if request.GET['nombre_paciente']:
        nombre = request.GET['nombre_paciente']
        consulta = Consulta.objects.filter(nombre_paciente__icontains=nombre)
        return render(request , "resultado_busqueda_consulta.html" , {'consulta':consulta})
    else:
        HttpResponse("Campo vacio")

@login_required
def buscar_paciente(request):
    if request.GET['nombre']:
        nombre =request.GET['nombre']
        consulta_paciente = Paciente.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda_paciente.html" , {'consulta_paciente':consulta_paciente})
    else:
        HttpResponse("Campo vacio")

@login_required
def buscar_doctor(request):
    if request.GET['nombre']:
        nombre =request.GET['nombre']
        consulta_doctor = Doctor.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda_doctor.html" , {'consulta_doctor':consulta_doctor})
    else:
        HttpResponse("Campo vacio")


#Eliminar Registro-----------------------------------------------------------
@login_required
def eliminar_consulta(request , id):
    eliminar_consulta = Consulta.objects.get(id = id)
    eliminar_consulta.delete()
    eliminar_consulta = Consulta.objects.all()
    return render(request, 'registro_eliminado.html', {"eliminar_consulta": eliminar_consulta})

@login_required
def eliminar_paciente(request , id):
    eliminar_paciente = Paciente.objects.get(id = id)
    eliminar_paciente.delete()
    eliminar_paciente = Paciente.objects.all()
    return render(request, 'registro_eliminado.html', {"eliminar_paciente": eliminar_paciente})

@login_required
def eliminar_doctor(request , id):
    eliminar_doctor = Doctor.objects.get(id = id)
    eliminar_doctor.delete()
    eliminar_doctor = Doctor.objects.all()
    return render(request, 'registro_eliminado.html', {"eliminar_doctor": eliminar_doctor})

#------------View Registro Eliminado------------------------------------------
@login_required
def registro_eliminado(request):
    return render(request, 'registro_eliminado.html')


#-------------------Editar Consulta--------------------------------
@login_required
def editar_consulta(request , id):
    consulta = Consulta.objects.get(id = id)
    if request.method == 'POST':
        mi_formulario = Consulta_formulario(request.POST)
        if mi_formulario.is_valid():
           datos = mi_formulario.cleaned_data
           consulta.fecha_cita = datos['fecha_cita']
           consulta.hora = datos['hora']
           consulta.nombre_paciente = datos['nombre_paciente']
           consulta.apellido_paciente = datos['apellido_paciente']
           consulta.email = datos['email']
           consulta.tel = datos['tel']
           consulta.save()
           return render(request, 'registro_editado.html') 

    else:
        mi_formulario = Consulta_formulario(initial = {'fecha_cita': consulta.fecha_cita , 'hora': consulta.hora , 'nombre_paciente': consulta.nombre_paciente , 'apellido_paciente': consulta.apellido_paciente , 'email': consulta.email , 'tel': consulta.tel})
    return render(request, 'editar_consulta.html', {'mi_formulario': mi_formulario , 'consulta': consulta})


    #-------------------Editar Paciente--------------------------------
@login_required
def editar_paciente(request , id):
    paciente = Paciente.objects.get(id = id)
    if request.method == 'POST':
        mi_formulario = Paciente_formulario(request.POST)
        if mi_formulario.is_valid():
           datos = mi_formulario.cleaned_data
           paciente.nombre = datos['nombre']
           paciente.apellido = datos['apellido']
           paciente.prescripcion = datos['prescripcion']
           paciente.diagnostico = datos['diagnostico']
           paciente.fecha_proxima_cita = datos['fecha_proxima_cita']
           paciente.hora_proxima_cita = datos['hora_proxima_cita']
           paciente.save()
           return render(request, 'registro_editado.html') 

    else:
        mi_formulario = Paciente_formulario(initial = {'nombre': paciente.nombre , 'apellido': paciente.apellido , 'prescripcion': paciente.prescripcion , 'diagnostico': paciente.diagnostico , 'fecha_proxima_cita': paciente.fecha_proxima_cita , 'hora_proxima_cita': paciente.hora_proxima_cita})
    return render(request, 'editar_paciente.html', {'mi_formulario': mi_formulario , 'paciente': paciente})

    #-------------------Editar Doctor-------------------------------
@login_required
def editar_doctor(request , id):
    doctor = Doctor.objects.get(id = id)
    if request.method == 'POST':
        mi_formulario = Doctor_formulario(request.POST)
        if mi_formulario.is_valid():
           datos = mi_formulario.cleaned_data
           doctor.nombre = datos['nombre']
           doctor.apellido = datos['apellido']
           doctor.especialidad = datos['especialidad']
           doctor.email = datos['email']
           doctor.telefono = datos['telefono']
           doctor.save()
           return render(request, 'registro_editado.html') 

    else:
        mi_formulario = Doctor_formulario(initial = {'nombre': doctor.nombre , 'apellido': doctor.apellido , 'especialidad': doctor.especialidad , 'email': doctor.email , 'telefono': doctor.telefono})
    return render(request, 'editar_doctor.html', {'mi_formulario': mi_formulario , 'doctor': doctor})


#-------------------View Registro Editado--------------------------------
@login_required
def registro_editado(request):
        return render(request, 'registro_editado.html')
#------------------------------Login----------------------------------------------------------
def login_request(request):
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request , data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            
            
            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                if avatares.exists():
                    return render(request,  'padre.html', {'url':avatares[0].image.url})
                else:
                    sin_avatar =   '/static/app_consultas/assets/img/blank.png'
                    return render (request,'padre.html', {'url':sin_avatar})
                
            return render (request,'usuaContinc.html')     
        else:
            return render(request, "login.html", {'form': form})
        
    form = AuthenticationForm()
        
    return render(request, 'login.html' , {'form':form}) 

#------------------------------Register----------------------------------------------------------
def register(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'usuarioregistrado.html')
    else:
        form = Register_form()
    return render(request, 'registro.html', {'form': form})


#------------------------------Editar Perfil----------------------------------------------------------
@login_required
def editar_perfil(request):

    usuario = request.user
    
    if request.method == 'POST':
       mi_formulario = UserEditForm(request.POST)
       
       if mi_formulario.is_valid():
           
           info = mi_formulario.cleaned_data
           usuario.email = info['email']
           usuario.first_name = info['first_name']
           usuario.last_name = info['last_name']
           password = info['password1']
           usuario.set_password(password)
           usuario.save()
           return render(request, 'registro_editado.html')
    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email , 'first_name':usuario.first_name , 'last_name':usuario.last_name})  
    return render(request, 'editar_perfil.html', {'mi_formulario':mi_formulario , 'usuario': usuario} , )

# Acerca de mi
def about(request):
         return render(request , "about.html")

