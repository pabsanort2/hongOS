from django.shortcuts import render
from fastbook import load_learner
from pathlib import Path

from .models import Imagen
from .forms import ImagenModelForm

# Create your views here.

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

        