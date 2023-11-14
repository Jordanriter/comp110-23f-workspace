"""Practice Writing Functions."""


def mimic_letter(my_words: str, letter_indx: int) -> str:
    """Give the string my_words, outputs the same string."""
    if letter_indx >= len(my_words):
        return "index too high"
    else:
        char = my_words[letter_indx] 
        return char


print(mimic_letter("howdy", 5))
