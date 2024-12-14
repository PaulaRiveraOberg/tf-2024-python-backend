import requests
from pprint import pprint


class Swapi:
    def __init__(self):
        self.base_url = 'https://swapi.dev/api/'

    def get_personajes(self, page=1):
        url = f"{self.base_url}people/?page={page}"
        try:
            response = requests.get(url)
            return response.json()['results']
        except requests.exceptions.RequestException as e:
            print("Error al realizar el request", e)
            return None

    def get_planeta(self, planeta_id):
        url = f"{self.base_url}/planets/{planeta_id}"
        try:
            response = requests.get(url)
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error al realizar el request", e)
            return None


if __name__ == '__main__':
    swapi = Swapi()
    personajes = swapi.get_personajes()
    # pprint(personajes)

    luke = None
    for personaje in personajes:
        if personaje['name'] == 'Luke Skywalker':
            luke = personaje
    pprint(luke)

    if luke:
        planeta_natal_id = luke['homeworld'].split('/')[-2]
        planeta = swapi.get_planeta(planeta_natal_id)
        pprint(planeta)


def hola():
    mensaje = "hola"
    print(mensaje)

print(mensaje)
