# Modulo 4 - Clase 2 Introducción al framework Django

## Ejercicios

### Bloque A - Ejercicio 1

Configuración de Django y Creación de una Aplicación Sencilla

Instrucciones: 
1. Configura un proyecto Django llamado sitio_grupo.
2. Crea una aplicación dentro del proyecto llamada info.
3. Define una ruta en urls.py que apunte a una vista llamada inicio, que devuelva un mensaje sencillo como "Bienvenidos al sitio web del grupo".
4. Ejecuta el servidor de desarrollo y verifica que puedas acceder al mensaje en el navegador.

Soluciones:
* [solución](bloque-a-ej-1/)

### Bloque A - Ejercicio 2

Vista Dinámica con Parámetros en la URL

Instrucciones:
1. Agrega una ruta en `urls.py` llamada `detalles/<str:proyecto>/` para mostrar detalles básicos sobre un proyecto del grupo.
2. Define una vista en `views.py` que reciba el parámetro dinámico `proyecto` y devuelva un mensaje como "Detalles del proyecto: [proyecto]".
3. Asegúrate de que el nombre del proyecto aparezca con todas las palabras capitalizadas.
4. Verifica que la vista funcione correctamente accediendo a URLs como `/detalles/proyecto-inicial/` y `/detalles/nuevo-desafío/`.


Soluciones:
* [solución](bloque-a-ej-2/)

### Bloque B - Ejercicio 1

Renderización de Plantillas para Mostrar Proyectos

Objetivo: Utilizar plantillas HTML para mostrar información dinámica sobre los proyectos del grupo. 
Instrucciones: 
1. Crea una plantilla `proyecto.html` que reciba un diccionario de contexto con los campos `nombre`, `descripcion` y `estado` (activo o finalizado).
2. Modifica la vista `detalles` para enviar estos valores a la plantilla. 
3. La plantilla debe mostrar un mensaje como: "Nombre del proyecto: [nombre]", "Descripción: [descripcion]" y "Estado: [estado]".
4. Prueba la funcionalidad con diferentes proyectos y verifica que se muestren correctamente.


Soluciones:
* [solución](bloque-b-ej-1/)

### Bloque B - Ejercicio 2

Modelo Sencillo y Uso del Administrador de Django

Objetivo: Crear un modelo básico para gestionar datos en el panel de administración de Django. 

Instrucciones:
1. Define un modelo `Proyecto` en `models.py` con los campos:
    - `nombre` (máximo 100 caracteres).
    - `descripcion` (campo de texto).
    - `fecha_inicio` (tipo `DateField`). 
2. Realiza las migraciones necesarias y ejecútalas para que el modelo se refleje en la base de datos.
3. Registra el modelo en `admin.py` para que sea gestionable desde el panel de administración.
4. Crea un superusuario y accede al panel de administración. Verifica que puedes agregar, editar y eliminar proyectos desde esta interfaz.

Soluciones:
* [solución](bloque-b-ej-2/)