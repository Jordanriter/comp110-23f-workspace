"""River Simulation."""

<<<<<<< HEAD
__author__ = "730388067"

from exercises.ex08.river import River


def main():
    """Main function."""
    my_river = River(num_fish=10, num_bears=2)
    my_river.view_river()
    my_river.one_river_week()
    my_river.view_river()
=======
from river import River


def main():
    my_river = River(num_fish=10, num_bears=2)
    my_river.view_river()
>>>>>>> a515408 (progress)


if __name__ == "__main__":
    main()
