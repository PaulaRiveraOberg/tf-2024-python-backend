from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Creamos la aplicación FastAPI
app = FastAPI()

@app.get("/libro/{nombre}/{autor}/{fecha}")
def obtener_libro(nombre: str, autor: str, fecha: str):
    """
    Endpoint que retorna los detalles de un libro en formato JSON
    
    Args:
        nombre (str): Título del libro
        autor (str): Nombre del autor del libro
        fecha (str): Fecha de publicación del libro
        
    Returns:
        dict: Diccionario con los detalles del libro incluyendo nombre, autor y fecha
    """
    return {"nombre": nombre, "autor": autor, "fecha": fecha}
