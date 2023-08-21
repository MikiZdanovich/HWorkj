from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def sound(self):
        raise NotImplementedError("You should implement this method.")


class BaseMixin:
    def __init__(self):
        assert hasattr(self, "name"), "Object should have a 'name' attribute"


class Mammal(Animal):
    def sound(self):
        return f"I'm a {self.name}. And I am a Mammal."


class Fish(Animal):
    def sound(self):
        return f"I'm a {self.name}. And I am a Fish."


class WalkerMixin(BaseMixin):
    def walk(self):
        return f"{self.name} is walking."


class SwimmerMixin(BaseMixin):
    def swim(self):
        return f"{self.name} is swimming."
