from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import Libro, Review, BookSearch
from typing import List
import re

# Inicializar FastAPI
app = FastAPI(title="API de Libros y Reseñas")

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['libreria']

# Rutas para libros
@app.post("/libros/", response_model=Libro)
async def crear_libro(libro: Libro):
    if db.libros.find_one({"isbn": libro.isbn}):
        raise HTTPException(status_code=400, detail="El ISBN ya existe")
    
    db.libros.insert_one(libro.model_dump())
    return libro

@app.get("/libros/buscar", response_model=List[Libro])
async def buscar_libros(search: BookSearch):
    query = {}
    if search.isbn:
        query["isbn"] = search.isbn
    if search.nombre:
        regex = re.compile(f".*{search.nombre}.*", re.IGNORECASE)
        query["nombre"] = regex
    if search.estrellas or search.estrellas_min:
        # Buscar los ISBNs que tienen las estrellas requeridas
        reviews_query = {}
        if search.estrellas:
            reviews_query["estrellas"] = search.estrellas
        if search.estrellas_min:
            reviews_query["estrellas"] = {"$gte": search.estrellas_min}
        # Obtener los ISBNs de los reviews que cumplen el criterio
        matching_isbns = [r["isbn"] for r in db.reviews.find(reviews_query)]
        if matching_isbns:
            query["isbn"] = {"$in": matching_isbns}
        else:
            # Si no hay reviews que cumplan, no debería haber resultados
            query["isbn"] = None
    libros = list(db.libros.find(query))
    return libros

# Rutas para reviews
@app.post("/reviews/", response_model=Review)
async def crear_review(review: Review):
    if not db.libros.find_one({"isbn": review.isbn}):
        raise HTTPException(status_code=404, detail="ISBN no encontrado")
    
    db.reviews.insert_one(review.model_dump())
    return review
