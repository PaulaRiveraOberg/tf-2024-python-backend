## Clase 4: ORM avanzado en Django

### Repaso Django ORM

El ORM de Django es una herramienta que permite interactuar con la base de datos de manera sencilla y orientada a objetos. Para eso crearemos un proyecto nuevo y una nueva aplicación.

```bash
django-admin startproject myproject
cd myproject
django-admin startapp myapp
```

Crearemos los modelos de la BD con la que hemos trabajado en las clases anteriores en [myproject/myapp/models.py](myproject/myapp/models.py).

Vamos a cambiar el motor de base de datos de nuestro proyecto a PostgreSQL. Para esto, debemos modificar el archivo `settings.py` y agregar la configuración de PostgreSQL.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'talentofuturo',
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

### Carga de datos

Para cargar los datos de la BD, podemos usar el siguiente comando:

```bash
python manage.py loaddata data.json
```

### Consulta de datos

Django nos permite hacer consultas a la base de datos de manera sencilla y orientada a objetos. Para esto, podemos usar el ORM de Django. Podemos hacer estas consultas desde el shell de Django.

```bash
python manage.py shell
```

```python
from myapp.models import Estudiante, Programa, Modulo, Relator, Curso, EstudianteCurso, RelatorModulo

# Consulta de todos los estudiantes
estudiantes = Estudiante.objects.all()
print(estudiantes)

# Consulta de todos los programas
programas = Programa.objects.all()
print(programas)

# Obtener los cursos de un estudiante
estudiante = Estudiante.objects.get(rut_estudiante="12345678-9")
cursos = estudiante.cursos.all()
print(cursos)

# Obtener los estudiantes de un curso
curso = Curso.objects.get(codigo_curso="INF-2024-01")
estudiantes = curso.estudiante_set.all()
print(estudiantes)
```

### Filtrar consultas

Podemos filtrar las consultas usando los operadores de comparación. [Documentación](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#field-lookups)

```python
# Obtener los estudiantes de un curso, nacidos en el año 2000
estudiantes = Estudiante.objects.filter(fecha_nacimiento__year=2000)
print(estudiantes)

# Obtener los estudiantes de un curso, nacidos antes del año 2000
estudiantes = Estudiante.objects.filter(fecha_nacimiento__year__lt=2000)
print(estudiantes)

# Obtener los estudiantes de un curso, con nombre de estudiante que contenga la letra 'a'
estudiantes = Estudiante.objects.filter(nombre_estudiante__contains='a')
print(estudiantes)

# Obtener los estudiantes sin un curso
estudiantes = Estudiante.objects.filter(cursos__isnull=True)
print(estudiantes)

# Estudiantes en el curso de INF-2024-01
estudiantes = Estudiante.objects.filter(cursos__codigo_curso="INF-2024-01")
print(estudiantes)
```

También podemos usar el metodo `exclude` para obtener los estudiantes que no están en el curso de INF-2024-01.

```python
estudiantes = Estudiante.objects.exclude(cursos__codigo_curso="INF-2024-01")
print(estudiantes)
```

### Ordenar consultas

Podemos ordenar las consultas usando el metodo `order_by`.

```python
# Ordenar los estudiantes por rut
estudiantes = Estudiante.objects.order_by('rut_estudiante')
print(estudiantes)

# Ordenar los estudiantes por rut, en orden descendente
estudiantes = Estudiante.objects.order_by('-rut_estudiante')
print(estudiantes)
```

### Revisar el SQL generado por un QuerySet

Podemos revisar el SQL generado por un QuerySet usando el metodo `query`.

```python
estudiantes = Estudiante.objects.all()
print(estudiantes.query)

estudiantes = Estudiante.objects.filter(cursos__codigo_curso="INF-2024-01")
print(estudiantes.query)

estudiantes = Estudiante.objects.exclude(cursos__codigo_curso="INF-2024-01").order_by('-rut_estudiante')
print(estudiantes.query)
```

### Uso de Q objects

Podemos usar los Q objects para hacer consultas más complejas. [Documentación](https://docs.djangoproject.com/en/5.1/topics/db/queries/#complex-lookups-with-q)

```python
from django.db.models import Q

# Obtener los estudiantes que tienen una dirección determinada o correo que contenga 'example.com'
estudiantes = Estudiante.objects.filter(
    Q(direccion="Calle Falsa 123") | Q(correo__icontains="example.com")
)

print(estudiantes.query)
print(estudiantes)

# Obtener los estudiantes que estan en el curso de INF-2024-01 y no tiene una dirección determinada
estudiantes = Estudiante.objects.filter(
    Q(cursos__codigo_curso="INF-2024-01") & ~Q(direccion="Calle Falsa 123")
)

print(estudiantes.query)
print(estudiantes)
```

### Funciones de agregación

Podemos usar las funciones de agregación para obtener resultados más complejos. [Documentación](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#aggregation-functions)

```python
from django.db.models import Count, Sum

# Obtener el número de estudiantes
numero_estudiantes = Estudiante.objects.count()
print(numero_estudiantes)

# Obtener la cantidad total de horas de todos los programas
horas_programas = Programa.objects.aggregate(Sum('cantidad_horas'))
print(horas_programas)
```

### Anotaciones

```python
from django.db.models import Count

programas = Programa.objects.annotate(num_modulos=Count('modulo'))

for programa in programas:
    print(programa.nombre_programa, programa.num_modulos)
```

## Ejercicio A: Consultas avanzadas usando Django ORM

Genere un informe sobre los programas, módulos y relatores. Guíese según las siguientes tareas:

1. Lista de programas y total de horas de sus módulos: Crear una consulta que anote el número de módulos y el total de horas de los módulos asociados a cada programa. Mostrar el nombre del programa, el número de módulos y las horas totales.
2. Relatores con más de 5 años de experiencia asignados a módulos: Crear una consulta que liste los relatores que tienen más de 5 años de experiencia, junto con los nombres de los módulos en los que enseñan. Optimizar la consulta usando prefetch_related.
3. Filtrar módulos en base a horas con Q objects: Crear una consulta que devuelva módulos que cumplan al menos una de las siguientes condiciones: 
    1. Tienen más de 100 horas. 
    2. Pertenecen al programa "Ingeniería en Informática".
4. Cursos con programas optimizados con select_related: Crear una consulta que devuelva los cursos y sus programas asociados, optimizando el acceso a la relación con select_related.

Opcional:
1. Crear una consulta que anote el número de relatores por programa, incluyendo solo aquellos relatores con más de 5 años de experiencia.
2. Mostrar el total de módulos de cada programa y actualizar su nombre para agregar el número de módulos al final (por ejemplo: "Ingeniería en Informática (3 módulos)").

## Solución

* [solución](ejercicio-bloque-a.py)

## Ejercicio B: Manejo de transacciones con try-except, commit y rollback.

Basados en el resultado del ejercicio anterior.

1. Crear un script en Python que siga el siguiente flujo:
    a) Insertar un nuevo estudiante en la tabla estudiante. Considere almacenar los datos del nuevo estudiante en variables separadas. 
    b) Verificar si un programa especifico existe en la tabla programa.
    c) Si el programa existe, registrar la inscripción del estudiante en la tabla `estudiante_curso` para el curso asociado al programa anterior.
    d) Confirmar los cambios con commit.
    e) En caso de error, usar rollback para revertir los cambios.
2. Condiciones:
    a) Si el id_programa no existe, generar un error y revertir la transacción.
    b) Manejar excepciones, recuerde clase 5 del modulo 2 de este curso. 

## Solución

* [solución](ejercicio-bloque-b/)

