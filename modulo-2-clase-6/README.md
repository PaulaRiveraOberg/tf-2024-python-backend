# Módulo 2 - Clase 6: Desarrollo de aplicaciones web en Python

## Ejercicios

### Bloque A - Ejercicio 1

Configuración inicial y rutas básicas
* **Objetivo**: Configurar la estructura básica de la aplicación Flask y crear rutas principales con HTML estático. 
* Instale Flask. 
* Cree una aplicación Flask con las rutas iniciales:
  * `/` Página de inicio con una bienvenida al sitio informativo. 
  * `/about`: Página "Acerca de", que contenga una breve descripción del grupo y los nombres de los integrantes.
* Cree un archivo `app.py` y una carpeta `templates/` con templates HTML para cada ruta (`index.html` y `about.html`). 


[solución](bloque-a-ej-1/)

### Bloque A - Ejercicio 2
Uso de templates y datos dinámicos
* **Objetivo**: renderizar contenido dinámico en los templates. 
* Modificar la ruta /about para pasar datos dinámicos a about.html 
  * a. Nombre del grupo 
  * b. Breve descripción de su objetivo en el curso. 
  * c. Lista de integrantes 
* Extra: mostrar la fecha y hora actualizadas cada vez que se cargue la página usando Python. 

[solución](bloque-a-ej-2/)

### Bloque B - Ejercicio 1
Creando un Perfil de integrante del grupo con Parámetros en el Query String
* **Objetivo**: Practicar el uso de query string en Flask para personalizar la página de perfil de un integrante del grupo. 
* Crea una ruta /perfil que reciba los siguientes parámetros opcionales en el query string; nombre, edad, profesión. 
* Si un parámetro no se proporciona en el query string, establece un valor predeterminado. 
* Muestra una respuesta que salude al usuario y describa su perfil con la información proporcionada. Use un template para mostrar los datos formateados.

* [solución](bloque-b-ej-1/)

### Bloque B - Ejercicio 2
* Objetivo: Crear una funcionalidad en el sitio web del grupo que permita publicar y visualizar anuncios importantes. 
* Ruta de publicación de Anuncio (`/anuncio`). 
  * La ruta `/anuncio` debe aceptar dos métodos; 
  * `GET`: Muestra un formulario para agregar un anuncio
  * `POST`: Procesa el formulario y guarda el anuncio en una lista en memoria. 
  * El formulario debe tener los siguientes campos; título (obligatorio), contenido (obligatorio), prioridad (alta, media, baja) con valor predeterminado media. 
* Página de Anuncios (`/anuncios`): 
  * La ruta `/anuncios` muestra todos los anuncios publicados. 
  * Usa ciclos en el template para mostrar los anuncios en forma de lista. 
  * Los anuncios de prioridad Alta deben resaltarse visualmente (por ejemplo, con un color diferente). 
  * Si no hay anuncios publicados, muestra un mensaje indicándolo.

[solución](bloque-b-ej-2/)