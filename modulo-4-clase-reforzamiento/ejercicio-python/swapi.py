import requests
from pprint import pprint

class Swapi:
    """
    Clase para consumir datos de la API de Star Wars
    """
    def __init__(self):
        self.base_url = "https://swapi.dev/api/"

    def get_personajes(self, page=1):
        url = f"{self.base_url}people/?page={page}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()["results"]
        except requests.exceptions.RequestException as e:
            print("Error al realizar la solicitud:", e)
            return None
        
    def get_planetas(self, page=1):
        url = f"{self.base_url}planets/?page={page}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()["results"]
        except requests.exceptions.RequestException as e:
            print("Error al realizar la solicitud:", e)
            return None
        
    def get_planeta(self, id):
        url = f"{self.base_url}planets/{id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error al realizar la solicitud:", e)
            return None

if __name__ == "__main__":
    swapi = Swapi()
    personajes = swapi.get_personajes()
    # buscar al personaje con el nombre "Luke Skywalker"
    luke = next((personaje for personaje in personajes if personaje["name"] == "Luke Skywalker"), None)
    pprint(luke)

    # obtener el id del planeta de Luke Skywalker
    # https://swapi.dev/api/planets/1/
    planeta_id = luke["homeworld"].split("/")[-2]
    planeta = swapi.get_planeta(planeta_id)
    pprint(planeta)