from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Room, Reservation
from .serializers import RoomSerializer, ReservationSerializer


# --- Vista de habitaciones (sin autenticación) ---
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]  # Acceso público

# --- Vista protegida con Basic Auth ---
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# --- Vista protegida con Token Auth ---
class TokenProtectedViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# --- Vista protegida con JWT ---
class JWTProtectedViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]