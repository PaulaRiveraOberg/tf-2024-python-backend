from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenidos al sitio web del grupo")

def detalles(request, proyecto):
    # capitaliza cada palabra del texto en el slug original
    titulo = " ".join(map(lambda x: x.capitalize(), proyecto.split("-")))
    return HttpResponse(f"Detalles del proyecto: {titulo}")
