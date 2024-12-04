from rest_framework import viewsets  # Importamos viewsets para crear vistas basadas en clases con operaciones CRUD automáticas.
from rest_framework.decorators import action  # Para crear endpoints personalizados en un ViewSet.
from rest_framework.permissions import AllowAny  # Importamos permisos para manejar el acceso a las vistas.
from rest_framework.response import Response  # Para generar respuestas HTTP personalizadas.

from .models import Producto, Etiqueta, Categoria  # Importamos los modelos que representan las tablas en la base de datos.
from .serializers import ProductoSerializer, CategoriaSerializer, EtiquetaSerializer  # Importamos los serializadores para convertir datos del modelo en JSON y viceversa.


# ViewSet para manejar las operaciones CRUD del modelo Categoria.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()  # Obtiene todos los registros de la tabla Categoria.
    serializer_class = CategoriaSerializer  # Usa el serializador CategoriaSerializer para transformar los datos.


# ViewSet para manejar las operaciones CRUD del modelo Producto.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()  # Obtiene todos los registros de la tabla Producto.
    serializer_class = ProductoSerializer  # Usa el serializador ProductoSerializer para transformar los datos.
    permission_classes = [AllowAny]  # Permite el acceso sin autenticación a todas las operaciones de este ViewSet.

    # Endpoint personalizado para filtrar productos por stock mínimo.
    @action(detail=False, methods=['get'])  # Define un endpoint adicional de solo lectura.
    def filtrar_por_stock(self, request):
        # Recupera el parámetro "stock_minimo" de los query params; usa 1 como valor predeterminado si no se proporciona.
        stock_minimo = request.query_params.get('stock_minimo', 1)
        try:
            stock_minimo = int(stock_minimo)  # Convierte el valor a entero para realizar la comparación.
        except ValueError:
            return Response({"error": "El parámetro 'stock_minimo' debe ser un número entero."}, status=400)

        # Filtra los productos cuyo stock sea mayor o igual al valor proporcionado.
        productos = self.queryset.filter(stock__gte=stock_minimo)
        # Serializa los datos filtrados para enviarlos como respuesta en formato JSON.
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)  # Devuelve los datos serializados como respuesta HTTP.


# ViewSet para manejar las operaciones CRUD del modelo Etiqueta.
class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()  # Obtiene todos los registros de la tabla Etiqueta.
    serializer_class = EtiquetaSerializer  # Usa el serializador EtiquetaSerializer para transformar los datos.
