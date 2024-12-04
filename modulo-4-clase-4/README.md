# Ejercicios: Gestión de Libros, Revistas y Reservas en Django REST Framework

## Bloque A - Ejercicio 1: Gestión de Libros en la Biblioteca

### Requerimientos
1. Crear un modelo `Libro` con los siguientes campos:
   - `titulo`: Título del libro (cadena, máximo 100 caracteres).
   - `genero`: Género literario del libro (cadena, máximo 50 caracteres).
   - `num_paginas`: Número de páginas del libro (entero).

2. Crear un serializador para el modelo `Libro` que transforme los datos en JSON.

3. Configurar un `ViewSet` para manejar las operaciones CRUD básicas.

4. Registrar las rutas para el `ViewSet` en un `Router`.

### Pruebas
1. Crear un libro con información básica.
2. Listar todos los libros registrados.

### Soluciones:
* [solución](bloque-a-ej-1/)

---

## Bloque A - Ejercicio 2: Gestión de Revistas

### Requerimientos
1. Crear un modelo `Revista` con los siguientes campos:
   - `titulo`: Título de la revista (cadena, máximo 100 caracteres).
   - `tema`: Tema principal de la revista (cadena, máximo 50 caracteres).
   - `frecuencia_publicacion`: Frecuencia de publicación (cadena, valores posibles: "Diaria", "Semanal", "Mensual").
   - `num_edicion`: Número de edición (entero).

2. Crear un serializador para el modelo `Revista`.

3. Configurar un `ViewSet` para manejar las operaciones CRUD básicas.

4. Registrar las rutas para el `ViewSet` en un `Router`.

### Pruebas
1. Crear una revista con información básica.
2. Listar todas las revistas registradas.
3. Probar qué sucede si intentas registrar una revista con un valor no válido para `frecuencia_publicacion`.

### Soluciones:
* [solución](bloque-a-ej-2/)

---

## Bloque A - Ejercicio 1: Autenticación para Gestión de Libros

### Requerimientos
1. Configurar **Token Authentication**:
   - Modificar `settings.py` para requerir autenticación.
   - Agregar el módulo `rest_framework.authtoken` y aplicar migraciones.

2. Proteger los endpoints del modelo `Libro` para que solo usuarios autenticados puedan acceder.

3. Generar un token para un usuario de prueba.

### Pruebas
1. Intentar acceder a los endpoints de libros sin autenticarse (debería devolver `401 Unauthorized`).
2. Usar el token generado para autenticarse y realizar las operaciones CRUD en los libros.

### Soluciones:
* [solución](bloque-b-ej-1/)

---

## Bloque B - Ejercicio 2: Gestión de Reservas de Libros con Validaciones Personalizadas

### Requerimientos
1. Crear un modelo `Reserva` con los siguientes campos:
   - `libro`: Nombre del libro reservado (cadena, máximo 100 caracteres).
   - `usuario`: Nombre del usuario que realiza la reserva (cadena, máximo 100 caracteres).
   - `fecha_reserva`: Fecha en la que se realiza la reserva (fecha).

2. Implementar validaciones personalizadas en el serializador:
   - La `fecha_reserva` no puede ser en el pasado.

3. Configurar un `ViewSet` para manejar las operaciones CRUD del modelo `Reserva`.

4. Agregar un endpoint adicional para listar reservas activas:
   - Endpoint: `/reservas/activas/`.
   - Definición: Listar reservas cuya fecha de reserva sea mayor o igual a la fecha actual.

### Pruebas
1. Crear una reserva con información básica.
2. Listar todas las reservas registradas.
3. Probar la validación personalizada al intentar registrar una reserva con una fecha en el pasado.
4. Verificar el endpoint adicional para listar reservas activas.

### Soluciones:
* [solución](bloque-b-ej-2/)