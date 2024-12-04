from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro  # Asociamos este serializador con el modelo Libro.
        fields = '__all__'  # Incluye todos los campos del modelo.
