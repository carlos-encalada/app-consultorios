from email import message
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from app_consultas.models import Avatar
from mensajes.forms import PostForm 
from mensajes.models import Post
from .models import *
from django.template import loader
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from django.forms import forms 
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

# Create your views here.
@login_required
def feed(request):
    posts = Post.objects.all()
    context ={'posts': posts}
    return render(request, 'feed.html', context)

@login_required
def post (request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Mensaje enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form' : form })



