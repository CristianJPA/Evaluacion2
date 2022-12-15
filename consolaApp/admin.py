from django.contrib import admin
from consolaApp.models import Consola
from .forms import FormConsola

class ConsolaAdmin(admin.ModelAdmin):
    list_display = ['nombreConsola','modelo','color','precio','memoria','edicion']
    form = FormConsola

admin.site.register(Consola,ConsolaAdmin)
# Register your models here.
