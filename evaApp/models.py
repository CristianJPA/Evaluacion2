from django.db import models

# Create your models here.

class Trabajador(models.Model):
    rut             = models.CharField(max_length=10)
    nombre          = models.CharField(max_length=15)
    apellido        = models.CharField(max_length=15)
    telefono        = models.IntegerField()
    correo          = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    compraConsola   = models.CharField(max_length=15)