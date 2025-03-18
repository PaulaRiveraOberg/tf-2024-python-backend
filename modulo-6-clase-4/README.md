## Clase 4: Habilitando Seguridad (FastAPI)

### Estructura recomendada para proyectos FastAPI

Cuando el proyecto es de mayor escala, es recomendable separar las rutas en diferentes archivos y directorios. Para esto, podemos utilizar el siguiente patrón:

```bash
├── app
│ ├── __init__.py
│ ├── main.py
│ ├── dependencies.py
│ └── routers
│ │ ├── __init__.py
│ │ ├── books.py
│ │ └── users.py
│ └── internal
│ ├── __init__.py
│ └── admin.py
│ └── models
│ ├── __init__.py
│ └── users.py
│ └── utils
│ ├── __init__.py
│ └── auth.py
```

Para esto haremos uso de la función `include_router` que nos permite incluir los routers en el archivo principal.

```python
# main.py
from fastapi import FastAPI
from app.routers import books, users

app = FastAPI()

app.include_router(books.router)
app.include_router(users.router)
```

y en el archivo `books.py` y `users.py` tendremos los routers correspondientes.

```python
# routers/books.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
async def get_books():
    return [{"title": "Book 1"}, {"title": "Book 2"}]
```

### Encriptación mediante bcrypt

Bcrypt es una librería que nos permite encriptar contraseñas de manera segura. Para utilizarla, podemos instalarla mediante pip:

```bash
pip install bcrypt
```

y en el archivo `auth.py` tendremos la función para encriptar contraseñas.

```python
# utils/auth.py
import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
```

## Ejercicio A: Agregando autenticación (mejorada) a nuestras APIs

* Al trabajo anterior con FastAPI (caso librería + basic auth):
    * Reestructuremos el código de tal forma que sigamos la estructura mejorada para autenticación.
    * Utilicemos bcrypt para hashear y almacenar passwords en una base de datos MongoDB.

Se implementaron 2 soluciones, una de ella con bd Sqlite3 usando `sqlmodel` y la otra con bd mongo usando `pymongo`.
* Solución: [ejercicio-bloque-a](./ejercicio-bloque-a/README.md)
* Solución: [ejercicio-bloque-a-mongo](./ejercicio-bloque-a-mongo/README.md)