from django.urls import path
from . import views

urlpatterns = [
    path('anotacion/', views.anotacion, name='anotacion'),
    path('anotacion2/', views.anotacion2, name='anotacion2'),
    path('cursos_no_eficiente/', views.cursos_no_eficiente, name='cursos_no_eficiente'),
    path('cursos/', views.cursos, name='cursos'),
    path('modulos_relatores/', views.modulos_relatores, name='modulos_relatores'),
    path('paginador/', views.paginador, name='paginador'),
    path('q_objects/', views.q_objects, name='q_objects'),
    path('agregacion/', views.agregacion, name='agregacion'),
    path('uso_only/', views.uso_only, name='uso_only'),
    path('inscribir_estudiante_ejemplo/', views.inscribir_estudiante_ejemplo, name='inscribir_estudiante_ejemplo'),
]