from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()  # Obtiene todos los registros de la tabla Libro.
    serializer_class = LibroSerializer  # Usa el serializador LibroSerializer.
