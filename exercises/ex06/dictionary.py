"""Dictionary Exercise!"""

__author__ = "730388067"


def invert(start_dict: dict[str, str]) -> dict[str, str]:  # finished
    """Returns a dictionary where the value and key are switched from the originial dictionary entered."""
    inverted = {}
    for key, value in start_dict.items():
        if value in inverted:
            raise KeyError    
        inverted[value] = key
    return inverted


def favorite_color(fav_colors: dict[str, str]) -> str:  # finished
    """Returns the most poular color in a dictionary."""
    count = {}
    max_count = 0
    favorite_color = ""
    
    for name, color in fav_colors.items():
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
        if count[color] > max_count:
            max_count = count[color]
            favorite_color = color
        if max_count == 1 and len(fav_colors) > 1:
            favorite_color = "None"
    return favorite_color


def count(list: list[str]) -> dict[str, int]:  # finished
    """Returns a dictionary when the value is the amount of times a word appears in a list."""
    count: dict[str, int] = {}
    index = 0
    while index < len(list):
        item = list[index]
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
        index += 1
    return count


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:  # finished
    """Returns a dictionary where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    result: dict[str, list[str]] = {}
    for word in word_list:  
        initial_letter = word[0].lower()
        if initial_letter not in result:
            result[initial_letter] = []
        result[initial_letter].append(word)
    return result


def update_attendance(attendance: dict[str, list[str]], day_of_week: str, name: str) -> dict[str, list[str]]:  # finised
    """Returns an updated version of a dictionary."""
    if day_of_week in attendance:
        if name not in attendance[day_of_week]:
            attendance[day_of_week].append(name)
    else:
        attendance[day_of_week] = [name]
    return attendance