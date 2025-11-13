from django.db import models

class Profesional(models.Model):
    nombre = models.CharField(max_length=150)
    especialidad = models.CharField(max_length=50)
