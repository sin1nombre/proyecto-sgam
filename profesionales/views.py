from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesional

def listar_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'profesionales/listar_profesionales.html', {
        'profesionales': profesionales
    })

def crear_profesional(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        rut = request.POST.get('rut')
        especialidad = request.POST.get('especialidad')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        horario = request.POST.get('horario')

        Profesional.objects.create(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            especialidad=especialidad,
            telefono=telefono,
            correo=correo,
            horario=horario
        )

        return redirect('listar_profesionales')

    return render(request, 'profesionales/crear_profesionales.html')

def editar_profesional(request, id):
    profesional = get_object_or_404(Profesional, id=id)

    if request.method == 'POST':
        profesional.nombre = request.POST.get('nombre')
        profesional.apellido = request.POST.get('apellido')
        profesional.rut = request.POST.get('rut')
        profesional.especialidad = request.POST.get('especialidad')
        profesional.telefono = request.POST.get('telefono')
        profesional.correo = request.POST.get('correo')
        profesional.horario = request.POST.get('horario')
        profesional.save()

        return redirect('listar_profesionales')

    return render(request, 'profesionales/editar_profesionales.html', {
        'profesional': profesional
    })

def eliminar_profesional(request, id):
    profesional = get_object_or_404(Profesional, id=id)
    profesional.delete()
    return redirect('listar_profesionales')