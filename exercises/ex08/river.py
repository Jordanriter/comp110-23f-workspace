"""River Class."""


from bear import Bear  
from fish import Fish  


class River:
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish, num_bears):
        """Initialize self.fish to contain num_fish many Fish."""
        """Initialize self.bears to contain num_bears many Bears."""
        """Initialize self.day to be 0."""
        self.day = 0
        self.fish = [Fish(age=1) for _ in range(num_fish)]  
        self.bears = [Bear(age=2, hunger_score=0) for _ in range(num_bears)] 

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")