"""Dictionary Test!"""

__author__ = "730388067"

from exercises.ex06.dictionary import invert, count, favorite_color, alphabetizer, update_attendance


def test_dict_length_3() -> None:  # use case
    """Testing on a length of three elements."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_longer_words() -> None:  # use case
    """Testing on dictionaries that contain more than one character."""
    assert invert({'cat': 'dog', 'horse': 'cow'}) == {'dog': 'cat', 'cow': 'horse'}


def test_empty_dict() -> None:  # edge case 
    """Testing on an empty list."""
    assert invert({}) == {}


def test_single_element() -> None:  # use case
    """Test a list with a single element."""
    assert count(['apple']) == {'apple': 1}


def test_multiple_elements_count() -> None:  # use case 
    """Test a list with multiple elements."""
    assert count(['apple', 'banana', 'apple', 'cherry', 'banana']) == {'apple': 2, 'banana': 2, 'cherry': 1}


def test_int_elements() -> None:  # edge case 
    """Testing with int instead of str."""
    assert count([1, 2, 3, 2, 1]) == {1: 2, 2: 2, 3: 1}


def test_empty_list() -> None:  # edge case 
    """Testing on an empty list."""
    assert count([]) == {}


def test_multiple_elements_fav_color() -> None:  # use case 
    """Testing multiple dictionary elements."""
    assert favorite_color({'susan': 'blue', 'jeff': 'green', 'brad': 'purple', 'jordan': 'purple', 'Andrew': 'purple'}) == 'purple' 


def test_one_color() -> None:  # use case 
    """Testing one dictionary element."""
    assert favorite_color({'susan': 'blue'}) == 'blue'


def test_no_fav_color() -> None:  # edge case 
    """Testing on no favorite color."""
    assert favorite_color({'susan': 'blue', 'jeff': 'green', 'brad': 'purple'}) == 'None'


def test_multiple_fav_color() -> None:  # edge case 
    """Testing on multiple favorite colors."""
    assert favorite_color({'susan': 'purple', 'jeff': 'purple', 'brad': 'red', 'jordan': 'red'}) == 'purple'


def test_longer_list() -> None:  # use case 
    """Testing long list of words."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def testing_one_elemet_list() -> None:  # use case
    """Testing a list length of one."""
    assert alphabetizer(['jordan']) == {'j': ['jordan']}


def testing_characters() -> None:  # edge case
    """Testing a list of characters."""
    assert alphabetizer(["c", "a", "b", "a", "b", "c"]) == {'c': ['c', 'c'], 'a': ['a', 'a'], 'b': ['b', 'b']}


def test_empty_dictionary() -> None:  # use case
    """Testing adding a person to an empty attendance dictionary."""
    attendance_log = update_attendance({}, "Monday", "Alice")
    assert attendance_log == {"Monday": ["Alice"]}


def test_adding_new_person() -> None:  # use case
    """Testing adding a person to an empty attendance dictionary."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]} 
    assert update_attendance(attendance_log, "Tuesday", "Vrinda") == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_empty_name() -> None:  # use case
    """Testing adding an empty name."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]} 
    assert update_attendance(attendance_log, "Monday", "") == {'Monday': ['Vrinda', 'Kaleb', ""], 'Tuesday': ['Alyssa']}


def test_no_repeat_names() -> None:  # use case
    """Testing adding an empty name."""
    attendance = {}
    update_attendance(attendance, "Monday", "Alice")
    update_attendance(attendance, "Monday", "Alice")
    assert attendance == {'Monday': ['Alice']}
