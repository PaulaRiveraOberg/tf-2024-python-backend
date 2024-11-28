# modelos.py
avisos = [
        {"fecha": "2024-11-06", "titulo": "Primer aviso", "autor": "Autor A"},
        {"fecha": "2024-11-07", "titulo": "Segundo aviso", "autor": "Autor B"},
        {"fecha": "2024-11-08", "titulo": "Tercer aviso", "autor": "Autor C"},
    ]

class Aviso:
    def all(self):
        """Retorna todos los avisos como una lista de diccionarios."""
        return avisos