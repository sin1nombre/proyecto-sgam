from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita, Box, Prestacion
from pacientes.models import Paciente
from profesionales.models import Profesional
from notificaciones.models import Notificacion

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'agenda/citas/listar_citas.html', {'citas': citas})

def crear_cita(request):
    pacientes = Paciente.objects.all()
    profesionales = Profesional.objects.all()
    prestaciones = Prestacion.objects.all()
    boxes = Box.objects.all()

    if request.method == 'POST':
        cita = Cita.objects.create(
            fecha = request.POST.get('fecha'),
            hora = request.POST.get('hora'),
            estado = request.POST.get('estado'),
            paciente_id = request.POST.get('paciente'),
            profesional_id = request.POST.get('profesional'),
            prestacion_id = request.POST.get('prestacion'),
            box_id = request.POST.get('box'),
        )


        Notificacion.objects.create(
            mensaje=f"Cita agendada para {cita.fecha} a las {cita.hora}",
            cita=cita
        )

        return redirect('listar_citas')

    return render(request, 'agenda/citas/crear_cita.html', {
        'pacientes': pacientes,
        'profesionales': profesionales,
        'prestaciones': prestaciones,
        'boxes': boxes,
    })

def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)

    pacientes = Paciente.objects.all()
    profesionales = Profesional.objects.all()
    prestaciones = Prestacion.objects.all()
    boxes = Box.objects.all()

    if request.method == 'POST':
        cita.fecha = request.POST.get('fecha')
        cita.hora = request.POST.get('hora')
        cita.estado = request.POST.get('estado')
        cita.paciente_id = request.POST.get('paciente')
        cita.profesional_id = request.POST.get('profesional')
        cita.prestacion_id = request.POST.get('prestacion')
        cita.box_id = request.POST.get('box')
        cita.save()

        return redirect('listar_citas')

    return render(request, 'agenda/citas/editar_cita.html', {
        'cita': cita,
        'pacientes': pacientes,
        'profesionales': profesionales,
        'prestaciones': prestaciones,
        'boxes': boxes,
    })

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    return redirect('listar_citas')

def listar_box(request):
    boxes = Box.objects.all()
    return render(request, "agenda/box/listar_box.html", {"boxes": boxes})

def crear_box(request):
    if request.method == "POST":
        numero = request.POST.get("numero")
        disponible = request.POST.get("disponible") == "on"

        Box.objects.create(numero=numero, disponible=disponible)
        return redirect("listar_box")

    return render(request, "agenda/box/crear_box.html")

def editar_box(request, id):
    box = get_object_or_404(Box, id=id)

    if request.method == "POST":
        box.numero = request.POST.get("numero")
        box.disponible = request.POST.get("disponible") == "on"
        box.save()
        return redirect("listar_box")

    return render(request, "agenda/box/editar_box.html", {"box": box})

def eliminar_box(request, id):
    box = get_object_or_404(Box, id=id)
    box.delete()
    return redirect("listar_box")

def listar_prestaciones(request):
    prestaciones = Prestacion.objects.all()
    return render(request, "agenda/prestacion/listar_prestaciones.html", {
        "prestaciones": prestaciones
    })

def crear_prestacion(request):
    if request.method == "POST":
        Prestacion.objects.create(
            nombre=request.POST.get("nombre"),
            descripcion=request.POST.get("descripcion"),
            duracion_minutos=request.POST.get("duracion_minutos"),
        )
        return redirect("listar_prestaciones")

    return render(request, "agenda/prestacion/crear_prestacion.html")

def editar_prestacion(request, id):
    prestacion = get_object_or_404(Prestacion, id=id)

    if request.method == "POST":
        prestacion.nombre = request.POST.get("nombre")
        prestacion.descripcion = request.POST.get("descripcion")
        prestacion.duracion_minutos = request.POST.get("duracion_minutos")
        prestacion.save()
        return redirect("listar_prestaciones")

    return render(request, "agenda/prestacion/editar_prestacion.html", {
        "prestacion": prestacion
    })

def eliminar_prestacion(request, id):
    prestacion = get_object_or_404(Prestacion, id=id)
    prestacion.delete()
    return redirect("listar_prestaciones")