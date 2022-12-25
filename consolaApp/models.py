from django.db import models

# Create your models here.
class Consola(models.Model):
    nombreConsola = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    color = models.CharField(max_length=10)
    precio = models.IntegerField()
    memoria = models.CharField(max_length=5)
    edicion = models.CharField(max_length=15)

    def __str__(self):
        return self.nombreConsola

