from django.shortcuts import render, redirect
from fastbook import load_learner
from pathlib import Path

from .models import Imagen
from .forms import ImagenModelForm, HongOSUserForm, UserForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def clasificar(request):
    if request.method == 'GET':
        form = ImagenModelForm(request.POST or None, request.FILES or None)
        return render(request, 'clasificar.html', {'form':form, 'method':request.method})
    if request.method == 'POST':
        form = ImagenModelForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            form.save()
            imagePath = Path('imagenes_hongos/' + str(form.cleaned_data.get('file_name')))
            path = Path().resolve()
            learner = load_learner(path/'89,1207.pkl')
            pred,pred_idx,probs = learner.predict(imagePath)
            return render(request, 'clasificar.html', {'imagePath': imagePath, 'predictedCategory': pred, 'method':request.method, 'prob': probs[pred_idx].item()*100})

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
    return render(request,'registro.html',{'form1': form1, 'form2': form2})

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'La sesión se inició correctamente')
            return redirect('/home/')
        else:
            messages.info(request, 'El usuario o contraseña son incorrectos')
            return redirect('/login/')
    if request.method == 'GET':
        return render(request, 'login.html',{})

@login_required
def home(request):
    return render(request, 'home.html',{})

@login_required
def logoutView(request):
    logout(request)
    messages.success(request,'La sesión se cerró correctamente')
    return redirect('/login/')
