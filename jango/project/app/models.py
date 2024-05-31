from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
