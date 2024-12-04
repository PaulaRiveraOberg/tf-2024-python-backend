from django.db import models
from django.utils import timezone

class Reserva(models.Model):
    libro = models.CharField(max_length=100)  # Nombre del libro reservado.
    usuario = models.CharField(max_length=100)  # Nombre del usuario que realiza la reserva.
    fecha_reserva = models.DateField()  # Fecha de la reserva.

    def __str__(self):
        return f"{self.libro} reservado por {self.usuario} el {self.fecha_reserva}"
