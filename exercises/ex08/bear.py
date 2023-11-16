"""Bear Class."""

__author__ = "730388067"


class Bear:
    """Class to represent Bears in river."""
    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Represents bears by the river."""
        self.age = age
        self.hunger_score = hunger_score

    def one_day(self):
        """Increase the value of the age attribute by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish):
        """Update the Bear’s hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish
