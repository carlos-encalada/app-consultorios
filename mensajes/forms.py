from cProfile import label
from dataclasses import field
from email.mime import image
from pyexpat import model
from tokenize import Name
from unicodedata import name
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import *

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Comentarios'}), required=True)

    class Meta:
        model = Post
        fields = ['content']
