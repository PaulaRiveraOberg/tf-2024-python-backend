from app.models import Programa, Modulo, Estudiante
from django.db.models import Count
from datetime import date

# 1. Obtener los programas que tengan más de 3 módulos asignados
programas = Programa.objects.annotate(num_modulos=Count('modulo')).filter(num_modulos__gt=3)
programa = programas[0]

for programa in programas:
    print(programa.nombre_programa, programa.num_modulos, programa.cantidad_horas)


# 2. Listar los módulos que tengan más de 60 horas y el programa al que pertenecen
modulos = Modulo.objects.filter(cantidad_horas__gt=60).select_related('id_programa')

for modulo in modulos:
    print(modulo.nombre_modulo, modulo.cantidad_horas, modulo.id_programa.nombre_programa)

# 3. Filtrar estudiantes que tengan más de 18 años y cuyo nombre contenga “Estu"
nacimiento_mayores_18 = date(date.today().year - 18, date.today().month, date.today().day)
estudiantes = Estudiante.objects.filter(
    fecha_nacimiento__lte=nacimiento_mayores_18,
    nombre_estudiante__icontains='Estu'
)
for estudiante in estudiantes:
    print(estudiante.nombre_estudiante, estudiante.fecha_nacimiento)
