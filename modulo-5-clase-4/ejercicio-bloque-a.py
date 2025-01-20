from app.models import Programa, Modulo, Relator, Curso
from django.db.models import Count, Sum
from django.db.models import Q

# 1. Lista de programas y total de horas de sus módulos:
# Crear una consulta que anote el número de módulos
# y el total de horas de los módulos asociados a cada programa.
# Mostrar el nombre del programa, el número de módulos y las horas totales.
programas = Programa.objects.filter(modulo__isnull=False).annotate(
    num_modulos=Count('modulo'), 
    total_horas=Sum('modulo__cantidad_horas')
)

for programa in programas:
    print(programa.nombre_programa, programa.num_modulos, programa.total_horas)


# 2. Relatores con más de 5 años de experiencia asignados a módulos:
# Crear una consulta que liste los relatores que tienen más de 5 años de experiencia,
# junto con los nombres de los módulos en los que enseñan.
# Optimizar la consulta usando prefetch_related.
relatores = Relator.objects.filter(
    anios_experiencia__gt=5, 
    modulo__isnull=False
    ).prefetch_related('modulo_set')

for relator in relatores:
    for modulo in relator.modulo_set.all():
        print(relator.nombre_relator, modulo.nombre_modulo)

# 3. Filtrar módulos en base a horas con Q objects: 
# Crear una consulta que devuelva módulos que cumplan al menos una de las siguientes condiciones:
# Tienen más de 100 horas.
# Pertenecen al programa "Ingeniería en Informática".
modulos = Modulo.objects.filter(
    Q(cantidad_horas__gt=100) | Q(id_programa__nombre_programa='Ingeniería en Informática')
)
for modulo in modulos:
    print(modulo.nombre_modulo, modulo.cantidad_horas, modulo.id_programa.nombre_programa)

# 4. Cursos con programas optimizados con select_related: 
# Crear una consulta que devuelva los cursos y sus programas asociados, 
# optimizando el acceso a la relación con select_related.
cursos = Curso.objects.select_related('id_programa').all()
for curso in cursos:
    print(curso.codigo_curso, curso.id_programa.nombre_programa)

# 5. Crear una consulta que anote el número de relatores por programa, 
# incluyendo solo aquellos relatores con más de 5 años de experiencia.
relatores_programa = Programa.objects.annotate(
    num_relatores=Count(
        'modulo__relatores', 
        filter=Q(modulo__relatores__anios_experiencia__gt=5),
        distinct=True
    )
)
for programa in relatores_programa:
    print(programa.nombre_programa, programa.num_relatores)
print(relatores_programa.query)

# 6. Mostrar el total de módulos de cada programa y actualizar 
# su nombre para agregar el número de módulos al final 
# (por ejemplo: "Ingeniería en Informática (3 módulos)")
programas = Programa.objects.annotate(
    num_modulos=Count('modulo')
)
for programa in programas:
    print(f"{programa.nombre_programa} ({programa.num_modulos} módulos)")
