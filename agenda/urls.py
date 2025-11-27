from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_citas, name='listar_citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('editar/<int:id>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:id>/', views.eliminar_cita, name='eliminar_cita'),

    path('box/', views.listar_box, name='listar_box'),
    path('box/crear/', views.crear_box, name='crear_box'),
    path('box/editar/<int:id>/', views.editar_box, name='editar_box'),
    path('box/eliminar/<int:id>/', views.eliminar_box, name='eliminar_box'),

    path('prestaciones/', views.listar_prestaciones, name='listar_prestaciones'),
    path('prestaciones/crear/', views.crear_prestacion, name='crear_prestacion'),
    path('prestaciones/editar/<int:id>/', views.editar_prestacion, name='editar_prestacion'),
    path('prestaciones/eliminar/<int:id>/', views.eliminar_prestacion, name='eliminar_prestacion'),
]
