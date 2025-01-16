from django.contrib import admin

# Register your models here.
from .models import Estudiante, Programa, Modulo, Relator, Curso, CursoEstudiante, ModuloRelator

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('rut_estudiante', 'nombre_estudiante', 'fecha_nacimiento', 'direccion', 'correo', 'telefono')
    search_fields = ('rut_estudiante', 'nombre_estudiante')

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre_programa', 'cantidad_horas')
    search_fields = ('nombre_programa',)

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nombre_modulo', 'cantidad_horas', 'id_programa')
    search_fields = ('nombre_modulo',)
    list_filter = ('id_programa',)

@admin.register(Relator)
class RelatorAdmin(admin.ModelAdmin):
    list_display = ('rut_relator', 'nombre_relator', 'titulo_relator', 'anios_experiencia')
    search_fields = ('rut_relator', 'nombre_relator')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo_curso', 'cantidad_estudiantes', 'fecha_inicio', 'fecha_termino', 'id_programa')
    search_fields = ('codigo_curso',)
    list_filter = ('id_programa',)

@admin.register(CursoEstudiante)
class CursoEstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_estudiante', 'id_curso')
    search_fields = ('id_estudiante', 'id_curso')

@admin.register(ModuloRelator)
class ModuloRelatorAdmin(admin.ModelAdmin):
    list_display = ('id_relator', 'id_modulo')
    search_fields = ('id_relator', 'id_modulo')

