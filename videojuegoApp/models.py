from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombreVideojuego = models.CharField(max_length=30)
    duracion = models.IntegerField()
    edicion = models.CharField(max_length=30)
    genero = models.CharField(max_length=20)
    precio = models.IntegerField()
    cantidadJugadores = models.IntegerField()
    idConsola = models.IntegerField()