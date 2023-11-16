"""Fish Class."""

__author__ = "730388067"


class Fish:
    """Class to represent fish in river."""

    def __init__(self, age: int = 0):
        """Represents fish."""
        self.age = age

    def one_day(self):
        """Increase the value of the age attribute by 1."""
        self.age += 1