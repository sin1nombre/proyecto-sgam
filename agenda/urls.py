from django.urls import path
from . import views

urlpatterns = [
    path('citas/', views.listar_citas, name="listar_citas"),
    path('citas/crear/', views.crear_cita, name="crear_cita"),
    path('citas/editar/<int:id>/', views.editar_cita, name="editar_cita"),
    path('citas/cancelar/<int:id>/', views.cancelar_cita, name="cancelar_cita"),
]