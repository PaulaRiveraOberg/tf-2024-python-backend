from typing import Optional

from pydantic import BaseModel, Field


class Libro(BaseModel):
    isbn: str
    nombre: str
    autores: str
    editorial: str
    edicion: str
    año: int

    def to_mongo(self):
        return {
            "isbn": self.isbn,
            "nombre": self.nombre,
            "autores": self.autores,
            "editorial": self.editorial,
            "edicion": self.edicion,
            "año": self.año,
        }

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)


class ReviewBase(BaseModel):
    isbn: str
    comentario: str
    estrellas: int = Field(ge=1, le=5)


class ReviewCreate(ReviewBase):
    usuario: str


class Review(ReviewBase):
    usuario: str

    def to_mongo(self):
        return {
            "isbn": self.isbn,
            "usuario": self.usuario,
            "comentario": self.comentario,
            "estrellas": self.estrellas,
        }

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)


class BookSearch(BaseModel):
    isbn: Optional[str] = None
    nombre: Optional[str] = None
    estrellas: Optional[int] = None
    estrellas_min: Optional[int] = None
