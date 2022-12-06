from django.contrib import admin
from django.urls import path
from evaApp import views

urlpatterns = [
    path('trabajadores/', views.listadoTrabajadores),
    path('agregarTrabajador/', views.agregarTrabajador),
    path('actualizarTrabajador/<int:id>', views.actualizarTrabajador),
    path('eliminarTrabajador/<int:id>', views.eliminarTrabajador),
]
