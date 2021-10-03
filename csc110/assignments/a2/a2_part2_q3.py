"""CSC110 Fall 2020 Assignment 2, Part 2: Conditional Execution

Instructions (READ THIS FIRST!)
===============================

This Python module contains your work for Part 2, Question 3. We have provided the functions
from the handout already, and you must NOT change these. Below them, we've provided one
sample (incomplete) unit test for each function. Your task is to complete these sample tests,
and then use the same format to create new ones to cover every possible execution path through
the three given functions.

You must use the provided structure for ALL unit tests. The only difference between your
tests should be which function is called, the argument values, and the expected return value.

Do not use hypothesis or property-based testing here.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""


###############################################################################
# The given functions (DO NOT CHANGE THESE)
###############################################################################
def mystery_3a(c1: str, c2: str, c3: str) -> int:
    """Function for question 3a."""
    if c1 == c2 and c1 == c3:
        return 1
    elif c1 == c2 and c1 != c3:
        return 2
    elif c2 == c3:
        return 3
    elif c1 == c3:
        return 4
    else:
        return 5


def mystery_3b(c1: int, c2: int, c3: int) -> int:
    """Function for question 3b."""
    if c1 >= c2:
        if c2 >= c3:
            return 1
        else:
            return 2
    else:
        if c2 <= c3:
            return 3
        else:
            return 4


def mystery_3c(c1: float, c2: float, c3: float) -> int:
    """Function for question 3c."""
    if c1 > 0:
        if c2 % 3 == 0:
            if c3 % c2 == 0:
                return 1
            else:
                return 2
        else:
            if c3 % c2 == 0:
                return 3
            else:
                return 4
    else:
        if c1 * c2 > 0:
            return 5
        elif c2 * c3 > 0:
            return 6
        elif c3 < 0:
            return 7
        else:
            return 8


###############################################################################
# The unit tests (do your work here)
###############################################################################
def test_mystery_3a_1() -> None:
    """Test mystery_3a for an expected return value of 1."""
    expected = 1
    actual = mystery_3a(..., ..., ...)  # TODO: fill in the arguments, then delete this TODO
    assert actual == expected


def test_mystery_3b_1() -> None:
    """Test mystery_3b for an expected return value of 1."""
    expected = 1
    actual = mystery_3b(..., ..., ...)  # TODO: fill in the arguments, then delete this TODO
    assert actual == expected


def test_mystery_3c_1() -> None:
    """Test mystery_3c for an expected return value of 1."""
    expected = 1
    actual = mystery_3c(..., ..., ...)  # TODO: fill in the arguments, then delete this TODO
    assert actual == expected


# TODO: add more tests as necessary

if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import pytest
    pytest.main(['a2_part2_q3.py', '-v'])

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # IMPORTANT: Leave this code uncommented when you submit your files.
    # python_ta.check_all(config={
    #     'extra-imports': ['python_ta.contracts'],
    #     'max-line-length': 100,
    #     'disable': ['R1705']
    # })
