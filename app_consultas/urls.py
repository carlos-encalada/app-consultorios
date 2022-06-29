from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.inicio , name='padre'),
    path('consulta', views.consulta , name='consulta'),
    path('paciente', views.paciente , name='paciente'),
    path('doctor', views.doctor , name='doctor'),
    path('alta', views.alta , name='alta'),
    path('busqueda', views.busqueda , name='busqueda'),
    path('buscar_consulta' , views.buscar_consulta , name='buscar_consulta'),
    path('buscar_paciente' , views.buscar_paciente , name='buscar_paciente'),    
    path('buscar_doctor' , views.buscar_doctor , name='buscar_doctor'),
    path('eliminar_consulta/<int:id>' , views.eliminar_consulta , name='eliminar_consulta'),
    path('eliminar_paciente/<int:id>' , views.eliminar_paciente , name='eliminar_paciente'),
    path('eliminar_doctor/<int:id>' , views.eliminar_doctor , name='eliminar_doctor'),
    path('registro_eliminado', views.registro_eliminado , name='registro_eliminado'),
    path('editar_consulta/<int:id>/', views.editar_consulta, name='editar_consulta'), 
    path('editar_consulta', views.editar_consulta, name='editar_consulta'), 
    path('editar_paciente/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('editar_paciente', views.editar_paciente, name='editar_paciente'),
    path('editar_doctor/<int:id>/', views.editar_doctor, name='editar_doctor'),
    path('editar_doctor', views.editar_doctor, name='editar_doctor'),
    path('registro_editado', views.registro_editado, name='registro_editado'), 
    path('login', views.login_request , name='login'),
    path('register', views.register , name='register'),
    path('logout', LogoutView.as_view(template_name="logout.html") , name="logout"),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('about', views.about, name='about'),
    
   
    
    
]