from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Creamos la aplicación FastAPI
app = FastAPI()

@app.get("/libro/{nombre}/{autor}/{fecha}")
def obtener_libro(nombre: str, autor: str, fecha: str):
    """
    Endpoint que retorna los detalles de un libro en formato HTML
    
    Args:
        nombre (str): Título del libro
        autor (str): Nombre del autor del libro
        fecha (str): Fecha de publicación del libro
        
    Returns:
        HTMLResponse: Página HTML con los detalles del libro
    """
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Detalles del Libro</title>
        </head>
        <body>
            <h1>Detalles del Libro</h1>
            <p>Nombre: {nombre}</p>
            <p>Autor: {autor}</p> 
            <p>Fecha de Publicación: {fecha}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)
