from rest_framework import viewsets
from .models import Revista
from .serializers import RevistaSerializer

class RevistaViewSet(viewsets.ModelViewSet):
    queryset = Revista.objects.all()  # Obtiene todos los registros de la tabla Revista.
    serializer_class = RevistaSerializer  # Usa el serializador RevistaSerializer.
