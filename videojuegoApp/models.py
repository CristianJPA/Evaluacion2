from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombreVideojuego = models.CharField(max_length=30)
    duracion = models.CharField(max_length=15)
    edicion = models.CharField(max_length=30)
    genero = models.CharField(max_length=20)
    precio = models.IntegerField()
    cantidadJugadores = models.CharField(max_length=4)
    consolaCompatible = models.CharField(max_length=15, default=0)