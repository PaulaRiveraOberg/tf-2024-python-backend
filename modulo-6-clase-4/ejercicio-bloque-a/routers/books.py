from typing import List

from fastapi import APIRouter, Depends, HTTPException
from models.books import BookSearch, Libro, Review, ReviewCreate
from models.users import Usuario
from sqlmodel import Session, select
from utils.auth import get_current_user
from utils.db import get_session

router = APIRouter()


# Rutas para libros
@router.post("/libros/", response_model=Libro)
async def crear_libro(
    libro: Libro,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_user),
):
    # Verificar si el ISBN ya existe
    existing = session.get(Libro, libro.isbn)
    if existing:
        raise HTTPException(status_code=400, detail="El ISBN ya existe")

    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro


@router.post("/libros/buscar", response_model=List[Libro])
async def buscar_libros(
    search: BookSearch,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_user),
):
    query = select(Libro)

    if search.isbn:
        query = query.where(Libro.isbn == search.isbn)
    if search.nombre:
        query = query.where(Libro.nombre.ilike(f"%{search.nombre}%"))
    if search.estrellas or search.estrellas_min:
        # Construir la subconsulta para los reviews
        review_query = select(Review.isbn)
        if search.estrellas:
            review_query = review_query.where(Review.estrellas == search.estrellas)
        if search.estrellas_min:
            review_query = review_query.where(Review.estrellas >= search.estrellas_min)

        # Filtrar libros por los ISBNs que tienen reviews que cumplen el criterio
        query = query.where(Libro.isbn.in_(review_query))

    return session.exec(query).all()


# Rutas para reviews
@router.post("/reviews/", response_model=Review)
async def crear_review(
    review: ReviewCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_user),
):
    # Verificar si el libro existe
    libro = session.get(Libro, review.isbn)
    if not libro:
        raise HTTPException(status_code=404, detail="ISBN no encontrado")

    # Verificar si el usuario ya ha hecho una reseña de este libro
    existing_review = session.exec(
        select(Review).where(
            Review.isbn == review.isbn, Review.usuario == current_user.username
        )
    ).first()
    if existing_review:
        raise HTTPException(
            status_code=400, detail="Ya has hecho una reseña de este libro"
        )

    # Crear el review con el usuario actual
    db_review = Review(**review.model_dump(), usuario=current_user.username)

    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review
