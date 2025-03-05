import re
import secrets
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import (
    BookSearch,
    Libro,
    Review,
    ReviewCreate,
    Usuario,
    UsuarioCreate,
    UsuarioResponse,
)
from passlib.context import CryptContext
from sqlmodel import Session, SQLModel, create_engine, select

# Inicializar FastAPI
app = FastAPI(title="API de Libros y Reseñas")

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./libreria.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear las tablas
SQLModel.metadata.create_all(engine)

# Configuración de seguridad
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Dependencia para obtener la sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session


# Funciones de autenticación
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security),
    session: Session = Depends(get_session),
) -> Usuario:
    user = session.get(Usuario, credentials.username)
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


# Rutas para usuarios
@app.post("/usuarios/", response_model=UsuarioResponse)
async def crear_usuario(
    usuario: UsuarioCreate, session: Session = Depends(get_session)
):
    # Verificar si el username ya existe
    if session.get(Usuario, usuario.username):
        raise HTTPException(status_code=400, detail="El username ya existe")

    # Verificar si el email ya existe
    existing_email = session.exec(
        select(Usuario).where(Usuario.email == usuario.email)
    ).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="El email ya existe")

    # Crear el usuario con la contraseña hasheada
    db_usuario = Usuario(
        username=usuario.username,
        email=usuario.email,
        hashed_password=get_password_hash(usuario.password),
        is_active=True,
    )

    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario


# Rutas para libros
@app.post("/libros/", response_model=Libro)
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


@app.post("/libros/buscar", response_model=List[Libro])
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
@app.post("/reviews/", response_model=Review)
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
