## Clase 2: Basic Auth con Django

## Autenticación y Autorización en Django

### Configuración inicial

* Primero debemos constar con las dependencias del proyecto, para ello se debe ejecutar el siguiente comando:

```bash
pip install django django-rest-framework
```

* luego crearemos el proyecto y la app:

```bash
django-admin startproject miapi
cd miapi
django-admin startapp autenticacion
```

* luego debemos agregar la app a la configuración del proyecto:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'autenticacion.apps.AutenticacionConfig',
]
Para implementar http basic auth en Django Dest Framework debemos configurar en `settings.py` la variable `REST_FRAMEWORK`:

```python
# settings.py
...
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        # para poder usar session authentication
        "rest_framework.authentication.SessionAuthentication",
    ],
    # para proteger todos nuestros endpoints requiriendo autenticación
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
```

esto permitirá autenticarnos mediante `BasicAuthentication` usuando los usuarios creados en la autenticación de Django, django-auth.

Para proteger nuestros endpoints debemos especificar mediante la siguiente configuración en las vistas:

```python
#app/views.py
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
```

Si queremos poder logearnos en la aplicación web que provee DRF para acceder a nuestra API, no debemos olvidar agregar las rutas a `api-auth` en `urls.py` del proyecto.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("books.urls")),
]
```

## Ejercicio A: Agregando autenticación a nuestras APIs

* En las últimas clases antes del receso, estuvimos diseñando algunos endpoints para manejo de bibliotecas (libros, reviews).
* Ahora, los usuarios normales podrán ver la lista de libros, pero sólo los administradores podrán acceder a una "Sala VIP" con los libros más exclusivos. 
* Crear los siguientes endpoints: 
    * GET `/biblioteca/`: accesible para cualquier usuario autenticado que entrega una lista de libros. 
    * GET `/sala-vip/`: accesible solo para administradores, que entrega sólo los libros exclusivos. 

*Recuerde*: El objetivo es implementar autenticación y autorización utilizando Basic Auth. Comience con una lista de libros estática y, posteriormente, refine su solución integrándola con los modelos de Django para gestionar los datos desde la base de datos.


* Solución: [ejercicio-bloque-a](./ejercicio-bloque-a/README.md)
