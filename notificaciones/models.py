from django.db import models

class Notificacion(models.Model):
    cita = models.ForeignKey("agenda.Cita", on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
