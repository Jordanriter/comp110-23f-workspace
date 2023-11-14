
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


print(max([-2, 0]))