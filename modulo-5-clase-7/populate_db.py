import random
from datetime import datetime, timedelta

from django.db import transaction
from django.utils.timezone import make_aware
from app.models import Curso, Estudiante, Relator, Modulo, Programa #ojo con el nombre de la aplicacion debe adaptarse

# Crear programas
programas = []
for i in range(100):
    programa = Programa.objects.create(
        nombre_programa=f"Programa {i + 1}",
        cantidad_horas=random.randint(20, 100),
    )
    programas.append(programa)

# Crear estudiantes
estudiantes = []
for i in range(1000):
    estudiante = Estudiante(
        rut_estudiante=f"{random.randint(1000000, 99999999)}-{random.choice('K123456789')}",
        nombre_estudiante=f"Estudiante {i + 1}",
        fecha_nacimiento=datetime(2000, 1, 1) + timedelta(days=random.randint(0, 8000)),
        direccion=f"Direccion {i + 1}",
        correo=f"estudiante{i + 1}@correo.com",
        telefono=f"+569{random.randint(10000000, 99999999)}",
    )
    estudiantes.append(estudiante)

# Insertar estudiantes en lotes
Estudiante.objects.bulk_create(estudiantes, batch_size=100)

# Crear relatores
relatores = []
for i in range(250):
    relator = Relator(
        rut_relator=f"{random.randint(1000000, 99999999)}-{random.choice('K123456789')}",
        nombre_relator=f"Relator {i + 1}",
        titulo_relator=f"Titulo {i + 1}",
        anios_experiencia=random.randint(1, 20),
        valor_hora=random.randint(10000, 50000),
    )
    relatores.append(relator)

# Insertar relatores en lotes
Relator.objects.bulk_create(relatores, batch_size=100)

# Crear módulos
modulos = []
for i in range(500):
    modulo = Modulo(
        nombre_modulo=f"Modulo {i + 1}",
        cantidad_horas=random.randint(5, 50),
        id_programa=random.choice(programas),
    )
    modulos.append(modulo)

# Insertar módulos en lotes
Modulo.objects.bulk_create(modulos, batch_size=100)

# Asociar relatores a módulos
for modulo in Modulo.objects.all():
    relatores_sample = random.sample(list(Relator.objects.all()), random.randint(1, 5))
    modulo.relatores.add(*relatores_sample)

# Crear cursos
cursos = []
for i in range(500):
    curso = Curso(
        codigo_curso=f"CUR-{i + 1:04}",
        cantidad_estudiantes=random.randint(10, 50),
        fecha_inicio=make_aware(datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365))),
        fecha_termino=make_aware(datetime(2025, 1, 1) + timedelta(days=random.randint(366, 730))),
        id_programa=random.choice(programas),
    )
    cursos.append(curso)

Curso.objects.bulk_create(cursos, batch_size=100)

with transaction.atomic():
    for curso in Curso.objects.all():
        estudiantes_sample = random.sample(list(Estudiante.objects.all()), random.randint(5, 30))
        for estudiante in estudiantes_sample:
            if not curso.estudiantes.filter(pk=estudiante.pk).exists():
                curso.estudiantes.add(estudiante)

