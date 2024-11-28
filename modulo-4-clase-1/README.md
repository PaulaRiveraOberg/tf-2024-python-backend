# Modulo 4 - Clase 1 Introducción al desarrollo con frameworks

## Ejercicios

### Bloque A - Ejercicio 1

Para entender los beneficios de usar un framework y comprender los componentes de este vamos a crear nuestro propio framework desde cero usando python.

Utilizando el archivo python con la implementación del servidor server.py y el punto de entrada app.py:
* Implemente una vista de acuerdo con la filosofía de Django (views.py)
* La vista en este caso asumirá las funciones de presentación y modelo, que aún no hemos implementado.
* La vista debe ser un objeto que implemente el metodo get_response 

Soluciones:
* [solución](bloque-a-ej-1/)

### Bloque A - Ejercicio 2

Implemente una lógica de templates simples

* Cree un nuevo archivo llamado templates.py, este debe definir un método llamado render_template
* El método recibe un nombre de template y lee el contenido del archivo desde un directorio llamado templates, retornando su contenido.
* La vista ahora retornará el resultado de llamar a render_template sobre el template home.html
* Asegúrese de cambiar el tipo de contenido del server, ahora es:
    ```python
    self.send_header("Content-Type", "text/html")
    ```


Soluciones:
* [solución](bloque-a-ej-2/)

### Bloque B - Ejercicio 1

Terminemos la implementación de nuestro framework MVC, para esto crearemos el modelo.

* Cree un archivo llamado models.py este tendrá nuestros modelos y lógica de negocios, no interactuará con ninguna base de datos por simplificación, pero tendremos una lista de avisos.
* Implemente un método llamado all (de instancia por simplicidad) que retorne el listado como un diccionario.
* Desde la vista importe el modelo e imprima de momento por consola el resultado de invocar el método all.

Soluciones:
* [solución](bloque-b-ej-1/)

### Bloque B - Ejercicio 2

Finalmente conectaremos el último componente, usemos los datos del modelo para renderizar.

* Modificaremos el archivo templates.py para que utilice jinja como lenguaje de templates. Se proporciona el nuevo archivo.
* Cambie la vista para entregar las variables a usar en el renderizado como contexto, se debe pasar un diccionario.
* Utilice estas variables en el template home.html para renderizar los avisos


Soluciones:
* [solución](bloque-a-ej-2/)