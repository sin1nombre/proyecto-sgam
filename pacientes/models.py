from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    ficha_ehr = models.CharField(max_length=50)
