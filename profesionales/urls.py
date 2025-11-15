from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_profesionales, name="listar_profesionales"),
    path('crear/', views.crear_profesional, name="crear_profesional"),
]
