from django.shortcuts import render
from django.http import JsonResponse
from evaApp.models import Trabajador
from consolaApp.models import Consola
from videojuegoApp.models import Videojuego
from .serializers import TrabajadorSerializer, ConsolaSerializer, VideojuegosSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
# Views Trabajador
@api_view(['GET','POST'])
def listadoTrabajadores(request):
    if request.method == 'GET':
        trabajadores = Trabajador.objects.all()
        serializer = TrabajadorSerializer(trabajadores, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TrabajadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PUT','DELETE'])
def detalles_Trabajadores(request, id):
    try:
        trabajador = Trabajador.objects.get(id=id)
    except Trabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TrabajadorSerializer(trabajador)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TrabajadorSerializer(trabajador, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        trabajador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views Consola
@api_view(['GET','POST'])
def listadoConsolas(request):
    if request.method == 'GET':
        consola = Consola.objects.all()
        serializer = ConsolaSerializer(consola, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ConsolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalles_Consolas(request, id):
    try:
        consola = Consola.objects.get(id=id)
    except Consola.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ConsolaSerializer(consola)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ConsolaSerializer(consola, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        consola.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views videojuegos
@api_view(['GET','POST'])
def listadoVideojuegos(request):
    if request.method == 'GET':
        videojuego = Videojuego.objects.all()
        serializer = VideojuegosSerializer(videojuego, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = VideojuegosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalles_Videojuego(request, id):
    try:
        videojuego = Videojuego.objects.get(id=id)
    except Videojuego.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VideojuegosSerializer(videojuego)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = VideojuegosSerializer(videojuego, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        videojuego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)