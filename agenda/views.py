from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages

from .models import Cita, Prestacion, Box
from pacientes.models import Pacientes
from profesionales.models import Profesional

def listar_citas(request):
    citas = Cita.objects.select_related("paciente", "prestacion", "profesional", "box")
    return render(request, "agenda/listar_citas.html", {"citas": citas})

def crear_cita(request):
    if request.method == "POST":
        paciente_id = request.POST["paciente"]
        prestacion_id = request.POST["prestacion"]
        profesional_id = request.POST["profesional"]
        box_id = request.POST["box"]
        fecha = request.POST["fecha"]
        hora = request.POST["hora"]

        paciente = Pacientes.objects.get(id=paciente_id)
        prestacion = Prestacion.objects.get(id=prestacion_id)
        profesional = Profesional.objects.get(id=profesional_id)
        box = Box.objects.get(id=box_id)

        cita = Cita.objects.create(
            paciente=paciente,
            prestacion=prestacion,
            profesional=profesional,
            box=box,
            fecha=fecha,
            hora=hora,
            estado="Agendada"
        )

        messages.success(request, "Cita creada exitosamente.")
        return redirect("listar_citas")

    pacientes = Pacientes.objects.all()
    prestaciones = Prestacion.objects.all()
    profesionales = Profesional.objects.all()
    boxes = Box.objects.all()

    return render(request, "agenda/crear_cita.html", {
        "pacientes": pacientes,
        "prestaciones": prestaciones,
        "profesionales": profesionales,
        "boxes": boxes
    })

def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)

    if request.method == "POST":
        cita.paciente_id = request.POST["paciente"]
        cita.prestacion_id = request.POST["prestacion"]
        cita.profesional_id = request.POST["profesional"]
        cita.box_id = request.POST["box"]
        cita.fecha = request.POST["fecha"]
        cita.hora = request.POST["hora"]
        cita.estado = request.POST["estado"]
        cita.save()

        messages.success(request, "Cita actualizada.")
        return redirect("listar_citas")

    return render(request, "agenda/editar_cita.html", {
        "cita": cita,
        "pacientes": Pacientes.objects.all(),
        "prestaciones": Prestacion.objects.all(),
        "profesionales": Profesional.objects.all(),
        "boxes": Box.objects.all(),
    })

def cancelar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.estado = "Cancelada"
    cita.save()
    messages.warning(request, "Cita cancelada.")
    return redirect("listar_citas")
