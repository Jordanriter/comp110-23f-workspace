<<<<<<< HEAD
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
=======
"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        return None

    def bears_eating(self):
        return None
    
    def check_hunger(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
>>>>>>> b5354f6088e43388953f45c6f88a789e0d71f069
