from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notificaciones, name='listar_notificaciones'),
]
