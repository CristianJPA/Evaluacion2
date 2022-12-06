from django.urls import path
from videojuegoApp import views

urlpatterns = [
    path('videojuegos/', views.listadoVideojuegos),
    path('agregarVideojuegos/', views.agregarVideojuego),
    path('actualizarVideojuegos/<int:id>', views.actualizarVideojuego),
    path('eliminarVideojuegos/<int:id>', views.eliminarVideojuego),
]