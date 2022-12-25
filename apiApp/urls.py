from django.urls import path
from apiApp import views

urlpatterns = [
    path('Trabajador/', views.listadoTrabajadores),
    path('DetallesTrabajador/<int:id>', views.detalles_Trabajadores),
    path('Consola/', views.listadoConsolas),
    path('DetallesConsola/<int:id>', views.detalles_Consolas),
    path('Videojuego/', views.listadoVideojuegos),
    path('DetallesVideojuego/<int:id>', views.detalles_Videojuego),   
]