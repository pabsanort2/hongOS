from django.db import models

# Create your models here.

class Imagen(models.Model):
    file_name = models.ImageField(upload_to='imagenes_hongos')