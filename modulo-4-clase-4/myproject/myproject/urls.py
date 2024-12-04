from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from myapp.views import ProductoViewSet, EtiquetaViewSet, CategoriaViewSet
from django.urls import path, include

# Crea un router que generará automáticamente las rutas para el ViewSet.
router = DefaultRouter()
router.register(r'productos', ProductoViewSet) # Asocia el prefijo "productos" al ViewSet.
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Incluye las rutas generadas por el router en las URLs del proyecto.
    path('api-token-auth/', obtain_auth_token), # Ruta para obtener un token de autenticación.
]

