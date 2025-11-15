from django.contrib import admin
from django.urls import path, include
from .views import home   # ← IMPORTA LA VISTA

urlpatterns = [
    path('', home, name='home'),   # ← INICIO SIN APP
    path('admin/', admin.site.urls),
    path('citas/', include('agenda.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('profesionales/', include('profesionales.urls')),
]
