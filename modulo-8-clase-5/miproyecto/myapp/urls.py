from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AutorViewSet,
    CarritoCompraViewSet,
    CategoriaViewSet,
    EditorialViewSet,
    ItemCarritoViewSet,
    ItemPedidoViewSet,
    LibroViewSet,
    PedidoViewSet,
    ResenaViewSet,
)

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"libros", LibroViewSet)
router.register(r"editoriales", EditorialViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"resenas", ResenaViewSet)
router.register(r"carritos", CarritoCompraViewSet)
router.register(r"items-carrito", ItemCarritoViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"items-pedido", ItemPedidoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
