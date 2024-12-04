from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReservaViewSet

router = DefaultRouter()
router.register(r'reservas', ReservaViewSet)  # Asocia el prefijo "reservas" al ViewSet.

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas por el router.
]
