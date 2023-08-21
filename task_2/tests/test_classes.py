from task_2.base import (
    Fish,
    Mammal,
)
from task_2.main import (
    Catfish,
    Mouse,
    Otter,
    Whale,
)


class TestUnit:
    def test_mammal(self):
        mammal = Mammal("Mammal", "Mammal")
        assert mammal.sound() == "I'm a Mammal. And I am a Mammal."

    def test_fish(self):
        fish = Fish("Fish", "Fish")
        assert fish.sound() == "I'm a Fish. And I am a Fish."

    def test_mouse(self):
        mouse = Mouse("Mouse", "Rodent")
        assert mouse.sound() == "I'm a Mouse. And I am a Mammal."
        assert mouse.walk() == "Mouse is walking."

    def test_whale(self):
        whale = Whale("Whale", "Cetacea")
        assert whale.sound() == "I'm a Whale. And I am a Mammal."
        assert whale.swim() == "Whale is swimming."

    def test_catfish(self):
        catfish = Catfish("Catfish", "Siluriformes")
        assert catfish.sound() == "I'm a Catfish. And I am a Fish."
        assert catfish.swim() == "Catfish is swimming."

    def test_otter(self):
        otter = Otter("Otter", "Mustelidae")
        assert otter.sound() == "I'm a Otter. And I am a Mammal."
        assert otter.walk() == "Otter is walking."
        assert otter.swim() == "Otter is swimming."
