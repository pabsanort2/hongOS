from django import forms
from .models import Imagen, HongOSUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ImagenModelForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ('file_name',)

class HongOSUserForm(forms.ModelForm):

    class Meta:
        model = HongOSUser
        fields = (
            'email',
        )  #If we want all parameters we can just use fields = "_all_"
        error_messages = {
            'email': {
                'unique':("Ya existe un usuario con este correo electrónico"),
            },
        }

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1','password2')
        error_messages = {
            'username': {
                'unique':("Ya existe un usuario con este nombre de usuario"),
            },
        }