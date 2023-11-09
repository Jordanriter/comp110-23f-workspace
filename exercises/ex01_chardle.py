"""Chardle Exercise!"""

__author__ = "730388067"

word_input: str = input("Enter a 5-character word: ")
if len(word_input) > 5:
    print("Error: Word must contain 5 characters")
    quit()
if len(word_input) < 5:
    print("Error: Word must contain 5 characters")
    quit()
else:
    character_input: str = input("Enter a single character: ")
    if len(character_input) > 1:
        print("Error: Character must be a single character")
        quit()
    if len(character_input) < 1:
        print("Error: Character must be a single character")
        quit()
    else:
        print("Searching for " + character_input + " in " + word_input)


if character_input == word_input[0]:
    print(character_input + " found at index" + " 0")
if character_input == word_input[1]:
    print(character_input + " found at index" + " 1")
if character_input == word_input[2]:
    print(character_input + " found at index" + " 2")
if character_input == word_input[3]:
    print(character_input + " found at index" + " 3")
if character_input == word_input[4]:
    print(character_input + " found at index" + " 4")

count: int = 0
if character_input == word_input[0]:
    count = count + 1 
if character_input == word_input[1]:
    count = count + 1    
if character_input == word_input[2]:
    count = count + 1   
if character_input == word_input[3]:
    count = count + 1     
if character_input == word_input[4]:
    count = count + 1   

if count == 1: 
    print(str(count) + " instance of " + character_input + " found in " + word_input)
if count == 2: 
    print(str(count) + " instances of " + character_input + " found in " + word_input)
if count == 3: 
    print(str(count) + " instances of " + character_input + " found in " + word_input)
if count == 4: 
    print(str(count) + " instances of " + character_input + " found in " + word_input) 
if count == 5: 
    print(str(count) + " instances of " + character_input + " found in " + word_input)     
if count == 0:
    print("No instances of " + character_input + " found in " + word_input)