from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)  # Título del libro.
    genero = models.CharField(max_length=50)  # Género literario.
    num_paginas = models.IntegerField()  # Número de páginas del libro.

    def __str__(self):
        return self.titulo  # Representación legible del modelo.
