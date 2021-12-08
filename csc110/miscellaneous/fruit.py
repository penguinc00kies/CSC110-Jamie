"""fruits"""

class Fruit:
    """a fruit class"""
    color: str
    edible: bool
    flavor: str

    def __init__(self, flavor: str):
        self.edible = True
        self.flavor = flavor

    def is_edible(self):
        return self.edible

    def set_color(self, color: str) -> str:
        raise NotImplementedError

class Grapes(Fruit):
    orbular: bool

    def __init__(self, flavor: str):
        Fruit.__init__(self, flavor)
        self.orbular = True

    def set_color(self, color: str) -> None:
        self.color = color
