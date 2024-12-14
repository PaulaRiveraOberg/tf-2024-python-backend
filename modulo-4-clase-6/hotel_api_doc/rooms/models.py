from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    """
    Modelo que representa una habitación en el hotel.
    """

    name = models.CharField(
        max_length=255,
        help_text="Nombre de la habitación."
    )
    description = models.TextField(
        help_text="Descripción detallada de la habitación."
    )
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio por noche de la habitación."
    )
    is_available = models.BooleanField(
        default=True,
        help_text="Indica si la habitación está disponible para reservas."
    )

    def __str__(self):
        """
        Retorna una representación en cadena del objeto Room, que es su nombre.
        """
        return self.name

class Reservation(models.Model):
    """
    Modelo que representa una reserva de habitación.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Usuario que realiza la reserva."
    )
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE,
        related_name='reservations',
        help_text="Habitación reservada."
    )
    start_date = models.DateField(
        help_text="Fecha de inicio de la reserva."
    )
    end_date = models.DateField(
        help_text="Fecha de fin de la reserva."
    )

    def clean(self):
        """
        Realiza validaciones antes de guardar una reserva:
        - Verifica que la fecha de inicio sea anterior a la fecha de fin.
        - Verifica que no haya superposición de fechas con otras reservas para la misma habitación.
        """
        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise models.ValidationError('La fecha de inicio debe ser anterior a la fecha de fin')

            # Verificar superposición de fechas
            overlapping = Reservation.objects.filter(
                room=self.room,
                start_date__lte=self.end_date,
                end_date__gte=self.start_date
            )
            if self.pk:
                overlapping = overlapping.exclude(pk=self.pk)
            if overlapping.exists():
                raise models.ValidationError('Ya existe una reserva para estas fechas')

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para incluir la validación antes de guardar.
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Retorna una representación en cadena del objeto Reservation, que incluye el nombre de usuario y el nombre de la habitación.
        """
        return f"{self.user.username} - {self.room.name}"
