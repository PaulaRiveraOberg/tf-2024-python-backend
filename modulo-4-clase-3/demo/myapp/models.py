from django.db import models

ESTADOS = [
    ('ACTIVO', 'Activo'),
    ('INACTIVO', 'Inactivo'),
]

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ACTIVO')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True, blank=True)
    etiquetas = models.ManyToManyField('Etiqueta', related_name='productos')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
