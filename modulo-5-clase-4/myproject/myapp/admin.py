from django.contrib import admin

# Register your models here.
from .models import Estudiante, Programa, Modulo, Relator, Curso, EstudianteCurso, RelatorModulo

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
    list_display = ('nombre_modulo', 'cantidad_horas', 'programa')
    search_fields = ('nombre_modulo',)
    list_filter = ('programa',)

@admin.register(Relator)
class RelatorAdmin(admin.ModelAdmin):
    list_display = ('rut_relator', 'nombre_relator', 'titulo_relator', 'anios_experiencia')
    search_fields = ('rut_relator', 'nombre_relator')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo_curso', 'cantidad_estudiantes', 'fecha_inicio', 'fecha_termino', 'programa')
    search_fields = ('codigo_curso',)
    
    list_filter = ('programa',)

@admin.register(EstudianteCurso)
class EstudianteCursoAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso')
    search_fields = ('estudiante', 'curso')
    list_filter = ('curso',)

@admin.register(RelatorModulo)
class RelatorModuloAdmin(admin.ModelAdmin):
    list_display = ('relator', 'modulo')
    search_fields = ('relator', 'modulo')
    list_filter = ('modulo',)
