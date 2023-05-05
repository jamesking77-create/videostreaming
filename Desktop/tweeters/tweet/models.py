from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    tweet = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
