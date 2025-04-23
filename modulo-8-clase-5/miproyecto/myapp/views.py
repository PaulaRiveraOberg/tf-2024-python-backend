from django.shortcuts import render
from rest_framework import viewsets

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
from .serializers import (
    AutorSerializer,
    CarritoCompraSerializer,
    CategoriaSerializer,
    EditorialSerializer,
    ItemCarritoSerializer,
    ItemPedidoSerializer,
    LibroSerializer,
    PedidoSerializer,
    ResenaSerializer,
)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer


class CarritoCompraViewSet(viewsets.ModelViewSet):
    queryset = CarritoCompra.objects.all()
    serializer_class = CarritoCompraSerializer


class ItemCarritoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer


class ItemCarritoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
