from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Paciente

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        try:
            Paciente.objects.create(
                nombre=request.POST['nombre'],
                rut=request.POST['rut'],
                telefono=request.POST['telefono'],
                correo=request.POST['correo'],
                ficha_ehr=request.POST['ficha_ehr']
            )
            return redirect('listar_pacientes')
        except IntegrityError:
            return render(request, 'pacientes/crear_pacientes.html', {
                'error': 'El RUT ya está registrado'
            })

    return render(request, 'pacientes/crear_pacientes.html')

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        paciente.nombre = request.POST.get('nombre')
        paciente.rut = request.POST.get('rut')
        paciente.telefono = request.POST.get('telefono')
        paciente.correo = request.POST.get('correo')
        paciente.ficha_ehr = request.POST.get('ficha_ehr')
        paciente.save()
        return redirect('listar_pacientes')

    return render(request, 'pacientes/editar_pacientes.html', {'paciente': paciente})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('listar_pacientes')
