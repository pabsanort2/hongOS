from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Imagen(models.Model):
    file_name = models.ImageField(upload_to='imagenes_hongos')


class HongOSUser(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

class Hongos(models.Model):

    def image_upload(self,filename):
        return 'imagenes_hongos/'+str(self.uploader.user)+'/'+str(filename)

    nombre = models.CharField(max_length=20, null=False)
    prob = models.CharField(max_length=20, null=False)
    uploader = models.ForeignKey(HongOSUser, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=image_upload)

