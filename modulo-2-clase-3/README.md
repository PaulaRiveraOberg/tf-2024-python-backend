# Modulo 2 : Programación Funcional

## Ejercicios Clase 3

### Bloque A - Ejercicio 1
Valor absoluto

* Escriba una función lambda que reciba un número y retorne su valor absoluto.
* Recuerde que el valor absoluto realiza lo siguiente: si el número es positivo o cero, devuelve el mismo número; si el número es negativo, devuelve el mismo número pero como valor positivo.

[solución](bloque-a-ej-1.py)

### Bloque A - Ejercicio 2
Función distancia como “lambda”

* Escriba nuevamente la función de distancia euclidiana.
* Transforme la función a una función anónima (lambda).
* Su programa debe recibir las coordenadas por la entrada estándar y luego llamar a la función anónima.
* La función anónima debe retornar la distancia euclidiana (presente el resultado por la salida estándar).

[solución](bloque-a-ej-2.py)

### Bloque A - Ejercicio 3
Dígito verificador en un RUT

* Escriba una función lambda que retorne el dígito verificador de un RUT.
* La lambda debe recibir como parámetro un RUT sin dígito verificador y retornar este último.
* Revise el algoritmo para dígito verificador en: https://es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario (sección “Procedimiento para obtener el dígito verificador”.

[solución](bloque-a-ej-3.py)

### Bloque B - Ejercicio 1
Determinar el mayor valor en una lista

* Escriba un programa que reciba una lista y permita determinar el valor mayor.
* Debe usar una operación tipo “reduce()” para realizar las comparaciones.
* El programa debe imprimir por pantalla el valor mayor de la lista.

[solución](bloque-b-ej-1.py)

### Bloque B - Ejercicio 2
Viento registrado en estaciones de monitoreo
* Cree un programa que solicite el nombre de una estación de monitoreo y los vientos registrados (nudos) en las últimas 5, 10, y 15 horas.
* Almacene esta información en la memoria principal usando diccionarios y listas.
* Su programa debe crear un nuevo diccionario con los vientos registrados en kilómetros por hora.
* Además, el programa debe mostrar por la salida estándar el nombre de la estación y los vientos registrados (convertidos a kilómetros por hora).
* Debe usar operación map().
* Tip: los vientos en una zona calmada están entre los 3 y 10 nudos.

[solución](bloque-b-ej-2.py)

### Bloque B - Ejercicio 2
Viento registrado en estaciones de monitoreo
* Modifique el programa anterior para mostrar por pantalla los vientos que sobrepasan los 20 kilómetros por hora.
* Utilice una operación filter() para complementar el ejercicio anterior de tal manera que pueda dar cumplimiento a los requisitos de este ejercicio.

[solución](bloque-b-ej-3.py)