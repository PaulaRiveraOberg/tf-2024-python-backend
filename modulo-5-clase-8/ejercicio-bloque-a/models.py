from pydantic import BaseModel, Field

class Libro(BaseModel):
    isbn: str
    nombre: str
    autores: str
    editorial: str
    edicion: str
    año: int

class Review(BaseModel):
    isbn: str
    usuario: str
    comentario: str
    estrellas: int = Field(ge=1, le=5)


class BookSearch(BaseModel):
    isbn: str | None = None
    nombre: str | None = None
    estrellas: int | None = None
    estrellas_min: int | None = None
    