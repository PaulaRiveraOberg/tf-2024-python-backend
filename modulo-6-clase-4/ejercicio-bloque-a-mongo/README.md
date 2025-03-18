# API de Libros y Reseñas

## Instalación de dependencias

```bash
pip install fastapi pydantic uvicorn passlib bcrypt pymongo
```

## Estructura de directorios y archivos

```bash
├── routers
│ ├── __init__.py
│ ├── books.py
│ └── users.py
├── models
│ ├── __init__.py
│ ├── books.py
│ └── users.py
├── utils
│ ├── __init__.py
│ ├── auth.py
│ └── db.py
├── main.py
├── libreria.db
└── README.md
```

## Pruebas usando Curl

Crear un usuario

```bash
curl -X POST "http://localhost:8000/usuarios/" -H "Content-Type: application/json" -d '{"username": "usuario", "email": "usuario@example.com", "password": "contrasena123"}'
```

Listar usuarios

```bash
curl -X GET "http://localhost:8000/usuarios/"  -H "Content-Type: application/json" -u usuario:contrasena123
```

Crear un libro

```bash
curl -X POST http://localhost:8000/libros/ -H "Content-Type: application/json" -u usuario:contrasena123 -d '{"isbn": "1234567890", "nombre": "Libro de Prueba", "autores": "Autor 1, Autor 2", "editorial": "Editorial 1", "edicion": "1ra", "año": 2024}'
```

Buscar libros

```bash
curl -X POST "http://localhost:8000/libros/buscar" -u usuario:contrasena123 -H "Content-Type: application/json" -d '{"nombre": "Libro"}'
```

Crear una reseña

```bash
curl -X POST http://localhost:8000/libros/reviews/ -H "Content-Type: application/json" -u usuario:contrasena123 -d '{"isbn": "1234567890", "usuario": "Usuario 1", "comentario": "Comentario de Prueba", "estrellas": 5}'
```


