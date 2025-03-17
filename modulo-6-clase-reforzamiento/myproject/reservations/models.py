from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=50)  # Ej: "Single", "Double", "Suite"
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.number} - {self.type}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.user.username} reserved {self.room.number} from {self.check_in} to {self.check_out}"
