from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RevistaViewSet

router = DefaultRouter()
router.register(r'revistas', RevistaViewSet)  # Asocia el prefijo "revistas" al ViewSet.

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas por el router.
]
