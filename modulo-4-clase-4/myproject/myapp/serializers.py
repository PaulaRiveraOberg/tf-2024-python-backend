from rest_framework import serializers
from .models import Producto, Etiqueta, Categoria


# Serializador para manejar los datos del modelo Categoria.
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria  # Asociamos este serializador con el modelo Categoria.
        fields = '__all__'  # Incluye todos los campos del modelo en la salida.


# Serializador para manejar los datos del modelo Etiqueta.
class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta  # Asociamos este serializador con el modelo Etiqueta.
        fields = '__all__'  # Incluye todos los campos del modelo en la salida.


# Serializador para manejar los datos del modelo Producto.
class ProductoSerializer(serializers.ModelSerializer):
    # Los siguientes campos están comentados porque se pueden configurar según sea necesario:
    # - Mostrar datos relacionados como cadenas legibles.
    # - Incluir datos relacionados de otros serializadores.
    # categoria = serializers.StringRelatedField()  # Muestra la categoría como un string (relación ForeignKey).
    # categoria = CategoriaSerializer()  # Incluye todos los datos de la categoría mediante un serializador.
    # etiquetas = serializers.StringRelatedField(many=True)  # Muestra las etiquetas como strings (relación ManyToMany).
    # etiquetas = EtiquetaSerializer(many=True)  # Incluye todos los datos de las etiquetas relacionadas.

    class Meta:
        model = Producto  # Asociamos este serializador con el modelo Producto.
        fields = '__all__'  # Incluye todos los campos del modelo en la salida.

    # Validación personalizada para el precio: debe ser mayor a 0.
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value

    # Validación personalizada para el stock: no puede ser negativo.
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value
