from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_inicio')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_inicio',)
