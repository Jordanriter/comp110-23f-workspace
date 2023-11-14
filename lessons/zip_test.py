"""Test my zip function."""

__author__ = "730388067"

from lessons.zip import zip


def test_list_length_1() -> None:
    """Testing on a length of one element."""
    assert zip(["Happy"], [1]) == {"Happy": 1}


def test_list_length_3() -> None:
    """Testing on a length of three elements."""
    assert zip(["Happy", "Tuesday", "Yall"], [1, 2, 3]) == {"Happy": 1, "Tuesday": 2, "Yall": 3}


def test_list_length_2() -> None:
    """Testing on a list with two elements."""
    assert zip(["Happy", "Tuesday"], [1, 2]) == {"Happy": 1, "Tuesday": 2}


def test_of_uneven_length() -> None:
    """Testing list of uneven length."""
    assert zip(["Happy", "Tuesday", "Yall"], [1, 2]) == {}