from django.contrib import admin
from .models import HongOSUser, Hongos, ImagenDataset


# Register your models here.

admin.site.register(Hongos)
admin.site.register(HongOSUser)
admin.site.register(ImagenDataset)