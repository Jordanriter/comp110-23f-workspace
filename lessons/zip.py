"""Combining two lists into a dictionary."""

__author__ = "730388067"


def zip(string_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list.""" 
    if len(string_list) != len(int_list):
        return {}
    if len(string_list) == 0:
        return {}
    if len(int_list) == 0:
        return {}
    result = {}
    for index in range(len(string_list)):
        result[string_list[index]] = int_list[index]
    return result


print(zip(["Happy", "Tuesday"], [1, 2]))
