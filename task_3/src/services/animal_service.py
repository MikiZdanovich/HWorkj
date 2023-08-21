from typing import List

from task_3.data.models.animal import Animal
from task_3.src.helpers.api_client import HttpClient


class AnimalAPIService(HttpClient):
    def __init__(self):
        super().__init__("https://api.api-ninjas.com/v1/")

    def fetch_animals_by_name(self, name: str) -> List[Animal]:
        animals_data = self.get(f"animals?name={name}")
        return [Animal(**animal) for animal in animals_data]
