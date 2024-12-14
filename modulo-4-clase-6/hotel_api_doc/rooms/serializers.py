from rest_framework import serializers

from .models import Room, Reservation

class RoomSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Room.
    Serializa todos los campos del modelo.
    """
    class Meta:
        model = Room
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Reservation.
    Serializa todos los campos del modelo, pero el campo 'user' es de solo lectura
    para que no pueda ser seteado manualmente durante la creación de una reserva.
    """
    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, attrs):
        """
        Valida que:
        - La fecha de inicio sea anterior a la fecha de fin.
        - La habitación esté disponible.
        - La habitación no tenga reservas en el rango de fechas especificado.
        """
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        if start_date >= end_date:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        
        room = attrs.get('room')
        if not room.is_available:
            raise serializers.ValidationError("La habitación no está disponible.")
        
        reservations = Reservation.objects.filter(room=room, start_date__lte=end_date, end_date__gte=start_date)
        if reservations.exists():
            raise serializers.ValidationError("La habitación ya tiene una reserva en ese rango de fechas.")

        return attrs
