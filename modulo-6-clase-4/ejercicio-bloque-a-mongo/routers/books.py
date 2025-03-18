from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from models.books import BookSearch, Libro, Review, ReviewCreate
from models.users import Usuario
from pymongo import MongoClient
from utils.auth import get_current_user
from utils.database import get_database

router = APIRouter(prefix="/libros", tags=["libros"])


# Rutas para libros
@router.post("/", response_model=Libro, status_code=status.HTTP_201_CREATED)
async def create_book(
    libro: Libro,
    current_user: Usuario = Depends(get_current_user),
    db: MongoClient = Depends(get_database),
):
    # Verificar si el libro ya existe
    if db.libros.find_one({"isbn": libro.isbn}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El libro ya existe"
        )

    db.libros.insert_one(libro.to_mongo())
    return libro


@router.post("/buscar", response_model=List[Libro])
async def get_books(
    search: BookSearch = None,
    current_user: Usuario = Depends(get_current_user),
    db: MongoClient = Depends(get_database),
):
    query = {}

    if search:
        if search.isbn:
            query["isbn"] = search.isbn
        if search.nombre:
            query["nombre"] = {"$regex": search.nombre, "$options": "i"}

        if search.estrellas or search.estrellas_min:
            pipeline = []
            match_stage = {"$match": query}

            pipeline.append(match_stage)
            pipeline.append(
                {
                    "$lookup": {
                        "from": "reviews",
                        "localField": "isbn",
                        "foreignField": "isbn",
                        "as": "reviews",
                    }
                }
            )

            pipeline.append(
                {"$addFields": {"promedio_estrellas": {"$avg": "$reviews.estrellas"}}}
            )

            if search.estrellas:
                pipeline.append({"$match": {"promedio_estrellas": search.estrellas}})
            elif search.estrellas_min:
                pipeline.append(
                    {"$match": {"promedio_estrellas": {"$gte": search.estrellas_min}}}
                )

            libros = list(db.libros.aggregate(pipeline))
            return [Libro.from_mongo(libro) for libro in libros]

    libros = list(db.libros.find(query))
    return [Libro.from_mongo(libro) for libro in libros]


@router.get("/{isbn}", response_model=Libro)
async def get_book(
    isbn: str,
    current_user: Usuario = Depends(get_current_user),
    db: MongoClient = Depends(get_database),
):
    libro = db.libros.find_one({"isbn": isbn})

    if not libro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado"
        )

    return Libro.from_mongo(libro)


# Rutas para reviews
@router.post("/reviews/", response_model=Review)
async def create_review(
    review: ReviewCreate,
    current_user: Usuario = Depends(get_current_user),
    db: MongoClient = Depends(get_database),
):
    # Verificar si el libro existe
    if not db.libros.find_one({"isbn": review.isbn}):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado"
        )

    # Verificar si ya existe una review de este usuario para este libro
    if db.reviews.find_one({"isbn": review.isbn, "usuario": review.usuario}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una review de este usuario para este libro",
        )

    new_review = Review(
        isbn=review.isbn,
        usuario=review.usuario,
        comentario=review.comentario,
        estrellas=review.estrellas,
    )

    db.reviews.insert_one(new_review.to_mongo())
    return new_review


@router.get("/{isbn}/reviews", response_model=List[Review])
async def get_book_reviews(
    isbn: str,
    current_user: Usuario = Depends(get_current_user),
    db: MongoClient = Depends(get_database),
):
    db = get_database()

    # Verificar si el libro existe
    if not db.libros.find_one({"isbn": isbn}):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado"
        )

    reviews = list(db.reviews.find({"isbn": isbn}))
    return [Review.from_mongo(review) for review in reviews]
