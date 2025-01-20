from django.shortcuts import render
from django.db import transaction
from myapp.models import Curso, Modulo, RelatorModulo, Programa, Relator
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@transaction.atomic
@csrf_exempt
def crear_curso(request):
    if request.method == 'POST':
        # Obtener datos del request JSON
        data = json.loads(request.body)

        # busca el programa
        try:
            programa = Programa.objects.get(pk=data.get('programa_id'))
        except Programa.DoesNotExist:
            return JsonResponse({'error': 'El programa no existe'}, status=404)
        
        
        try:
            primer_modulo = Modulo.objects.filter(programa=programa).first()
        except Modulo.DoesNotExist:
            return JsonResponse({'error': 'El programa no tiene módulos asociados'}, status=404)
        
        
        # busca el relator
        try:
            relator = Relator.objects.get(pk=data.get('relator_id'))
        except Relator.DoesNotExist:
            return JsonResponse({'error': 'El relator no existe'}, status=404)
        
        # Crear el nuevo curso
        curso = Curso.objects.create(
            codigo_curso=data['codigo_curso'],
            cantidad_estudiantes=data['cantidad_estudiantes'], 
            fecha_inicio=data['fecha_inicio'],
            fecha_termino=data['fecha_termino'],
            programa=programa
        )

        # Crear la relación entre el relator y el módulo
        RelatorModulo.objects.create(
            relator=relator,
            modulo=primer_modulo
        )

        return JsonResponse({'message': 'Curso creado exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
