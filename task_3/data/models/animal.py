from pydantic import BaseModel


class Animal(BaseModel):
    name: str
    species: str
    speed: str
    lifespan: str
    weight: str
