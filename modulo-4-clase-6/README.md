# Modulo 4 - Clase 6 Construyendo una API en DRF

## Caso: Gestión de Reservas de Hotel

* Un hotel necesita desarrollar una API para gestionar la disponibilidad de sus habitaciones y permitir que los usuarios puedan realizar reservas de manera programática.
* La API debe ser funcional, segura y accesible para diferentes tipos de usuarios con roles específicos. El sistema debe incluir autenticación simple mediante Token Authentication y permisos diferenciados para administradores y usuarios normales.

## Descripción General del Sistema

* Administradores:
  * Pueden gestionar habitaciones (crear, listar, actualizar y eliminar).
  * No pueden realizar reservas.
* Usuarios normales:
  * Pueden crear reservas para habitaciones disponibles.
  * Pueden listar las reservas que hayan realizado.
  * No pueden gestionar habitaciones.
* Autenticación:
  * Todos los usuarios deben autenticarse con un token de autorización para acceder a la API.
  * Los tokens se generan a través de un endpoint especial. 

## Modelos del sistema

* Room (Habitación): Representa la habitación del hotel.
  * name: Nombre de la habitación (ej., "Suite Ejecutiva").
  * description: Descripción breve (ej., "Una suite amplia con vista al mar").
  * price_per_night: Precio por noche (en dólares).
  * is_available: Indica si la habitación está disponible.

* Reservation (Reserva): Representa una reserva realizada por un usuario.
  * user: Usuario que realiza la reserva.
  * room: Habitación reservada.
  * start_date: Fecha de inicio de la reserva.
  * end_date: Fecha de fin de la reserva.

## Requisitos técnicos

1. Endpoints para Habitaciones (Rooms):
   * GET /rooms/: Lista todas las habitaciones. Solo accesible para administradores.
   * POST /rooms/: Crea una nueva habitación. Solo accesible para administradores.
   * PUT /rooms/{id}/: Actualiza los datos de una habitación existente. Solo accesible para administradores.
   * DELETE /rooms/{id}/: Elimina una habitación existente. Solo accesible para administradores.
2. Endpoints para Reservas (Reservations):
   * GET /reservations/: Lista todas las reservas realizadas por el usuario autenticado.
   * POST /reservations/: Crea una reserva para una habitación disponible.
3. Endpoint para Autenticación:
   * POST /api/token/: Genera un token de autenticación para el usuario. Los usuarios deben enviar sus credenciales (username y password) para obtener el token.
4. Endpoint personalizado : Para verificar la disponibilidad de una habitación en un
rango de fechas determinado. Este endpoint permite a los usuarios consultar si una
habitación está disponible antes de realizar una reserva.
   * GET /rooms/{id}/check_availability/
   * start_date (obligatorio): Fecha de inicio en formato YYYY-MM-DD.
   * end_date (obligatorio): Fecha de fin en formato YYYY-MM-DD.

## Criterios para probar las APIs

1. Autenticación:
   * Los usuarios pueden obtener un token de autorización mediante sus credenciales.
   * Todos los endpoints requieren un token válido para acceder.
2. Permisos:
   * Los administradores pueden gestionar habitaciones pero no reservas.
   * Los usuarios normales pueden crear y listar reservas pero no gestionar habitaciones.
3. Operaciones CRUD:
   * Los administradores pueden realizar operaciones CRUD completas sobre habitaciones.
   * Los usuarios normales pueden realizar operaciones de creación y lectura sobre reservas.
4. Validaciones:
   * Las fechas de reserva deben ser válidas (por ejemplo, la fecha de inicio debe ser anterior a la fecha de fin).
   * Las reservas no pueden superponerse con otras reservas para la misma habitación.

## Formatos de Respuesta
* `/rooms/`

```json
[
    {
        "id": 1,
        "name": "Suite Ejecutiva",
        "description": "Una suite amplia con vista al mar",
        "price_per_night": 150.00,
        "is_available": true
    },
    {
        "id": 2,
        "name": "Habitación Doble",
        "description": "Habitación con dos camas individuales",
        "price_per_night": 100.00,
        "is_available": false
    }
]
```

* /reservations/

```json
[
    {
        "id": 1,
        "user": 2,
        "room": 1,
        "start_date": "2024-12-10",
        "end_date": "2024-12-15"
    }
]
```

* `/api/token/`

```json
{
    "token": "7f5c5a2bfc0e49ef9d401a2c2dbb51d8"
}
```

## Notas Importantes

Los desarrolladores deberán implementar esta API usando Django REST Framework.
* Se recomienda utilizar serializers, ViewSets y routers para simplificar el desarrollo.
* Las pruebas pueden realizarse con herramientas como Postman o el cliente de API integrado en Django.
* Ante dudas consulte primero las diapositivas de clases previas, y luego la documentación oficial del framework disponible en:
  * https://www.django-rest-framework.org/
  * https://docs.djangoproject.com/en/5.1/


## Solución

* [solución](hotel_api/README.md)


## Parte 2

En esta parte agregaremos documentación a la API usando Swagger, mediante la libreria `drf-spectacular`.

* [solución](hotel_api_doc/README.md)
