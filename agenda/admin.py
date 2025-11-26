from django.contrib import admin
from .models import Cita, Prestacion, Box, PrestacionProfesional

admin.site.register(Cita)
admin.site.register(Prestacion)
admin.site.register(Box)
admin.site.register(PrestacionProfesional)