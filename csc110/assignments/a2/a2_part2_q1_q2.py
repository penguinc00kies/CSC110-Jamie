"""CSC110 Fall 2021 Assignment 2, Part 2: Conditional Execution

Instructions (READ THIS FIRST!)
===============================

This Python module contains the functions you should complete for Part 2, Questions 1 and 2.
Note that we've only given the headers for the functions that you should complete.
To test your work against the original functions, we suggest:

    1. Create a NEW Python file (not to be handed in) and copy and paste the original
       functions from the assignment handout into your new file.
    2. a) Run each file in the Python console and call the corresponding functions to
          see if their return values match.
       b) Write a few unit tests that check whether their return values match.
       c) Use hypothesis to create *property-based tests* to see whether their return
          values match on a wide range of inputs. (This is a perfect case when when
          to use property-based testing!!)

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
# Part 2, Question 1
###############################################################################
def mystery_1a_flat(x: int, y: set[int]) -> str:
    """Return the same value as mystery_1a_nested, but using just a single if statement."""
    if x > 1 and sum({n ** 2 for n in y}) >= 10:
        return 'Mario'
    else:
        return 'David'


def mystery_1b_flat(n: int, rows_of_nums: list[list[int]]) -> int:
    """Return the same value as mystery_1b_nested, but using just a single if statement."""


###############################################################################
# Part 2, Question 2
###############################################################################
def mystery_2a_no_if(x: int, y: int, z: set[int]) -> bool:
    """Return the same value as mystery_2a_if, but without using any if statements."""


def mystery_2b_no_if(n: int) -> bool:
    """Return the same value as mystery_2b_if, but without using any if statements."""


def mystery_2c_no_if(c1: int, c2: int, c3: int) -> bool:
    """Return the same value as mystery_2c_if, but without using any if statements."""


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # Leave this code uncommented when you submit your files.
    # python_ta.check_all(config={
    #     'extra-imports': ['python_ta.contracts'],
    #     'max-line-length': 100,
    #     'disable': ['R1705']
    # })
