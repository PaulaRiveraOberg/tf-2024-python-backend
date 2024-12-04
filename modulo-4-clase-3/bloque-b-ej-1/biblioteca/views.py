from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse
from .models import Libro

class LibroListView(View):
    def get(self, request):
        libros = Libro.objects.all()
        data = []
        for libro in libros:
            libro_data = {
                'titulo': libro.titulo,
                'genero': libro.genero.nombre if libro.genero else None,
                'autores': [autor.nombre for autor in libro.autores.all()]
            }
            data.append(libro_data)
            
        response = {
            'total': len(data),
            'libros': data
        }
        
        return JsonResponse(response)