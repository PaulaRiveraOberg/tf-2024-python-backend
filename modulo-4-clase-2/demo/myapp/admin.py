from django.contrib import admin
from .models import Curso

# admin.site.register(Curso)


class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "fecha_creacion")
    search_fields = ("nombre", "descripcion")
    list_filter = ("fecha_creacion",)


admin.site.register(Curso, CursoAdmin)
