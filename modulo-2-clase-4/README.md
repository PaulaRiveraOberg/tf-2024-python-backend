# Modulo 2 - Clase 4: Principios de Diseño Orientado a Objetos

## Ejercicios

### Bloque A - Ejercicio 1
Creación de objetos complejos

* Cree las clases Waypoint y Trackpoint.
* La clase Waypoint contiene un nombre; la clase Trackpoint contiene una fecha de registro.
* Ambas clases son posiciones geográficas de tipo Position.
* La clase Position requiere en su inicialización una latitud, una longitud y una altitud.

[solución](bloque-a-ej-1.py)

### Bloque A - Ejercicio 2
Múltiples representaciones

* Cree dos representaciones para los objetos de tipo posición:
    * Una representación de atributos separados por coma (string).
    * Una representación de atributos como diccionario.

[solución](bloque-a-ej-2.py)

### Bloque A - Ejercicio 3
Distancia geodésica

* Importe la biblioteca `geopy` para hacer uso de la función de distancia geodésica (`import geopy.distance`).
* Cree una clase `helper` llamada `Distance` que se inicialice con dos posiciones: una posición de origen y una posición de destino.
* Cree un método llamado `km(self)` que retorne la distancia geodésica en kilómetros.
    ```python
    return geopy.distance.geodesic(
                ((self.source.__dict__())["latitude"],
                (self.source.__dict__()["longitude"])),
                ((self.destination.__dict__())["latitude"],
                (self.destination.__dict__()["longitude"]))
            ).km
    ```

[solución](bloque-a-ej-3.py)

### Bloque B - Ejercicio 1
Instalación de Visual Paradigm Community Edition

* Baje el software Visual Paradigm en su versión Community Edition en el siguiente enlace: https://www.visual-paradigm.com/download/community.jsp
* Instale el software en su computador.
* Inicie el software, asigne un directorio para sus modelos, y cree un diagrama de clases (sin asignar clases).

### Bloque B - Ejercicio 2
Modelo de clases
* Construya un modelo de clases para el caso del ejercicio anterior (Bloque A).
* Presente y discuta el modelo.

### Bloque B - Ejercicio 2
Viento registrado en estaciones de monitoreo
* Modifique el programa anterior para mostrar por pantalla los vientos que sobrepasan los 20 kilómetros por hora.
* Utilice una operación filter() para complementar el ejercicio anterior de tal manera que pueda dar cumplimiento a los requisitos de este ejercicio.
