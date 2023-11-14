"""Structured Wordle!"""

__author__ = "730388067"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Finding a match between a single character and all the chracters in a word."""
    assert len(character) == 1
    if character in word:
        return True
    else: 
        return False


def input_guess(len_wanted: int) -> str:
    """Seeing if the input matches the length of the secret word."""
    guess: str = input(f"Enter a {len_wanted} character word: ")
    while len(guess) > len_wanted or len(guess) < len_wanted:
        new_guess: str = input(f"That wasn't {len_wanted} chars! Try again: ")
        guess = new_guess
    return guess 


def emojified(guess: str, secret: str) -> str:
    """Matching characters to correspsonding emoji color."""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    index: int = 0
    emoji: str = ""
    while index < len(secret):
        if secret[index] == guess[index]:
            emoji += green_box
        else:     
            if contains_char(secret, guess[index]):
                emoji += yellow_box
            else: 
                emoji += white_box
        index = index + 1
    return emoji


def main() -> None:
    """Entry point of thr program!"""
    secret: str = "hello"
    word_length = len(secret)
    print("=== Turn 1/6 ===")
    guess = input_guess(word_length)
    print(emojified(guess, secret))
    tries_count: int = 2
    while (guess != secret):
        if (tries_count > 6):
            print("X/6 - Sorry, try again tomorrow!")
            break
        else:
            if (tries_count <= 6):
                print("=== " + "Turn " + (str(tries_count)) + "/" + "6" + " ===")
                guess = input_guess(word_length)
                print(emojified(guess, secret))
        tries_count += 1 
    if guess == secret:
        print("You won in " + str(tries_count - 1) + "/6 " + "turns!")


if __name__ == "__main__":
    main()