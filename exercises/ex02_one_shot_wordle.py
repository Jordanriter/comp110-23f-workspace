"""One Shot Wordle!"""

__author__: "730388067"

word: str = "python"
word_length = len(word)
guess: str = input(f"What is your {word_length}-letter guess?")
correct_guess: str = "Woo! You got it!"
wrong_guess: str = "Not quite. Play again soon!"

white_box: chr = "\U00002B1C"
green_box: chr = "\U0001F7E9"
yellow_box: chr = "\U0001F7E8"

index: int = 0
emoji: str = ""

while len(guess) > word_length or len(guess) < word_length: 
    guess: str = input(f"That was not {word_length} letters! Try again:")
    if len(guess) == word_length:
        continue

while index < word_length:
    if guess[index] in word[index]:
        emoji += green_box
    else: 
        if guess[index] in word:
            emoji += yellow_box
        else: 
            emoji += white_box
    index += 1

if guess == word:
    print(emoji)  
    print(f"{correct_guess}")
    exit()
if guess != word: 
    print(emoji)
    print(f"{wrong_guess}")
    exit()