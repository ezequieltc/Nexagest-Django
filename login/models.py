from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 30)
    email = models.CharField(max_length=200)
    usuario = models.CharField(max_length=100, unique= True)
    contrasena = models.CharField(max_length=100)
    admin = models.BooleanField(default= False)
