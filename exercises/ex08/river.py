"""River Class."""

__author__ = "730388067"

from exercises.ex08.bear import Bear  
from exercises.ex08.fish import Fish  


class River:
    """Class to represent River."""
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish, num_bears):
        """Initialize self.fish to contain num_fish many Fish."""
        """Initialize self.bears to contain num_bears many Bears."""
        """Initialize self.day to be 0."""
        self.day = 0
        self.fish = [Fish(0) for _ in range(num_fish)]  
        self.bears = [Bear(0, 0) for _ in range(num_bears)] 

    def view_river(self):
        """Print the river status out."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Calls one_day in Fish and Bears."""
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.day += 1

    def one_river_week(self):
        """Call one_river_day() seven times."""
        days = 1
        while days <= 7:
            self.one_river_day()
            days += 1

    def check_ages(self):
        """A fish age > 3 removed from fish."""
        """A bear age is > 5 it should be removed from bears."""
        fish_kept = []
        for fish in self.fish:
            if fish.age <= 3:
                fish_kept.append(fish)
        self.fish = fish_kept

        bears_kept = []
        for bear in self.bears:
            if bear.age <= 5:
                bears_kept.append(bear)
        self.bears = bears_kept

    def remove_fish(self, amount: int):        
        """Remove amount of Fish from the front of the list."""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """Removing 3 Fish from the river using the remove_fish method."""
        """Calling eat() each time a Bear eats."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Remove Bears with hunger_score < 0."""
        surviving_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving_bears

    def repopulate_bears(self):
        """Each pair of bears will produce 1 offspring."""
        new_bears = []
        for _ in range(len(self.bears) // 2):
            new_bear = Bear(age=0, hunger_score=0)
            new_bears.append(new_bear)
        self.bears.append(new_bears)

    def repopulate_fish(self):
        """Each pair of fish will produce 4 offspring."""
        new_fish = []
        for _ in range(len(self.fish) // 2):
            for _ in range(4):
                new_fish.append(Fish(age=0))
        self.fish.extend(new_fish)