# Modulo 8: Fundamentos de Integración Continua

## Clase 5: Monitorización y APM

### Parte 1: Monitorización local mediante Django Debug Toolbar

Nos basaremos en el proyecto de ejemplo disponible en el directorio [miproyecto](./miproyecto). Este es una API para un sitio de ventas de libros en linea.

Para iniciar el proyecto, primero debemos instalar las dependencias del proyecto.

```bash
cd miproyecto
pip install -r requirements.txt
# instalaremos tambien django-debug-toolbar
pip install django-debug-toolbar
```

Luego inicializaremos la base de datos.

```bash
python manage.py migrate
```

Indicaremos en la guía los pasos para instalar [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/).


Tras instalar el package `django-debug-toolbar`, agregamos la aplicación `debug_toolbar` y el middleware en el archivo [`myproject/settings.py`](./miproyecto/myproject/settings.py).

```python
INSTALLED_APPS = [
    # requerida por debug toolbar
    "django.contrib.staticfiles",
    ...
    'debug_toolbar',
    ...
]
# requerida por debug toolbar
STATIC_URL = "static/"
...
MIDDLEWARE = [
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
# nos aseguramos tambien de tener las siguientes configuraciones:
INTERNAL_IPS = [
    "127.0.0.1",
]
```

Debemos agregar el siguiente código en el archivo [`myproject/urls.py`](./miproyecto/myproject/urls.py).

```python
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    ...
] + debug_toolbar_urls()
```

Ejecutamos el servidor de desarrollo.

```bash
python manage.py runserver
```

Revisemos nuestra API en el navegador.

```bash
http://127.0.0.1:8000/api/libros/
```

Revisemos una web simple que creamos en el directorio [`web`](./miproyecto/web).

```bash
http://127.0.0.1:8000/
```

Explora las distintas pestañas del Debug Toolbar, entre ellas:

- SQL: Muestra las consultas SQL que se han realizado.
- Templates: Muestra el template que se está utilizando.
- Request/Response: Muestra la respuesta que se está devolviendo.
- History: Muestra el historial de las peticiones.
- Profiling: Muestra el tiempo que se ha tardado en ejecutar las peticiones.

### Parte 2: Monitorización en producción con Sentry

Instalamos el paquete de Sentry con el extra de django.

```bash
pip install sentry-sdk[django]
```

Luego configuramos el archivo [`myproject/settings.py`](./miproyecto/myproject/settings.py).

```python
import sentry_sdk
...
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
```

Podemos generar una url para enviar un error de prueba. Para esto, agregamos una vista en el archivo [`myproject/views.py`](./miproyecto/myproject/urls.py).

```python
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    # ...
]
```

```bash
http://127.0.0.1:8000/sentry-debug/
```

Para activar la trazabilidad y profiling debemos ademas agregar las siguientes configuraciones en el archivo [`myproject/settings.py`](./miproyecto/myproject/settings.py).

```python
sentry_sdk.init(
    ...
    traces_sample_rate=1.0,
    profile_session_sample_rate=1.0,
)
```

Debemos ajustar los sample rates segun nuestras necesidades cuando estemos en producción, para no enviar demasiados eventos a Sentry dado que de acuerdo al plan tenemos un límite eventos por mes.