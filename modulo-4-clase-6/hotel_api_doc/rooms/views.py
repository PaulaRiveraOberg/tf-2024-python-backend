from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Room, Reservation
from .serializers import RoomSerializer, ReservationSerializer

@extend_schema_view(
    list=extend_schema(description="Lista todas las habitaciones."),
    retrieve=extend_schema(description="Recupera una habitación específica."),
    create=extend_schema(description="Crea una nueva habitación."),
    update=extend_schema(description="Actualiza una habitación existente."),
    partial_update=extend_schema(description="Actualiza parcialmente una habitación."),
    destroy=extend_schema(description="Elimina una habitación."),
)
class RoomViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Room.
    Proporciona las acciones CRUD para las habitaciones.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        """
        Retorna las clases de permisos que se aplican a la acción actual.
        Si la acción es 'check_availability', se requiere autenticación.
        Para otras acciones, se requiere que el usuario sea administrador.
        """
        if self.action == 'check_availability':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    @action(detail=True, methods=['get'])
    @extend_schema(
        description="Verifica la disponibilidad de una habitación en un rango de fechas.",
        parameters=[
            {
                "name": "start_date",
                "in": "query",
                "required": True,
                "description": "Fecha de inicio para verificar disponibilidad.",
                "schema": {"type": "string", "format": "date"}
            },
            {
                "name": "end_date",
                "in": "query",
                "required": True,
                "description": "Fecha de fin para verificar disponibilidad.",
                "schema": {"type": "string", "format": "date"}
            }
        ],
        responses={200: "Indica si la habitación está disponible."}
    )
    def check_availability(self, request, pk=None):
        """
        Acción personalizada para verificar la disponibilidad de una habitación.
        Requiere los parámetros de consulta 'start_date' y 'end_date'.
        Retorna un diccionario indicando si la habitación está disponible.
        """
        room = self.get_object()
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        reservations = room.reservations.filter(start_date__gte=start_date, end_date__lte=end_date)
        available = not reservations.exists()
        return Response({'available': available})   

@extend_schema_view(
    list=extend_schema(description="Lista todas las reservas del usuario autenticado."),
    create=extend_schema(description="Crea una nueva reserva."),
    update=extend_schema(description="Actualiza una reserva existente."),
    partial_update=extend_schema(description="Actualiza parcialmente una reserva."),
)
class ReservationViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Reservation.
    Permite listar, crear y editar reservas.
    """
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    http_method_names = ['get', 'post', 'put']  

    def get_queryset(self):
        """
        Retorna el conjunto de reservas del usuario autenticado.
        """
        return Reservation.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario autenticado a la reserva al crearla.
        """
        serializer.save(user=self.request.user)
