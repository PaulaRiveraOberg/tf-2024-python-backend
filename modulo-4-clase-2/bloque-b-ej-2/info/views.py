from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenidos al sitio web del grupo")

def detalles(request, proyecto):
    context = {
        "nombre": "Proyecto Inicial",
        "descripcion": "Este es el proyecto inicial del grupo",
        "estado": "activo"
    }
    return render(request, "proyecto.html", context)
