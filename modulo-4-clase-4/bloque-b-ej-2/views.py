from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()  # Obtiene todas las reservas registradas.
    serializer_class = ReservaSerializer  # Usa el serializador ReservaSerializer.

    # Endpoint adicional para listar reservas activas.
    @action(detail=False, methods=['get'])
    def activas(self, request):
        # Filtra reservas con fecha mayor o igual a la fecha actual.
        reservas_activas = self.queryset.filter(fecha_reserva__gte=timezone.now().date())
        serializer = self.get_serializer(reservas_activas, many=True)
        return Response(serializer.data)
