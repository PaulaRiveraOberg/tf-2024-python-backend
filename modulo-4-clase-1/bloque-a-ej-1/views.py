# views.py

class View:
    """
    Vista simple que maneja la ruta raíz del servidor.
    Implementa un endpoint básico que devuelve un saludo.
    """

    def get_response(self):
        """
        Genera la respuesta HTTP para esta vista.
        
        Returns:
            str: Un mensaje de saludo "Hello, World!"
        """
        return "Hello, World!"