from django.contrib import admin
from .models import Etiqueta, Categoria, Producto


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'estado', 'categoria')
    search_fields = ('nombre', 'categoria__nombre', 'etiquetas__nombre')
    list_filter = ('estado', 'categoria', 'etiquetas')
