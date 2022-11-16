from django.db import models
from datetime import date
# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    consulta = models.CharField(max_length=450)

class Post(models.Model):
    titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=450)