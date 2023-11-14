"""practice for wordle!"""


def contains_char(word: str, character: str) -> bool:
    """Finding a match between a single character and all the chracters in a word."""
    assert len(character) == 1
    if character in word:
        return True
    else: 
        return False


def emojified(guess: str, secret: str) -> str:
    """Matching characters to correspsonding emoji color."""
    assert len(guess) == len(secret)
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


def input_guess_(len_wanted: int) -> str:
    guess: str = input(f"Enter a {len_wanted} character word:")
    while len(guess) != len_wanted:
        guess: str = input(f"That wasn't {len_wanted} characters! Try again:") 
    return guess
        
    
print(input_guess_(5))