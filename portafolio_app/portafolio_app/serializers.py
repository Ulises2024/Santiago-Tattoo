from rest_framework import serializers
from .models import cita, cliente, emails

class EmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = emails
        fields = ['mail']

class ClienteSerializer(serializers.ModelSerializer):
    emails = EmailsSerializer()

    class Meta:
        model = cliente
        fields = ['persona', 'direccion', 'emails', 'telefono']

class CitaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()

    class Meta:
        model = cita
        fields = ['eventTitle', 'eventStartDate', 'eventEndDate', 'eventStartTime', 'eventEndTime', 'descripcion', 'tatuador', 'cliente', 'estudio']
