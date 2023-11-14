<<<<<<< HEAD
"""Bear Class."""

__author__ = "730388067"

=======
<<<<<<< HEAD
"""File to define Bear class"""
>>>>>>> 5bdd356 (Progress in 110)

class Bear:
    """Class to represent Bears in river."""
    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Represents bears by the river."""
        self.age = age
        self.hunger_score = hunger_score

    def one_day(self):
<<<<<<< HEAD
        """Increase the value of the age attribute by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish):
        """Update the Bear’s hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish
=======
        return None
=======
"""River Simulation."""


class Bear:
    def __init__(self, age=0, hunger_score=0):
        """Class to represent bear."""
        self.age = age
        self.hunger_score = hunger_score
>>>>>>> 82a71f9 (Progress in 110)
>>>>>>> 5bdd356 (Progress in 110)
