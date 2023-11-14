"""Bear Class."""


class Bear:
    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Represents bears by the river."""
        self.age = age
        self.hunger_score = hunger_score