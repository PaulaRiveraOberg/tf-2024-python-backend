from rest_framework import serializers

from .models import (
    Autor,
    CarritoCompra,
    Categoria,
    Editorial,
    ItemCarrito,
    ItemPedido,
    Libro,
    Pedido,
    Resena,
)


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
        read_only_fields = ["id"]


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = "__all__"
        read_only_fields = ["id"]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        read_only_fields = ["id"]


class LibroSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True, read_only=True)
    editorial = EditorialSerializer(read_only=True)
    categorias = CategoriaSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = "__all__"
        read_only_fields = ["id"]


class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = "__all__"
        read_only_fields = ["id", "fecha_creacion"]


class CarritoCompraSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = CarritoCompra
        fields = "__all__"
        read_only_fields = ["id", "fecha_creacion"]


class ItemCarritoSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()
    libro = LibroSerializer(read_only=True)

    class Meta:
        model = ItemCarrito
        fields = "__all__"
        read_only_fields = ["id", "fecha_agregado"]


class ItemPedidoSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()
    libro = LibroSerializer(read_only=True)

    class Meta:
        model = ItemPedido
        fields = "__all__"
        read_only_fields = ["id"]


class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = "__all__"
        read_only_fields = ["id", "fecha_creacion"]


class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = "__all__"
        read_only_fields = ["id", "fecha_creacion"]
