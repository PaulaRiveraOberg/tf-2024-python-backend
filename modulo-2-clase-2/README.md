# Modulo 2 : Estructuras de Datos Avanzadas

## Ejercicios Clase 2

### Bloque A - Ejercicio 1
Cálculo de promedio y rango
* Crear una lista con los siguientes números:
    ```python
    10, 20, 5, 60, 20, 10 # en este orden
    ```
* Determine el rango del conjunto de números.
* Determine el promedio haciendo uso del ciclo for.
* Determine el promedio haciendo uso de las funciones genéricas que aplican sobre la lista.

[solución](bloque-a-ej-1.py)

### Bloque A - Ejercicio 2

Estudiantes y sus notas:
Desarrolle un programa que permita almacenar y calcular el promedio de notas de cinco estudiantes en una escuela. Cada estudiante tiene tres calificaciones en un rango de 1 a 7. El sistema debe solicitar los datos de los estudiantes y sus notas al usuario y luego mostrar el promedio de calificaciones de cada estudiante. 

* Crear un programa que solicite el nombre de cada uno de los cinco estudiantes. Para cada estudiante, solicite tres notas. 
* Almacenar los datos de cada estudiante (nombre y lista de notas) en una lista de listas. 
* Calcular el promedio de notas para cada estudiante. Mostrar el nombre de cada estudiante junto con su promedio. 

[solución](bloque-a-ej-2.py)

### Bloque B - Ejercicio 1
Registro de personas (Lista de diccionarios):

Desarrolla un programa que permita registrar el nombre y apellido de varias personas, almacenando cada registro en un diccionario y organizando todos los registros en una lista.

* Solicita al usuario los datos de cada persona. Cada persona debe ser almacenada en un diccionario con las claves "nombre" y "apellido". 
* Guarda cada diccionario en una lista llamada personas. Cada vez que se ingresen los datos de una persona, crea un diccionario y agrégalo a la lista personas. 
* El programa debe continuar solicitando datos hasta que el usuario ingrese "FIN" como nombre. 
* Mostrar la lista de personas. Recorre la lista personas e imprime el nombre y apellido de cada persona registrada. 

[solución](bloque-b-ej-1.py)

### Bloque B - Ejercicio 2
Cursos y notas de una persona
* Incrementar la funcionalidad del programa anterior permitiendo que ahora cada persona cuente con cursos inscritos. 
* Es decir, necesitamos que cada persona contenga un diccionario con claves correspondientes a cursos y cada clave con una lista con las notas de dicho curso. 
* Todos los datos deben ser solicitados por la entrada estándar. Puede considerar ingresar un curso por persona. Cada curso tendrá 3 notas. 
* Al finalizar, el programa debe imprimir el nombre y apellido, seguido del listado de cursos y los promedios obtenidos en cada curso.

[solución](bloque-b-ej-2.py)
