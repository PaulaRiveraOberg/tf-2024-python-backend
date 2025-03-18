from fastapi import FastAPI
from routers import books, users

app = FastAPI(title="API de Libros y Reseñas")

app.include_router(books.router)
app.include_router(users.router)
