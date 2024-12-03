from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Curso


# Create your views here.
def home(request):
    return HttpResponse("Hola mundo!")


def saludo(request, name=None):
    if name is None:
        return HttpResponseBadRequest("El nombre es requerido")
    return HttpResponse(f"Hola {name.capitalize()}!")


def home_template(request):
    return render(request, "home.html")


def saludo_v2(request, nombre, apellido):
    context = {"nombre": nombre.capitalize(), "apellido": apellido.upper()}
    return render(request, "saludo_v2.html", context)


def cursos(request):
    # cursos = ["Python", "Django", "JavaScript", "React", "Vue", "Angular", "Node", "Express", "Flask", "Django Rest Framework"]
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})
