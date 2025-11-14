from django.shortcuts import render, redirect
from .models import Pacientes

def listar_pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, "pacientes/listar_pacientes.html", {"pacientes": pacientes})

def crear_paciente(request):
    if request.method == "POST":
        Pacientes.objects.create(
            nombre=request.POST["nombre"],
            rut=request.POST["rut"],
            telefono=request.POST["telefono"],
            correo=request.POST["correo"],
            ficha_ehr=request.POST["ficha_ehr"],
        )
        return redirect("listar_pacientes")

    return render(request, "pacientes/crear_paciente.html")
