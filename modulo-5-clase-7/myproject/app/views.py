from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Modulo, Curso, Estudiante, CursoEstudiante
from django.db import transaction

# Lista de cursos con paginación
def cursos(request):
    cursos = Curso.objects.all()
    paginator = Paginator(cursos, 10)  # 10 cursos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cursos.html', {'page_obj': page_obj})

# Detalle de un curso
def detalle_curso(request, codigo_curso):
    curso = get_object_or_404(Curso, codigo_curso=codigo_curso)
    programa = curso.id_programa
    modulos = Modulo.objects.filter(id_programa=programa.id_programa)
    estudiantes = curso.estudiantes.all()
    return render(request, 'detalle_curso.html', {
        'curso': curso,
        'programa': programa,
        'modulos': modulos,
        'estudiantes': estudiantes
    })

# Inscripción de un estudiante a un curso
@transaction.atomic
def inscribir_estudiante(request, codigo_curso):
    curso = get_object_or_404(Curso, codigo_curso=codigo_curso)
    estudiantes_inscritos = curso.estudiantes.values_list('id_estudiante', flat=True)
    estudiantes_disponibles = Estudiante.objects.exclude(id_estudiante__in=estudiantes_inscritos)

    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
        CursoEstudiante.objects.create(id_estudiante=estudiante, id_curso=curso)
        return redirect('detalle_curso', codigo_curso=curso.codigo_curso)

    return render(request, 'inscribir_estudiante.html', {
        'curso': curso,
        'estudiantes_disponibles': estudiantes_disponibles
    })
