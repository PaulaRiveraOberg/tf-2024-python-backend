## Clase 4: Repaso ORM en Django

### ORM Básico y Consultas Relacionadas

Crearemos un proyecto nuevo y una nueva aplicación.

```bash
django-admin startproject myproject
cd myproject
django-admin startapp app
```

Crearemos los modelos de la BD con la que hemos trabajado en las clases anteriores en [myproject/app/models.py](myproject/app/models.py).

Vamos a cambiar el motor de base de datos de nuestro proyecto a PostgreSQL. Para esto, debemos modificar el archivo `settings.py` y agregar la configuración de PostgreSQL.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'm5clase6',
        'USER': 'roberto',
        'PASSWORD': 'roberto',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Además debemos asegurarnos de instalar las dependencias necesarias para PostgreSQL, en nuestro ambiente virtual.

```bash
# activar el ambiente virtual
source venv/bin/activate
# en windows
venv\Scripts\activate
# instalar psycopg2
pip install psycopg2
```

Si recibimos el error al correr las migraciones:
```
django.db.utils.DataError: invalid value for parameter "TimeZone": "UTC"
```

Debemos modificar el archivo `settings.py` y cambiar el valor de `TIME_ZONE` a `America/Santiago` y `USE_TZ` a `False`.

```python
TIME_ZONE = "America/Santiago"
USE_TZ = False
```

### Correr migraciones

```bash
# crear migraciones
python manage.py makemigrations
# correr migraciones
python manage.py migrate
```

### Consulta de datos

Django nos permite hacer consultas a la base de datos de manera sencilla y orientada a objetos. Para esto, podemos usar el ORM de Django. Podemos hacer estas consultas desde el shell de Django.

```bash
python manage.py shell
```

Creación de un registro:

```python
from app.models import Programa

programa = Programa(
    nombre_programa="Ciencias de Datos", 
    cantidad_horas=120
)
programa.save()
print(f"Programa creado: {programa.nombre_programa}, Horas: {programa.cantidad_horas}")

```

### Operaciones y operadorescomunes
* Operaciones
    * Filtrar consultas `filter`
    * Excluir consultas `exclude`
    * Obtener un registro `get`
    * Obtener todos los registros `all`
* Operadores
    * Mayor que `>` `__gte`
    * Menor que `<` `__lt`
    * Contiene `__contains`
    * Match exacto `__exact`

Todos operadores de comparación están disponibles en [documentación operadores](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#field-lookups)

```python
# Obtener los estudiantes de un curso, nacidos en el año 2000
estudiantes = Estudiante.objects.filter(fecha_nacimiento__year=2000)
print(estudiantes)

# Excluir los estudiantes de un curso, nacidos antes del año 2000
estudiantes = Estudiante.objects.exclude(fecha_nacimiento__year__lt=2000)
print(estudiantes)

# Obtener un estudiante con nombre de estudiante que contenga la letra 'a'
estudiante = Estudiante.objects.get(nombre_estudiante__contains='a')
print(estudiante)

# Obtener todos los estudiantes sin un curso
estudiantes = Estudiante.objects.filter(curso__isnull=True)
print(estudiantes)
```

### Relaciones y consultas relacionadas

Podemos hacer consultas relacionadas usando los atributos de las relaciones.

```python
# Obtener los estudiantes de un curso
curso = Curso.objects.get(codigo_curso="INF-2024-01")
estudiantes = curso.estudiantes.all()
print(estudiantes)
```

Podemos optimizar las consultas relacionadas usando el metodo `select_related`.

```python
modulos = Modulo.objects.select_related('id_programa').all()
print(modulos)
# al acceder a los atributos de la relación no es necesario hacer una consulta adicional a la base de datos
print(modulos[0].id_programa.nombre_programa)
```

Para la optimización de consultas relacionadas a relaciones `ManyToMany` se puede usar el metodo `prefetch_related`.

```python
estudiantes = Estudiante.objects.prefetch_related('curso').all()
print(estudiantes)
```

## Q objects

Los Q objects son objetos que nos permiten hacer consultas complejas usando operadores lógicos.

```python
from django.db.models import Q

# Obtener los cursos que comiencen en 2023 o tengan más de 20 estudiantes
cursos_a = Curso.objects.filter(fecha_inicio__year=2023)
cursos_b = Curso.objects.filter(cantidad_estudiantes__gt=20)
cursos = cursos_a | cursos_b
for curso in cursos:
    print(curso.codigo_curso)
```

### Only, defer

```python
# only: solo trae los campos que se especifican
cursos = Curso.objects.only('codigo_curso', 'fecha_inicio')
for curso in cursos:
    print(curso.codigo_curso, curso.fecha_inicio)
# defer: no trae los campos que se especifican
cursos = Curso.objects.defer('cantidad_estudiantes', 'fecha_termino')
for curso in cursos:
    print(curso.codigo_curso)
```

### Paginación

```python
from django.core.paginator import Paginator

cursos = Curso.objects.all()
paginator = Paginator(cursos, 10)
page = paginator.page(1)
print(page)
```

## Ejercicio A: Consultas avanzadas usando Django ORM

Genere un informe sobre los programas, módulos y relatores. Guíese según las siguientes tareas:

1. Ejecutar el script entregado (populate_db.py) para generar datos e insertarlos en la base de datos. Recuerde que antes de ejecutarlo, deberá haber ejecutado las migraciones respectivas (makemigrations y migrate). 
    a) Copiar el archivo .py en el directorio de manage.py
    b) Ejecutar en el terminal: python manage.py shell < populate_db.py
2. Obtener los programas que tengan más de 3 módulos asignados. 
3. Listar los módulos que tengan más de 60 horas y el programa al que pertenecen.
4. Filtrar estudiantes que tengan más de 18 años y cuyo nombre contenga `"Estu"`. 

## Solución

* [solución](ejercicio-bloque-a.py)

## Ejercicio B: Manejo de transacciones con try-except, commit y rollback.

1. Implemente una vista y su template para mostrar el listado de cursos en la url `/cursos` a partir de la app base. Utilice paginación para mostrar solo 10 cursos por página.
2. Cree una página con el detalle del curso, este debe mostrar de manera en la url `/cursos/codigo_curso` todos los detalles asociados a un curso, el listado de alumnos y un enlace para agregar alumnos al curso
3. Cree una página `/cursos/codigo_curso/inscripcion` con un formulario que permita agregar alumnos a un curso, la vista asociada debe realizar la operación mediante una transacción y redirigir a la página de detalle en caso de exito.

## Solución

* [solución](ejercicio-bloque-b/README.md)

