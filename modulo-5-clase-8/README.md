## Clase 8: Bases de Datos NoSQL (MongoDB)

## Instalación de MongoDB

En windows podemos instalar MongoDB y el cliente de MongoDB Compass descargando el instalador desde el sitio de MongoDB:
* [MongoDB](https://www.mongodb.com/try/download/community)
* [Compass](https://www.mongodb.com/try/download/compass)

En OSX podemos instalar MongoDB y el cliente de MongoDB Compass con Homebrew:

```bash
brew install mongodb-community
brew install mongodb-compass
```

Para acceder a MongoDB desde python utilizamos el paquete `pymongo`:

```bash
pip install pymongo
```

Conectamos a MongoDB:

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['customers']

data = collection.insert_one({'name': 'John', 'surname': 'Doe', 'age': 30})
print(data.inserted_id)
```

## Ejercicio A: Diseñando una API “NoSQL”
* Diseñe una API que permita:
    * Guardar un libro (ISBN, nombre, autores (por ahora como string), editorial, edición, año).
    * Guardar un review (ISBN, nombre del usuario, comentario, número de estrellas de 1 a 5).
    * Encontrar un libro por ISBN, texto en el nombre, un número predefinido de estrellas, un número mayor de estrellas.
* Pruebe funcionalmente su API con Postman.
* OPCIONAL: Diseñe al menos 2 pruebas de performance con Apache JMeter.