from rest_framework import serializers
from .models import Sensores,Ambientes,Historico

class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        field = '__all__'

class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        field = '__all__'

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        field = '__all__'
