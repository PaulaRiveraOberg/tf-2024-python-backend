from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LibroViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)  # Asocia el prefijo "libros" al ViewSet.

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas por el router.
]
