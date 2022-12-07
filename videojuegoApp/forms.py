from django import forms
from videojuegoApp.models import Videojuego
from consolaApp.models import Consola
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ValidationError


class FormVideojuego(forms.ModelForm):

    consolas = Consola.objects.values('nombreConsola')
    test = {consolas}
    games = []
    i = 0
    for consola1 in test:
        for campo in consola1:
            hola = consola1[i]['nombreConsola']
            print(hola)
            listado = (hola,hola)
            print(f'listado- {listado}')
            games.append(listado)                
            print("separar")
            print(f'listadooo - {games}')
            i+=1     
    print("---------------------------------")

    nombreVideojuego = forms.CharField(label="Nombre VideoJuego")
    duracion = forms.CharField()
    edicion = forms.CharField()
    genero = forms.CharField()
    precio = forms.IntegerField()
    cantidadJugadores = forms.CharField(label="Jugadores")
    consolaCompatible = forms.CharField(widget=forms.Select(choices=games), label="Compatibilidad")

    nombreVideojuego.widget.attrs['class'] = 'form-control'
    duracion.widget.attrs['class'] = 'form-control'
    edicion.widget.attrs['class'] = 'form-control'
    genero.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    cantidadJugadores.widget.attrs['class'] = 'form-control'
    consolaCompatible.widget.attrs['class'] = 'form-select'

    duracion.widget.attrs['placeholder'] = '00 Horas'
    precio.widget.attrs['placeholder'] = '50000'
    cantidadJugadores.widget.attrs['placeholder'] = '1-2'


    class Meta:
            model = Videojuego
            fields = '__all__' 