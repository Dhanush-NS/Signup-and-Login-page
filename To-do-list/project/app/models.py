from django.db import models

# Create your models here.
class add(models.Model):
    num1 = models.CharField(max_length = 10)
    num2 = models.CharField(max_length= 10)
    result = models.CharField(max_length=15)

def __str__(self):
    return self.num1
    