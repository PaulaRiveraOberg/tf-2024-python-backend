from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum, Q
from .models import Programa, Modulo, Curso, Estudiante
from django.views.decorators.csrf import csrf_exempt

def q_objects(request):
    estudiantes = Estudiante.objects.filter(
        Q(direccion='Calle Falsa 123') | Q(correo__icontains='example.com')
    )
    return JsonResponse(list(estudiantes.values()), safe=False)

def agregacion(request):
    total_horas = Programa.objects.aggregate(total_horas=Sum('cantidad_horas'))
    return JsonResponse(total_horas, safe=False)

def anotacion(request):
    programas = Programa.objects.annotate(num_modulos=Count('modulo'))
    return JsonResponse(list(programas.values()), safe=False)

def anotacion2(request):
    programas = Programa.objects.annotate(total_horas_modulos=Sum('modulo__cantidad_horas'))
    data = []
    for p in programas:
        data.append({"nombre_programa": p.nombre_programa, "total_horas_modulos": p.total_horas_modulos})

    return JsonResponse(data, safe=False)

def cursos_no_eficiente(request):
    data = []
    cursos = Curso.objects.all()
    for curso in cursos:
        data.append({'codigo_curso': curso.codigo_curso, 'nombre_programa': curso.id_programa.nombre_programa})
    return JsonResponse(data, safe=False)


def cursos(request):
    data = []
    cursos = Curso.objects.select_related('id_programa')
    for curso in cursos:
        data.append({'codigo_curso': curso.codigo_curso, 'nombre_programa': curso.id_programa.nombre_programa})
    return JsonResponse(data, safe=False)

def modulos_relatores(request):
    data = []
    modulos = Modulo.objects.prefetch_related('relatores')
    for modulo in modulos:
        relatores = modulo.relatores.all()
        for relator in relatores:
            data.append({'nombre_modulo': modulo.nombre_modulo, 'nombre_relator': relator.nombre_relator})
    return JsonResponse(data, safe=False)

def paginador(request):
    data = []
    estudiantes = Estudiante.objects.all()
    paginator = Paginator(estudiantes, 10)

    pagina1 = paginator.page(1)
    for estudiante in pagina1.object_list:
        data.append({'nombre_estudiante': estudiante.nombre_estudiante})
    return JsonResponse(data, safe=False)

def uso_only(request):
    data = []
    estudiantes = Estudiante.objects.only('nombre_estudiante')
    for estudiante in estudiantes:
        data.append({'nombre_estudiante': estudiante.nombre_estudiante})
    return JsonResponse(data, safe=False)

@transaction.atomic
@csrf_exempt
def inscribir_estudiante_ejemplo(request):
    if request.method == 'POST':
        id_curso = request.POST.get('id_curso')
        id_estudiante = request.POST.get('id_estudiante')
        curso = Curso.objects.get(id_curso=id_curso)
        if curso.cantidad_estudiantes <= 0:
            raise ValueError('No hay cupos disponibles')

        curso.cantidad_estudiantes -= 1
        curso.save()

        #Obtener el estudiante
        estudiante = Estudiante.objects.get(id_estudiante=id_estudiante)
        #Validar que el estudiante no se agregue más de una vez
        if estudiante in curso.estudiantes.all():
            raise ValueError('Estudiante ya inscrito en el curso')
        curso.estudiantes.add(estudiante)

        #Actualizar la cantidad de estudiantes disponibles
        curso.cantidad_estudiantes -= 1
        curso.save()
        return JsonResponse({'mensaje': 'Estudiante inscrito correctamente'}, safe=False)