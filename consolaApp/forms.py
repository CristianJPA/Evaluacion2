from django import forms
from consolaApp.models import Consola
from django.contrib.admin import widgets
from django.core import validators 
from django.forms import ValidationError

class FormConsola(forms.ModelForm):
    class Meta:
            model = Consola
            fields = '__all__' # incluye todo lo que esta en el modelo

    nombreConsola = forms.CharField(label="Nombre de la consola")
    modelo = forms.CharField()
    color = forms.CharField()
    precio = forms.IntegerField()
    memoria = forms.CharField()
    edicion = forms.CharField()

    nombreConsola.widget.attrs['class']= 'form-control'
    modelo.widget.attrs['class']= 'form-control'
    color.widget.attrs['class']= 'form-control'
    precio.widget.attrs['class']= 'form-control'
    memoria.widget.attrs['class']= 'form-control'
    edicion.widget.attrs['class']= 'form-control'

