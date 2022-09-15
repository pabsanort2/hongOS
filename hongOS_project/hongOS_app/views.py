import email
from unicodedata import name
from django.shortcuts import render, redirect
from fastbook import load_learner
from pathlib import Path
import os
from django.contrib.auth.models import User
from .models import Hongos, HongOSUser, Imagen, ImagenDataset
from .forms import ImagenForm, HongOSUserForm, UserForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import PIL
from PIL import Image

# Create your views here.

@login_required
def clasificar(request):
    if request.method == 'GET':
        form = ImagenForm(request.POST or None, request.FILES or None)
        return render(request, 'clasificar.html', {'form': form, 'method': request.method})
    if request.method == 'POST':
        form = ImagenForm(request.POST or None, request.FILES or None)
        if request.POST.get('file_name') == '':
            messages.info(request, 'No ha adjuntado ninguna imagen')
            return redirect('/clasificar/')
        if form.is_valid and HongOSUser.objects.filter(user=request.user.id).count() != 0:
            form.save()
            username = request.user.username
            imagePath = os.path.join(settings.BASE_DIR, 'media/imagenes_hongos/' +
                             str(form.cleaned_data.get('file_name')).replace(' ','_'))

            #Buscamos si la imagen está en el set de entrenamiento

            tamanio = os.stat(imagePath).st_size
            picture = PIL.Image.open(imagePath)
            alto, ancho = picture.size
            resolucion = str(alto) + 'x' + str(ancho)
            nombre_archivo = form.cleaned_data.get('file_name')
            if ImagenDataset.objects.filter(tamanio=tamanio, resolucion=resolucion).count() !=0  or ImagenDataset.objects.filter(nombre_archivo=nombre_archivo).count() !=0 :
                messages.info(
                request, 'Es probable que la imagen que haya subido se haya usado para entrenar el modelo de clasificación.')

            path = Path().resolve()
            learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
            clases = ['Agaricus','Amanita','Boletus','Cortinarius','Entoloma','Hygrocybe','Lactarius','Russula','Suillus']
            pred, pred_idx, probs = learner.predict(imagePath)
            print(pred_idx)
            zipped = list(zip(probs, clases))
            srtd = sorted(zipped, key=lambda t: t[0], reverse=True)
            next2 = srtd[1:3]

            hongo2Prob, hongo2Label = next2[0]
            hongo3Prob, hongo3Label = next2[1]
            
            hongo2Prob = '{:.2f}%'.format(hongo2Prob.item()*100)
            hongo3Prob = '{:.2f}%'.format(hongo3Prob.item()*100)

            prob = '{:.2f}%'.format(probs[pred_idx].item()*100)
            userHongOS = HongOSUser.objects.filter(user=request.user.id)[0]
            hongo = Hongos(nombre=pred, prob=prob, uploader=userHongOS,
                           imagen=form.cleaned_data.get('file_name'), nombre2=hongo2Label, prob2=hongo2Prob, nombre3=hongo3Label, prob3=hongo3Prob)
            hongo.save()
            os.remove(imagePath)
            return render(request, 'clasificar.html', {'imagePath': imagePath, 'method': request.method, 'hongo': hongo})
        else:
            messages.info(
                request, 'El usuario con el que está intentando acceder no está correctamente creado, por favor, cree otro o inténtelo de nuevo')
            return redirect('/login/')

@login_required
def cargar(request):
    if request.method == 'GET':
        return render(request, 'cargar.html', {'method': request.method})
    if request.method == 'POST':
        directorios = os.listdir(os.path.join(settings.BASE_DIR, 'Mushrooms'))
        for directorio in directorios:
            imagenes = os.listdir(os.path.join(settings.BASE_DIR, 'Mushrooms/'+directorio))
            print(len(imagenes))
            for imagen in imagenes:
                ruta = os.path.join(settings.BASE_DIR, 'Mushrooms/'+directorio+'/'+imagen)
                tamanio = os.stat(ruta).st_size
                picture = PIL.Image.open(ruta)
                alto, ancho = picture.size
                resolucion = str(alto) + 'x' + str(ancho)
                nombre_archivo = imagen
                imagenDataset = ImagenDataset(especie=directorio, tamanio=tamanio, resolucion=resolucion,nombre_archivo=nombre_archivo)
                imagenDataset.save()
    return render(request, 'cargar.html', {'method': request.method})
        


def registro(request):
    submitted = False
    if request.method == "POST":
        form1 = UserForm(request.POST)
        form2 = HongOSUserForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            gameetUser = form2.save(commit=False)
            gameetUser.user = form1.save()
            gameetUser.save()
            messages.success(request, 'Tu cuenta se creó correctamente!')
            return HttpResponseRedirect('/login')
    else:
        form1 = UserForm()
        form2 = HongOSUserForm()
    return render(request, 'registro.html', {'form1': form1, 'form2': form2})

@login_required
def info(request):
    return render(request,'info.html',{})


@login_required
def busqueda(request):
    if request.method == "POST":
        busqueda = request.POST.get('busqueda')
        hongos = Hongos.objects.filter(nombre__contains=busqueda)

        if len(busqueda) != 0:
            return render(request, 'busqueda.html', {'busqueda': busqueda, 'hongos': hongos})
        else:
            return redirect('/home/')
    else:
        return render(request, 'busqueda.html', {})


def loginView(request):

        if request.method == 'POST':
            if User.objects.filter(
                username=request.POST.get('username')).count() != 0:
                userID = User.objects.filter(
                    username=request.POST.get('username'))[0].id
                if HongOSUser.objects.filter(user=userID).count() != 0:

                    username = request.POST.get('username')
                    password = request.POST.get('password')

                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'La sesión se inició correctamente')
                        return redirect('/home/')
                    else:
                        messages.info(
                            request, 'El usuario o contraseña son incorrectos')
                        return redirect('/login/')
                else:
                    messages.info(
                        request, 'El usuario con el que está intentando acceder no está correctamente creado, por favor, cree otro o inténtelo de nuevo')
                    return redirect('/logout/')
            else:
                messages.info(
                            request, 'El usuario no existe, por favor, regístrese')
                return render(request, 'login.html', {})
        if request.method == 'GET':
            return render(request, 'login.html', {})


@login_required
def home(request):
    hongOSUserID = HongOSUser.objects.filter(user=request.user.id)[0].id
    hongos_from_this_user = Hongos.objects.filter(uploader=hongOSUserID)[:10]
    return render(request, 'home.html', {'hongos': hongos_from_this_user})


@login_required
def logoutView(request):
    logout(request)
    messages.success(request, 'La sesión se cerró correctamente')
    return redirect('/login/')
