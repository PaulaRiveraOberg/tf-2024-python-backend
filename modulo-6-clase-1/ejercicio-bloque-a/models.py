from typing import Optional

from sqlalchemy import PrimaryKeyConstraint
from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):
    username: str = Field(primary_key=True)
    email: str = Field(unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)


class Libro(SQLModel, table=True):
    isbn: str = Field(primary_key=True)
    nombre: str
    autores: str
    editorial: str
    edicion: str
    año: int


class ReviewBase(SQLModel):
    isbn: str = Field(foreign_key="libro.isbn")
    comentario: str
    estrellas: int = Field(ge=1, le=5)


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase, table=True):
    usuario: str = Field(foreign_key="usuario.username")

    # Definir clave primaria compuesta
    __table_args__ = (
        PrimaryKeyConstraint("isbn", "usuario", name="pk_review_isbn_usuario"),
    )


class BookSearch(SQLModel):
    isbn: Optional[str] = None
    nombre: Optional[str] = None
    estrellas: Optional[int] = None
    estrellas_min: Optional[int] = None


class UsuarioCreate(SQLModel):
    username: str
    email: str
    password: str


class UsuarioResponse(SQLModel):
    username: str
    email: str
    is_active: bool
