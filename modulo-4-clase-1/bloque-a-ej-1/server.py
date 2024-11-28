# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de solicitudes HTTP que procesa las peticiones GET entrantes.
    Hereda de BaseHTTPRequestHandler para implementar un servidor HTTP básico.
    """

    def __init__(self, *args, route_handler=None, **kwargs):
        """
        Inicializa el manejador de solicitudes.

        Args:
            route_handler: Función que maneja el enrutamiento de las solicitudes
            *args: Argumentos posicionales adicionales
            **kwargs: Argumentos de palabra clave adicionales
        """
        self.route_handler = route_handler
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """
        Procesa las solicitudes GET entrantes.
        Obtiene la ruta de la solicitud y la pasa al manejador de rutas.
        Envía la respuesta correspondiente al cliente.
        """
        # Obtener la ruta de la solicitud
        path = self.path
        
        # Llamar al manejador de rutas para obtener la respuesta
        if self.route_handler:
            response = self.route_handler(path)
        else:
            response = "404 Not Found"
        
        # Configurar la respuesta HTTP
        self.send_response(200 if response != "404 Not Found" else 404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        
        # Enviar la respuesta al cliente
        self.wfile.write(response.encode("utf-8"))

def start_server(port=8000, route_handler=None):
    """
    Inicia el servidor HTTP en el puerto especificado.

    Args:
        port: Puerto en el que se ejecutará el servidor (por defecto 8000)
        route_handler: Función que maneja el enrutamiento de las solicitudes
    """
    # Crear una función para inicializar el servidor con un route_handler personalizado
    def handler(*args, **kwargs):
        RequestHandler(*args, route_handler=route_handler, **kwargs)

    # Configurar y ejecutar el servidor
    server_address = ('', port)
    httpd = HTTPServer(server_address, handler)
    print(f"Servidor corriendo en el puerto {port}...")
    httpd.serve_forever()