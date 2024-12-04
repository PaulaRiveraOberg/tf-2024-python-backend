from django.db import models

ESTADOS = [
    (True, 'Disponible'),
    (False, 'Agotado')
]

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Definimos el modelo Producto que representa los datos a manejar en la API.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.BooleanField(choices=ESTADOS, default=True)
    stock = models.IntegerField()
    url = models.URLField(null=True)
    etiquetas = models.ManyToManyField('Etiqueta')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
