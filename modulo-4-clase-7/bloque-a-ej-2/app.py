from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import books_service

# Creamos la aplicación FastAPI
app = FastAPI()

responses = {
    200: {"description": "Libro encontrado"},
    400: {"description": "ISBN no válido"},
    404: {"description": "Libro no encontrado"},
    500: {"description": "Error interno del servidor"},
}

class BookUpdate(BaseModel):
    name: str
    publisher: str
    year: str
    details: str

@app.get("/book/{book_id}", responses=responses)
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

@app.get("/book/details/{book_id}", responses=responses)
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

@app.put("/book/{book_id}", responses=responses)
def update_book(book_id: str, book: BookUpdate):
    try:
        updated_book = books_service.update_book(book_id, book.model_dump(exclude_none=True))
        return updated_book
    except ValueError as e:
        raise HTTPException(status_code=400, detail="ISBN no válido")
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"Libro no encontrado: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.delete("/book/{book_id}", responses=responses)
def delete_book(book_id: str):
    try:
        books_service.delete_book(book_id)
        return {"mensaje": f"Libro con ISBN {book_id} eliminado exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail="ISBN no válido")
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"Libro no encontrado: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

# probar endpoints  
# http://127.0.0.1:8000/book/19920043920-1
# http://127.0.0.1:8000/book/details/19920043920-1

# delete
# curl -X DELETE http://127.0.0.1:8000/book/19920043920-1

# ver
# curl http://127.0.0.1:8000/book/19920043920-1
# modificar
# curl -X PUT -H "Content-Type: application/json" -d '{"name": "Backend Software Engineering", "publisher": "Talento Futuro", "year": "2025", "details": "This best-selling book on backend software development in the industry standard for guiding the development of such applications"}' http://127.0.0.1:8000/book/19920043920-1