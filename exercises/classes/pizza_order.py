"""Instantoating A Class."""


from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("Large", 10, True)  # CONSTUCTOR

sals_pizza: Pizza = Pizza("Medium", 5, False)


def price(input_pizza: Pizza) -> float:
    """Give cost of a Pizza."""
    if input_pizza.size == "Large":
        price: float = 6.25
    if input_pizza.size == "Medium":
        price: float = 5.00
    if input_pizza.size == "Small":
        price: float = 4.50
    price += .75 * input_pizza.toppings 
    if input_pizza.glutenfree:
        price += 1.00
    return price


print(sals_pizza.price())