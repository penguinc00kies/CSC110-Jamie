"""CSC110 Fall 2021 Assignment 2, Part 1: Predicate Logic

Instructions (READ THIS FIRST!)
===============================
This Python module contains the functions you should complete for Part 1, Questions 3 and 4.
Your task is to:

1. Implement functions `statement3` and `statement4` so that they translate the statements given in
Part 1.
2. Define predicate functions `example_p`, and `example_q` as an example arguments to `statement3`
and `statement4`, then use `test_statements_different` to show that these two functions don't
compute the same things.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Mario Badr and Tom Fairgrieve.
"""
from typing import Callable


###############################################################################
# Part 1, Question 3
###############################################################################
def statement3(my_set: set[int],
               my_p: Callable[[int], bool],
               my_q: Callable[[int], bool]) -> bool:
    """Implementation of Statement 3 from Part 1, Question 2.

    This statement is represented as a function that takes three arguments:
        - a set my_set (corresponds to "S" from the statement)
        - a predicate my_p (corresponds to the predicate "P" from the statement);
          its domain is my_set
        - a predicate my_q (corresponds to the predicate "Q" from the statement);
          its domain is my_set

    Note that my_p is a *function* and can be called inside the body below, e.g. my_p(...).
    Similarly, my_q is also a function and can be called using my_q(...).

    Preconditions:
        - my_p can be called on every element from my_set
        - my_q can be called on every element from my_set
    """


def statement4(my_set: set[int],
               my_p: Callable[[int], bool],
               my_q: Callable[[int], bool]) -> bool:
    """Implementation of Statement 4 from Part 1, Question 2.
    """


###############################################################################
# Part 1, Question 4
###############################################################################
def test_statements_different() -> None:
    """A test that verifies that statement3 and statement4 are not equivalent.
    """
    my_set = set(range(0, 10))
    assert statement3(my_set, example_p, example_q) != statement4(my_set, example_p, example_q)


def example_p(x: int) -> bool:
    """An example predicate for "my_p" that can be used in test_statements_different.
    """


def example_q(x: int) -> bool:
    """An example predicate for "my_q" that can be used in test_statements_different.
    """


if __name__ == '__main__':
    import pytest
    pytest.main(['a2_part1.py', '-v'])

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # Leave this code uncommented when you submit your files.
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'R1729']
    # })
