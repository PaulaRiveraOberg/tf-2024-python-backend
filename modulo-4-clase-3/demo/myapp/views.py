from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Producto
from django.views.generic import ListView, DetailView


# Create your views here.
class MiVista(View):
        def get(self, request):
            return HttpResponse("Hola desde una CBV") #sin template
        

class ProductoView(View):
        def get(self, request):
            # Recuperar todos los productos
            productos = Producto.objects.values("id", "nombre", "precio")
            return JsonResponse(list(productos), safe=False) #sin template
        

class ProductoViewFiltered(View):
        def get(self, request):
            # Recuperar todos los productos
            min_precio = request.GET.get("min_precio", None)
            max_precio = request.GET.get("max_precio", None)

            query = Producto.objects.all()
            if min_precio:
                query = query.filter(precio__gte=min_precio)
            if max_precio:
                query = query.filter(precio__lte=max_precio)

            productos = query.values("id", "nombre", "precio")

            return JsonResponse(list(productos), safe=False) #sin template
        
class ProductoListView(ListView):
    model = Producto
    template_name = "lista.html"
    context_object_name = "productos"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "detalle.html"
    context_object_name = "producto"