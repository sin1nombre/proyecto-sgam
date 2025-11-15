from django.db import models
from pacientes.models import Pacientes
from profesionales.models import Profesional

class Prestacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_minutos = models.IntegerField()

class Box(models.Model):
    numero = models.IntegerField()
    disponible = models.BooleanField(default=True)

class PrestacionProfesional(models.Model):
    prestacion = models.ForeignKey(Prestacion, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

class Cita(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default="Agendada")