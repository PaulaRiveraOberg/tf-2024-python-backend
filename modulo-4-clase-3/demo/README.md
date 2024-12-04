## Utilización del ORM Django

### Activación del entorno virtual

Primero debemos activar el entorno virtual, en linux y mac se puede activar con el siguiente comando:

```bash
source .venv/bin/activate
```

en el caso de windows se puede activar con el siguiente comando:

```bash
.venv\Scripts\activate
```

### Comando usados en la demo

```bash
# creación de app
python manage.py startapp myapp
# activar app en settings.py
INSTALLED_APPS = [
    ...
    'myapp.apps.MyappConfig',
]
# creación de modelo en models.py
```

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
```

Podemos usar https://sqliteviewer.app/ para visualizar la base de datos.

```bash
# creación de migración
python manage.py makemigrations
# aplicación de migración
python manage.py migrate
```

Agregar un nuevo campo a un modelo existente:

```python
ESTADOS = [
    ('ACTIVO', 'Activo'),
    ('INACTIVO', 'Inactivo'),
]

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)    
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ACTIVO')
```

### Creación de modelos con relaciones:

```python
ESTADOS = [
    ('ACTIVO', 'Activo'),
    ('INACTIVO', 'Inactivo'),
]

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ACTIVO')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True, blank=True)
    etiquetas = models.ManyToManyField('Etiqueta')
```

Activación de administración de modelos:

```python
@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass
```

```bash
# creación de migración
python manage.py makemigrations
# aplicación de migración
python manage.py migrate
# creación de superusuario
python manage.py createsuperuser
```

### Django shell

Para probar la consulta de datos podemos construir querysets para esto usaremos el shell de django:

```bash
python manage.py shell
```

En este importamos los modelos y construimos querysets:

```python
from myapp.models import Producto, Etiqueta

productos = Producto.objects.all()
```

### Consultas usando el ORM

```python
productos = Producto.objects.all()
productos = Producto.objects.filter(estado='ACTIVO')
productos = Producto.objects.filter(estado='ACTIVO', precio__gt=100)
productos = Producto.objects.filter(estado='ACTIVO', precio__gt=100).order_by('precio')
productos = Producto.objects.filter(estado='ACTIVO', precio__gt=100).order_by('-precio')
# filter by categoria
productos = Producto.objects.filter(categoria__nombre='Calzado')
# filter by etiqueta
productos = Producto.objects.filter(etiquetas__nombre='Calzado')
# display de objetos como diccionario
print(list(productos.values()))
```

Incluir relaciones en el resultado:

```python
productos = Producto.objects.filter(categoria__nombre='Calzado').select_related('categoria')
```

Obtención de valores agregados:

```python
from django.db.models import Avg, Max

estadisticas = Producto.objects.filter(categoria__nombre="Calzado").aggregate(
    precio_promedio=Avg('precio'),
    precio_maximo=Max('precio')
)

Obtención solo de un valor:

```python
productos = Producto.objects.filter(categoria__nombre="Calzado").values('nombre')
[producto['nombre'] for producto in productos]
```

```python
productos = Producto.objects.filter(categoria__nombre="Calzado").values_list('nombre', 'precio')
[producto for producto in productos]
```

Creación de nuevos objetos:

```python
producto = Producto(nombre='Zapato', precio=100, estado='ACTIVO')
producto.save()
```

Actualización de objetos:

```python
producto = Producto.objects.get(id=1)
producto.precio = 150
producto.save()
```

Eliminación de objetos:

```python
producto = Producto.objects.get(id=1)
producto.delete()
# elimiación de varios objetos
Producto.objects.filter(precio__lt=500).delete()
# eliminación de todos los objetos
Producto.objects.all().delete()
```

### consultar relaciones

```python
productos = Producto.objects.filter(categoria__nombre='Calzado')
pprint(list(productos.values()))
```

many to many:

```python
producto = Producto.objects.get(id=1)
pprint(list(producto.etiquetas.all().values()))

etiqueta = Etiqueta.objects.get(id=1)
pprint(list(etiqueta.producto_set.all().values()))
```

### Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

para ver las migraciones aplicadas y pendientes:

```bash
python manage.py showmigrations
```
