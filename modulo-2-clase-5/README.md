# Modulo 2 - Clase 5: Manejo de Excepciones y Debugging

## Ejercicios

### Bloque A - Ejercicio 1

Entendiendo las excepciones
* Investigue posibles excepciones aplicables a las listas y diccionarios.
* Escriba un código que obligue la emergencia de una excepción y captúrela con los bloques try/except. Imprima por pantalla el nombre de la excepción y el mensaje.
* Tip: para identificar las excepciones que aplican a determinados tipos de datos usted siempre debe recurrir a la documentación oficial.

[solución](bloque-a-ej-1.py)

### Bloque A - Ejercicio 2
Mejorando el código con manejo de excepciones
* Utilice el código creado en la clase anterior (el problema de la distancia geodésica) y mejórelo con manejo de excepciones.
* Investigue los valores posibles de las latitudes y longitudes.
* Incorpore excepciones de tipo ValueError a ser lanzadas cuando se intente crear un objeto con valores de latitude y/o longitude erróneas.
* Pruebe su código forzando la aparición de estas excepciones y capturándolas para mostrar el resultado erróneo.

[solución](bloque-a-ej-2.py)

### Bloque B - Ejercicio 1
Base de ejercicio
* Incorpore el siguiente código en su IDE y estúdielo.
  ```python
  FIN = False
  registro_llamado = {"frecuencia": None, "motivo": None, "fecha": None}
  listado_llamados = []
  while not FIN:
    frecuencia = input("Ingrese frecuencia: ")
    if frecuencia == "FIN":
      FIN = True
    else:
      motivo = input("Ingrese motivo: ")
      fecha = input("Ingrese fecha: ")
      registro_llamado["frecuencia"] = frecuencia
      registro_llamado["motivo"] = motivo
      registro_llamado["fecha"] = fecha
      listado_llamados.append(registro_llamado)
  print(listado_llamados)
  ```

### Bloque B - Ejercicio 2

Debugging de código
* Una vez que haya estudiado y ejecutado el código, identifique el principal resultado erróneo.
* Identifique líneas que sean de su interés, actívelas como puntos de suspensión (breakpoint) y ejecute un proceso de debugging.
* Discuta el problema subyacente y corrija el código para que este funcione adecuadamente.

[solución](bloque-b-ej-2.py)