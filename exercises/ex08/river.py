"""River Simulation."""

from bear import Bear 
from fish import Fish  


class River:
    """Class to represent river."""
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """Representing thr river."""
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear(age=0, hunger_score=0) for _ in range(num_bears)]