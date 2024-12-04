from rest_framework import serializers
from .models import Reserva
from django.utils import timezone

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva  # Asociamos este serializador con el modelo Reserva.
        fields = '__all__'  # Incluye todos los campos del modelo.

    # Validación personalizada para `fecha_reserva`.
    def validate_fecha_reserva(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("La fecha de reserva no puede estar en el pasado.")
        return value
