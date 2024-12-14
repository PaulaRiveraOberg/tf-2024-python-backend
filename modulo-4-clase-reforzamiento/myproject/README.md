# Proyecto Django

## Instalación

No olvidar crear el entorno virtual y activar el entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
# en windows
.\.venv\Scripts\activate
```

## Proceso de desarrollo

Partimos desarrollando los modelos en [`models.py`](myapp/models.py)

Luego, creamos las vistas en [`views.py`](myapp/views.py)

Y finalmente, creamos las URLs en [`urls.py`](myapp/urls.py)

También debemos crear las plantillas en [`templates/`](myapp/templates/)


Para poder editar nuestros modelos en el admin de Django, debemos registrarlo en [`admin.py`](myapp/admin.py)

Antes de poder acceder a nuestro admin, debemos crear las migraciones, ejecutar las migraciones y crear un superusuario:    

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

También podemos cargar datos de prueba en nuestra base de datos:

```bash
python manage.py loaddata myapp/seed/posts.json
```

## Ejecución

```bash
python manage.py runserver
```

## Acceso a la aplicación

Accedemos a la aplicación en [http://localhost:8000/](http://localhost:8000/)

Accedemos al admin de Django en [http://localhost:8000/admin/](http://localhost:8000/admin/)