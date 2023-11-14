"""Loop Practice."""

from random import randint

guess: int = int(input("Guess a number between 1 and 10: "))
secret: int = randint(1, 10)

while guess != secret: 
    print("Wrong!")
    guess = int(input("guess again: "))

if guess == secret:
    print("you got it")