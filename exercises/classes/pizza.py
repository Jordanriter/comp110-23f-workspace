"""Defining a Class."""


class Pizza:

    # Attributes

    size: str
    toppings: int
    glutenfree: bool

    def __init__(self, inp_size: str, toppings: int, glutenfree: bool) -> None:
        """Size input."""
        self.size = inp_size
        self.toppings = toppings
        self.glutenfree = glutenfree

    def price(self) -> float:
        """Give cost of a Pizza."""
        if self.size == "Large":
            price: float = 6.25
        if self.size == "Medium":
            price: float = 5.00
        if self.size == "Small":
            price: float = 4.50
        price += .75 * self.toppings 
        if self.glutenfree:
            price += 1.00
        return price
    
    def __str__(self) -> str:
        """Returns string."""
        pizza_info: str = f"Pizza Order: size {self.size}, toppings: {self.toppings}, GF: {self.glutenfree}"
        return pizza_info
        

my_pizza = Pizza("Large", 10, False)
sals_pizza = Pizza("small", 4, True)

print(my_pizza)
print(sals_pizza)