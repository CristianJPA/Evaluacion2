from django.db import models
from consolaApp.models import Consola

# Create your models here.
class Videojuego(models.Model):
    nombreVideojuego = models.CharField(max_length=30)
    duracion = models.CharField(max_length=15)
    edicion = models.CharField(max_length=30)
    genero = models.CharField(max_length=20)
    precio = models.IntegerField()
    cantidadJugadores = models.CharField(max_length=4)
    nombreConsola   = models.ForeignKey(Consola, null=True, blank=True, on_delete=models.CASCADE)