from rest_framework import serializers

from .models import Room, Reservation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        # necesario para que el usuario no pueda setear el usuario en la creación de una reserva
        # este se setea automáticamente en el viewset
        read_only_fields = ['user']

    def validate(self, attrs):
        # valida que la fecha de inicio sea anterior a la fecha de fin
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        if start_date >= end_date:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        
        # valida que la habitación esté disponible
        room = attrs.get('room')
        if not room.is_available:
            raise serializers.ValidationError("La habitación no está disponible.")
        
        # valida que la habitación no tenga reservas en el rango de fechas
        reservations = Reservation.objects.filter(room=room, start_date__lte=end_date, end_date__gte=start_date)
        if reservations.exists():
            raise serializers.ValidationError("La habitación ya tiene una reserva en ese rango de fechas.")

        return attrs


