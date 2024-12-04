from django.db import models

class Revista(models.Model):
    titulo = models.CharField(max_length=100)  # Título de la revista.
    tema = models.CharField(max_length=50)  # Tema principal de la revista.
    frecuencia_publicacion = models.CharField(
        max_length=20,
        choices=[("Diaria", "Diaria"), ("Semanal", "Semanal"), ("Mensual", "Mensual")]  # Valores posibles.
    )
    num_edicion = models.IntegerField()  # Número de edición.

    def __str__(self):
        return self.titulo  # Representación legible del modelo.
