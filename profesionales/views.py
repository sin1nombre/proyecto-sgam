from django.shortcuts import render, redirect
from .models import Profesional
from .forms import ProfesionalForm

def listar_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'profesionales/listar_profesionales.html', {'profesionales': profesionales})

def crear_profesional(request):
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesionales')
    else:
        form = ProfesionalForm()
    
    return render(request, 'profesionales/crear_profesional.html', {'form': form})