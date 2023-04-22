import requests

from enum import Enum


class Endpoints(Enum):
    CATS = "https://api.thecatapi.com/v1/images/search"
    DOGS = "https://api.thedogapi.com/v1/images/search"


def get_random_animal_image_url(endpoint: Endpoints) -> str:
    response = requests.get(endpoint.value).json()
    return response[0]["url"]
