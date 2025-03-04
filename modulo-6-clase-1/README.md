## Clase 1: Seguridad en API REST

## Autenticación en FastAPI

Para proteger un endpoint en FastAPI mediante [Http Basic Auth](https://fastapi.tiangolo.com/es/advanced/security/http-basic-auth/) usamos el siguiente codigo base:

```python
import secrets
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"usuario"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"mipassword"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/users/me")
def read_current_user(username: Annotated[str, Depends(get_current_username)]):
    return {"username": username}
```

## Authenticación en DRF

Podemos implementar tambien http basic auth en Django Dest Framework, para esto debemos configurar en `settings.py` la variable `REST_FRAMEWORK`:

```python
# settings.py
...
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}
```

esto permitirá autenticarnos mediante `BasicAuthentication` usuando los usuarios creados en la autenticación de Django, django-auth. Para proteger nuestros endpoints debemos especificar mediante la siguiente configuración en las vistas:

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
* En esta clase, nuestra tarea será incorporar autenticación a estos endpoints y probar el funcionamiento de la autenticación.
* Si no tenemos listos los endpoints, ¡este es el momento para ponernos al día!

* Solución: [ejercicio-bloque-a](./ejercicio-bloque-a/README.md)
* Solución: [ejercicio-bloque-a-django](./ejercicio-bloque-a-django/README.md)