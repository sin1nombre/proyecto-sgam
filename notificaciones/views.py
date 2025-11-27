from django.shortcuts import render
from .models import Notificacion

def listar_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'notificaciones/listar_notificaciones.html', {
        'notificaciones': notificaciones
    })
