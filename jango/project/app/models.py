from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, default='')
    email = models.EmailField(default='')
    password1 = models.CharField(max_length=40)
    password2 = models.CharField(max_length=40)

    def __str__(self):
        return self.name

