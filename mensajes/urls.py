from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.feed , name='feed'),
    path('post', views.post , name='post'),
    
   
    
]
