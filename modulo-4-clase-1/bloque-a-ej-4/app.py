# app.py
from views import View
from server import start_server

# Definimos un diccionario de rutas para mapear rutas URL a vistas específicas
ROUTES = {
    "/": View(),  # La ruta raíz se asocia con HelloView
}

def route_request(path):
    # Buscar la vista asociada a la ruta; si no se encuentra, devolver None
    view = ROUTES.get(path)
    if view:
        return view.get_response()
    else:
        return "404 Not Found"  # Respuesta de error si la ruta no existe

if __name__ == "__main__":
    # Iniciar el servidor en el puerto 8000
    start_server(port=8000, route_handler=route_request)