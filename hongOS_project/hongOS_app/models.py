from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Imagen(models.Model):
    file_name = models.ImageField(upload_to='imagenes_hongos')

class Hongos(models.Model):
    imagen = models.ImageField()
    nombre = models.CharField(max_length=20, null=False)
    prob = models.FloatField(null=False)

class HongOSUser(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    hongos = models.ManyToManyField(Hongos)

