# Modulo 4 - Clase 5 Rest y Servicios FastAPI

## Requisitos

Primero activaremos el entorno virtual e instalaremos `fastapi`, junto con `uvicorn` y `pydantic`.

```bash
# activar entorno virtual en osx y linux
source .venv/bin/activate
# para activar en windows
.\.venv\Scripts\activate
# instalar fastapi, uvicorn y pydantic
pip install fastapi uvicorn pydantic
```

Para crear una applicación basica creamos el archivo `app.py` con el siguiente contenido:

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

Para ejecutar el servidor, usamos el siguiente comando:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000 --reload
```

## Ejercicios

### Bloque A - Ejercicio 1

Crear un endpoint simple (GET)

1. Escriba el código para implementar un endpoint de tipo GET que reciba tres
parámetros (nombre del libro, autor, fecha de publicación) de tipo “path”.
2. Su endpoint debe responder con con HTML-compatible presentando el nombre del
libro, autor, fecha de publicación.


Soluciones:
* [solución](bloque-a-ej-1/)

### Bloque A - Ejercicio 2

Crear un endpoint simple (GET)

1. Modifique el código anterior para que la respuesta sea JSON compatible.


Soluciones:
* [solución](bloque-a-ej-2/)

### Bloque A - Ejercicio 3

Crear un endpoint simple (POST)

1. Escriba el código para implementar un endpoint POST que permita recibir un objeto `búsqueda` con los siguientes elementos: fecha inicial de publicación, fecha final de publicación.
2. Por ahora, su código debe crear una lista de libros con fechas de publicación.
3. El endpoint debe responder con el primer libro que se encuentre entre las fechas de inicio y fecha final.
4. Si no se encuentra un libro, debe responder con status code 404: not found.
5. Discuta: ¿por qué la búsquesa se implementa como POST y no GET?

Soluciones:
* [solución](bloque-a-ej-3/)

### Bloque B - Ejercicio 1

Endpoint GET para los datos de un paciente.

1. Con el código ya revisado, cree un nuevo endpoint de tipo GET para responder con un HTML con los datos de un paciente.. 

Soluciones:
* [solución](bloque-b-ej-1/)

### Bloque B - Ejercicio 2

Endpoint GET para los datos de un paciente.

1. Modifique el endpoint anterior para que responda con un enlace hacia la representación en XML.
2. ¡Usted debe probar que su enlace responda con un XML!

Soluciones:
* [solución](bloque-b-ej-2/)

## Caso

* [caso](caso/)
