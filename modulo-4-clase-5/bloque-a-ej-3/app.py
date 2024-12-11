from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

# Creamos la aplicación FastAPI
app = FastAPI()

class BusquedaLibro(BaseModel):
    """
    Modelo de datos para la búsqueda de libros por rango de fechas
    
    Attributes:
        fecha_inicial (date): Fecha inicial del rango de búsqueda
        fecha_final (date): Fecha final del rango de búsqueda
    """
    fecha_inicial: date
    fecha_final: date

@app.post("/libro/buscar")
def buscar_libros(busqueda: BusquedaLibro):
    """
    Endpoint que busca libros dentro de un rango de fechas especificado
    
    Args:
        busqueda (BusquedaLibro): Objeto con las fechas inicial y final para la búsqueda
        
    Returns:
        dict: Primer libro encontrado dentro del rango de fechas, incluyendo título, autor y fecha
        
    Raises:
        HTTPException: Si no se encuentra ningún libro en el rango de fechas especificado
    """
    # Lista de libros con fechas de publicación
    libros = [
        {"titulo": "Don Quijote", "autor": "Cervantes", "fecha": date(1605, 1, 1)},
        {"titulo": "Cien años de soledad", "autor": "García Márquez", "fecha": date(1967, 5, 30)},
        {"titulo": "El Aleph", "autor": "Borges", "fecha": date(1949, 6, 15)},
        {"titulo": "Rayuela", "autor": "Cortázar", "fecha": date(1963, 6, 28)}
    ]
    
    # Buscar el primer libro que esté entre las fechas indicadas
    libros_encontrados = []
    for libro in libros:
        if busqueda.fecha_inicial <= libro["fecha"] <= busqueda.fecha_final:
            libros_encontrados.append(libro)
            
    if len(libros_encontrados) == 0:
        raise HTTPException(status_code=404, detail="No se encontró ningún libro en ese rango de fechas")
    
    return libros_encontrados[0]