from django.contrib import admin
from evaApp.models import Trabajador
from .forms import FormTrabajador

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','apellido','telefono','correo','fechaNacimiento','nombreConsola']
    form = FormTrabajador
# Register your models here.


admin.site.register(Trabajador,TrabajadorAdmin)