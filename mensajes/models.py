from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from sqlite3 import Timestamp
import email
import datetime

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default =timezone.now)
    content = models.TextField()

    class Meta: 
        ordering =['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'
