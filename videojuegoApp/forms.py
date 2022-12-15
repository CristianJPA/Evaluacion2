from django import forms
from videojuegoApp.models import Videojuego
from consolaApp.models import Consola
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ValidationError


class FormVideojuego(forms.ModelForm):   
    print("---------------------------------")

    nombreVideojuego = forms.CharField(label="Nombre VideoJuego")
    duracion = forms.CharField()
    edicion = forms.CharField()
    genero = forms.CharField()
    precio = forms.IntegerField()
    cantidadJugadores = forms.CharField(label="Jugadores")

    nombreVideojuego.widget.attrs['class'] = 'form-control'
    duracion.widget.attrs['class'] = 'form-control'
    edicion.widget.attrs['class'] = 'form-control'
    genero.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    cantidadJugadores.widget.attrs['class'] = 'form-control'

    duracion.widget.attrs['placeholder'] = '00 Horas'
    precio.widget.attrs['placeholder'] = '50000'
    cantidadJugadores.widget.attrs['placeholder'] = '1-2'


    class Meta:
            model = Videojuego
            fields = '__all__' 