"""Summing the elements of a list using different loops."""

__author__ = "730388067"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats."""
    index: int = 0 
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats."""
    sum: float = 0.0
    for index in vals:
        sum += index
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats."""
    sum: float = 0.0
    for index in range(len(vals)): 
        sum += vals[index]
    return sum