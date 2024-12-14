## Solución al caso

Primero activaremos el entorno virtual e instalaremos `django`, junto con `django-rest-framework` en caso que no lo tengamos instalado.

```bash
# activar entorno virtual en osx y linux
source .venv/bin/activate
# para activar en windows
.\.venv\Scripts\activate
# instalar django, django-rest-framework
pip install django django-rest-framework
```

## Proyecto django

Crear el proyecto django:

```bash
django-admin startproject hotel_api
```

Crearemos la aplicación que llamaremos `rooms`, no olvidar que debemos agregarla al proyecto en el archivo `hotel_api/settings.py`:

```bash
django-admin startapp rooms
```

## Modelos

Dentro de esta crearemos los modelos `Room` y `Reservation`.

* [modelos](rooms/models.py)

Despues de crear los modelos debemos crear las migraciones y migrar los cambios a la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Admin

Habilitares el modulo de admin para los modelos que creamos en la aplicación `rooms` en el archivo [rooms/admin.py](rooms/admin.py) y crearemos un superusuario:

```bash
python manage.py createsuperuser
```

## Endpoints

Primero habilitaremos el modulo de rest-framework en el archivo [hotel_api/settings.py](hotel_api/settings.py). Luego de esto crearemos los serializadores en el archivo [rooms/serializers.py](rooms/serializers.py), para esto usaremos el serializador `ModelSerializer` de django-rest-framework.

Crearemos los endpoints para las habitaciones y las reservas en el archivo [rooms/views.py](rooms/views.py). Para el caso de las reservar desactivaremos el endpoint de eliminar mediante el atributo `http_method_names` de la clase `ReservationViewSet`. También restringiremos las reservas listadas solo a las creadas por el usuario autenticado, esto lo realizaremos en el método `get_queryset` de la clase `ReservationViewSet`. Finalmente sobreescribiremos el método `perform_create` para que las reservas se guarden con el usuario autenticado.

Una vez creados los endpoints apuntaremos las urls a estos en [urls.py](hotel_api/urls.py)

## Autenticación y Autorización

Para la autenticación usaremos el modulo de rest-framework `TokenAuthentication` y lo habilitaremos en el archivo [hotel_api/settings.py](hotel_api/settings.py). Para la autorización usaremos el modulo de rest-framework `IsAdminUser` y `IsAuthenticated` estos los habilitaremos en el archivo [rooms/views.py](rooms/views.py).

Para determinar si un usuario es administrador utilizaremos el campo `is_staff` del modelo de usuario de django. Este campo se utiliza en el admin de django para determinar si un usuario es administrador y por ende si puede acceder a las vistas de administración.

## Carga de datos

Para cargar los datos de ejemplo usaremos el comando `loaddata` de django, el cual se encuentra en el archivo [manage.py](manage.py).

```bash
python manage.py loaddata data.json
```

Este comando creará los usuarios `roberto` y `roberto_user` con contraseñas `roberto`, para poder hacer las pruebas de los endpoints. Además creará 2 habitaciones y 1 reserva.

Si queremos eliminar los datos de la base de datos podemos usar el comando `flush` de django, el cual se encuentra en el archivo [manage.py](manage.py).

```bash
rm -rf db.sqlite3
python manage.py migrate
python manage.py loaddata data.json
```

# Prueba de los endpoints con curl

La solicitud sin autenticación no debería funcionar:

```bash
curl -X GET http://localhost:8000/api/rooms/
curl -X GET http://localhost:8000/api/reservations/
```

## Prueba de endpoints autenticados como administrador

Obtención de token:

```bash
curl -X POST http://localhost:8000/api/token/ -d 'username=roberto&password=roberto'
```

Si usamos bash podemos almacenar el token en una variable de entorno para usarlo en las siguientes solicitudes:

```bash
export TOKEN=$(curl -X POST http://localhost:8000/api/token/ -d 'username=roberto&password=roberto' | jq -r '.token')
echo $TOKEN
```

En caso de usar powershell podemos almacenar el token en una variable de entorno para usarlo en las siguientes solicitudes:

```bash
$TOKEN = (Invoke-WebRequest -Uri http://localhost:8000/api/token/ -Method POST -Body 'username=roberto&password=roberto' -UseBasicParsing).Content | ConvertFrom-Json | Select-Object -ExpandProperty token
echo $TOKEN
```

Listar habitaciones:

```bash
curl -X GET http://localhost:8000/api/rooms/ -H "Authorization: Token $TOKEN"
```

Crear una habitación:

```bash
curl -X POST http://localhost:8000/api/rooms/ -H "Authorization: Token $TOKEN" -H "Content-Type: application/json" -d '{"name": "Habitación 3", "description": "Habitación con vista a la playa", "price_per_night": 150.00}'
```

Modificar una habitación:

```bash
curl -X PUT http://localhost:8000/api/rooms/3/ -H "Authorization: Token $TOKEN" -H "Content-Type: application/json" -d '{"name": "Habitación 3", "description": "Habitación con vista a la playa", "price_per_night": 250.00}'
```

Ver una habitación:

```bash
curl -X GET http://localhost:8000/api/rooms/3/ -H "Authorization: Token $TOKEN"
```

Eliminar una habitación:

```bash
curl -X DELETE http://localhost:8000/api/rooms/3/ -H "Authorization: Token $TOKEN"
```

## Prueba de endpoints autenticados como usuario

Obtención de token y guardarlo en una variable de entorno:

```bash
export TOKEN_USER=$(curl -X POST http://localhost:8000/api/token/ -d 'username=roberto_user&password=roberto' | jq -r '.token')
echo $TOKEN_USER
```

Listar habitaciones, debiera fallar por falta de permisos:

```bash
curl -X GET http://localhost:8000/api/rooms/ -H "Authorization: Token $TOKEN_USER"
```

Crear una reserva:

```bash
curl -X POST http://localhost:8000/api/reservations/ -H "Authorization: Token $TOKEN_USER" -H "Content-Type: application/json" -d '{"room": 1, "start_date": "2024-01-01", "end_date": "2024-01-05"}'
```

Listar mis reservas:

```bash
curl -X GET http://localhost:8000/api/reservations/ -H "Authorization: Token $TOKEN_USER"
```

Al volver a crear la misma reserva debiera fallar por que la habitación ya tiene una reserva en ese rango de fechas:

```bash
curl -X POST http://localhost:8000/api/reservations/ -H "Authorization: Token $TOKEN_USER" -H "Content-Type: application/json" -d '{"room": 1, "start_date": "2024-01-01", "end_date": "2024-01-05"}'
```

Eliminar una reserva, no permitido:

```bash
curl -X DELETE http://localhost:8000/api/reservations/1/ -H "Authorization: Token $TOKEN_USER"
```

Buscar si una habitación está disponible:

```bash
curl -X GET "http://localhost:8000/api/rooms/1/check_availability/?start_date=2024-01-01&end_date=2024-01-05" -H "Authorization: Token $TOKEN_USER"
```

