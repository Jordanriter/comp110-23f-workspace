"""List Utility Functions!"""

__author__ = "730388067"


def all(number_list: list[int], number: int) -> bool:
    """Return bool indicating wheter or not all ints in list are same given int.""" 
    index: int = 0
    while index < len(number_list) and number == number_list[index]: 
        index += 1
        if len(number_list) - 1 == index - 1 and number == number_list[index - 1]:
            return True
    else: 
        return False
    

def max(int_list: list[int]) -> int:
    """Returns the largest number in a list."""
    if len(int_list) == 0: 
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max_num = int_list[index]
    while index < len(int_list): 
        if int_list[index] > max_num: 
            max_num = int_list[index]
        index += 1
    return max_num
             

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines if all int of a list are the same."""
    if list_1 != list_2: 
        return False
    else: 
        return True