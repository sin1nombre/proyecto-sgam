from django.shortcuts import render, redirect
from .models import Profesional

def listar_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, "profesionales/listar_profesionales.html", {"profesionales": profesionales})

def crear_profesional(request):
    if request.method == "POST":
        Profesional.objects.create(
            nombre=request.POST["nombre"],
            especialidad=request.POST["especialidad"],
            nro_licencia=request.POST["nro_licencia"],
        )
        return redirect("listar_profesionales")
    return render(request, "profesionales/crear_profesional.html")