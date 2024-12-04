# Modulo 4 - Clase 3 Modelos y el ORM de Django

## Ejercicios

### Bloque A - Ejercicio 1

Crear Modelos y Relacionarlos

1. Crea los siguientes modelos en una aplicación llamada biblioteca:
    - Autor: Almacena el nombre y la fecha de nacimiento.
    - Libro: Contiene título, fecha de publicación y una relación Muchos a Muchos con Autor.
    - Género: Define un género literario con un campo de nombre único. Relaciona Libro con Género mediante una relación Uno a Muchos (ForeignKey).
2. Realiza las migraciones necesarias para reflejar estos modelos en la base de datos. 
3. Registra los modelos en el admin de Django, y realice algunas inserciones para probar consistencia. 


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

Construir una Vista para Listar Productos en JSON

1. Crea una vista LibroListView que:
    - Use la clase base View.
    - Maneje solicitudes HTTP GET.
    - Recupere datos del modelo Libro, incluyendo; título, género, autores asociados. 
    - Devuelva los datos en formato JSON. 
2. Configura la URL para la vista. 
3. **EXTRA**: Personaliza la respuesta JSON para que incluya un mensaje como "total": `<número de productos>`. 

Pistas:
    - Usa un queryset para obtener todos los libros. 
    - Itera sobre los libros y utiliza sus relaciones para construir el JSON. 
    - Utiliza JsonResponse para retornar la respuesta.


Soluciones:
* [solución](bloque-b-ej-1/)

### Bloque B - Ejercicio 2

Filtrar Libros por Género y Mostrar Autores

1. Crea una vista LibroFiltrarView que:
    - Use la clase base View.
    - Maneje solicitudes HTTP GET.
    - Recibe un parámetro genero desde la URL (query string).
    - Filtra los libros que pertenecen al género especificado. 
    - Devuelve los datos en formato JSON, incluyendo; título, género, y autores asociados. 
2. Configura la URL para la vista. 

Pistas:
    - Usa `request.GET.get('genero')` para obtener el valor del parámetro género.
    - Filtra los libros por género. 
    - Itera sobre los libros para construir la respuesta JSON. 
    - Si no se proporciona el parámetro genero, devuelve un error JSON con un código de estado 400. 

Soluciones:
* [solución](bloque-b-ej-2/)