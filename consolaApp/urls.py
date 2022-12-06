from django.urls import path
from consolaApp import views


urlpatterns = [
    path('consolas/', views.listadoConsolas),
    path('agregarConsola/', views.agregarConsola),
    path('actualizarConsola/<int:id>', views.actualizarConsola),
    path('eliminarConsola/<int:id>', views.eliminarConsola),
]
