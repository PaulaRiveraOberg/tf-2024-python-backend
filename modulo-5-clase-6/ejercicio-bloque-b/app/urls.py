from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('<str:codigo_curso>/', views.detalle_curso, name='detalle_curso'),
    path('<str:codigo_curso>/inscripcion/', views.inscribir_estudiante, name='inscribir_estudiante'),
]
