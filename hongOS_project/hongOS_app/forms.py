from django import forms
from .models import Imagen

class ImagenModelForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ('file_name',)