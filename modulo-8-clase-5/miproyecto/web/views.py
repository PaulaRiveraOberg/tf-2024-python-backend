from django.shortcuts import render
from myapp.models import Autor, Categoria, Editorial, Libro

# Create your views here.


def home(request):
    libros = Libro.objects.all()
    return render(request, "web/home.html", {"libros": libros})
