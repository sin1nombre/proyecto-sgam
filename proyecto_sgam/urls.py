from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('pacientes/', include('pacientes.urls')),
    path('profesionales/', include('profesionales.urls')),
    path('citas/', include('agenda.urls')),
    path('notificaciones/', include('notificaciones.urls')),
]
