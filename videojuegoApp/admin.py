from django.contrib import admin
from videojuegoApp.models import Videojuego
from .forms import FormVideojuego

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ['nombreVideojuego','duracion','edicion','genero','precio','cantidadJugadores','nombreConsola']
    form = FormVideojuego
# Register your models here.

admin.site.register(Videojuego,VideojuegoAdmin)