from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_profesionales, name='listar_profesionales'),
    path('crear/', views.crear_profesional, name='crear_profesional'),
    path('editar/<int:id>/', views.editar_profesional, name='editar_profesional'),
    path('eliminar/<int:id>/', views.eliminar_profesional, name='eliminar_profesional'),
]
