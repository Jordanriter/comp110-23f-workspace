"""Guess my number!"""

my_number_string: str = input("Guess a number: ")
my_number: 10

if my_number_string == 10: 
    print(str(my_number_string) + " is correct")
else: 
    print(str(my_number_string) + " is incorrect")