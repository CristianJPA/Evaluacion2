from django.db import models
from consolaApp.models import Consola

# Create your models here.

class Trabajador(models.Model):
    rut             = models.CharField(max_length=10)
    nombre          = models.CharField(max_length=15)
    apellido        = models.CharField(max_length=15)
    telefono        = models.IntegerField()
    correo          = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    nombreConsola   = models.ForeignKey(Consola, null=True, blank=True, on_delete=models.CASCADE)