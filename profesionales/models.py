from django.db import models

class Profesional(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono Contacto")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    horario = models.TextField(verbose_name="Horario de Atención", help_text="Ej: Lunes a Viernes de 9:00 a 18:00")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
