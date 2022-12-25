from rest_framework import serializers
from evaApp.models import Trabajador
from consolaApp.models import Consola
from videojuegoApp.models import Videojuego

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = '__all__'

class ConsolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consola
        fields = '__all__'

class VideojuegosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = '__all__'


