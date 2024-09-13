from rest_framework import serializers

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    codigo_municipio = serializers.CharField()
    nombre_municipio = serializers.CharField()
    codigo_postal = serializers.CharField()
    tipo = serializers.CharField()
    limite_norte = serializers.CharField()
    limite_sur = serializers.CharField()
    limite_este = serializers.CharField()
    limite_oeste = serializers.CharField()