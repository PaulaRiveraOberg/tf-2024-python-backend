from fastapi import FastAPI, HTTPException
import books_service

# Creamos la aplicación FastAPI
app = FastAPI()

@app.get(
    "/book/{book_id}",
    responses={
        200: {"description": "Libro encontrado"},
        400: {"description": "ISBN no válido"},
        404: {"description": "Libro no encontrado"},
        500: {"description": "Error interno del servidor"},
    },
)
def get_book(book_id: str):
    try:
        book_data = books_service.get_book_basic_data(book_id)
        book_data["more data"] = f"http://localhost:8000/book/details/{book_id}"
        return book_data
    except ValueError:
        raise HTTPException(status_code=400, detail="ISBN no válido")
    except KeyError:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get(
    "/book/details/{book_id}",
    responses={
        200: {"description": "Detalles del libro encontrados"},
        400: {"description": "ISBN no válido"},
        404: {"description": "Detalles del libro no encontrados"},
        500: {"description": "Error interno del servidor"},
    },
)
def get_book_details(book_id: str):
    try:
        book_details = books_service.get_a_book_details(book_id)
        return {"isbn": book_id, "details": book_details}
    except ValueError:
        raise HTTPException(status_code=400, detail="ISBN no válido")
    except KeyError:
        raise HTTPException(status_code=404, detail="Detalles del libro no encontrados")
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

# probar endpoints  
# http://127.0.0.1:8000/book/19920043920-1
# http://127.0.0.1:8000/book/details/19920043920-1

# errores
# error 400
# http://127.0.0.1:8000/book/details/199200s-1
# http://127.0.0.1:8000/book/details/199200s-1

# error 404
# http://127.0.0.1:8000/book/19920043921-1
# http://127.0.0.1:8000/book/details/19920043921-1