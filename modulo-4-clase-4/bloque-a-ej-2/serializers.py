from rest_framework import serializers
from .models import Revista

class RevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revista  # Asociamos este serializador con el modelo Revista.
        fields = '__all__'  # Incluye todos los campos del modelo.
