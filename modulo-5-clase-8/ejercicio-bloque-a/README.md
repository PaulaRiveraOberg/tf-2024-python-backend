# API de Libros y Reseñas

## Instalación

```bash
pip install fastapi pymongo pydantic uvicorn
```

## Ejecución

```bash
uvicorn main:app --reload
```

## Pruebas usando Curl

Crear un libro

```bash
curl -X POST http://localhost:8000/libros/ -H "Content-Type: application/json" -d '{"isbn": "1234567890", "nombre": "Libro de Prueba", "autores": "Autor 1, Autor 2", "editorial": "Editorial 1", "edicion": "1ra", "año": 2024}'
```

Buscar libros

```bash
curl -X POST "http://localhost:8000/libros/buscar" -H "Content-Type: application/json" -d '{"nombre": "Libro"}'
```

Crear una reseña

```bash
curl -X POST http://localhost:8000/reviews/ -H "Content-Type: application/json" -d '{"isbn": "1234567890", "usuario": "Usuario 1", "comentario": "Comentario de Prueba", "estrellas": 5}'
```


