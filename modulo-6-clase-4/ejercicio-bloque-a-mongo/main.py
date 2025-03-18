import uvicorn
from fastapi import FastAPI
from routers import books, users
from utils.database import setup_indexes

app = FastAPI(title="API de Libros y Reseñas")


# Configurar índices de MongoDB al iniciar la aplicación
@app.on_event("startup")
async def startup_event():
    setup_indexes()


app.include_router(books.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
