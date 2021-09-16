"""CSC110 Tutorial 1: Data and Functions

Module Description
==================
This Python file contains exercises for you to complete in Tutorial 1
(Parts 2 and 4).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Mario Badr.
"""


###############################################################################
# Exercise 2: Practice Writing Functions
###############################################################################
# In this part, you'll write some functions to help review the data types
# you learned about in lecture this week, and to get some practice
# writing functions. We recommend working individually but asking a classmate
# or your TA if you get stuck. After each function, you should check your work
# by running this file (right-click -> "Run File in Python Console"), and
# typing in the doctest example to see whether the returned value matches
# what the doctest example says.


def is_much_greater(num1: int, num2: int) -> bool:
    """Return whether num1 is greater than or equal to 2 * num2.

    >>> is_much_greater(8, 3)
    True
    >>> is_much_greater(5, 3)
    False
    """


def make_course_label(code: str, title: str) -> str:
    """Return a string label for a course.

    The course label should have the format
        '<code>: <title>'

    >>> make_course_label('CSC110', 'Foundations of Computer Science I')
    'CSC110: Foundations of Computer Science I'
    >>> make_course_label('PSY100', 'Introductory Psychology')
    'PSY100: Introductory Psychology'
    """


def sum_in_list(num1: float, num2: float, lst: list) -> bool:
    """Return whether the sum of num1 and num2 is in lst (a list of floats).

    >>> sum_in_list(2.0, 3.5, [1.1, 3.3, 5.5, 7.7])
    True
    >>> sum_in_list(-10.1, 23.6, [])
    False
    """


def multiply_sums(set1: set, set2: set) -> int:
    """Return the product of the sums of the elements in set1 and set2.

    >>> multiply_sums({1, 2}, {1})
    3
    >>> multiply_sums({100, 101, 102}, {0})
    0
    >>> multiply_sums({0, -1, -2}, {0, 1, 2})
    -9
    """


def sum_of_values_two(key1: str, key2: str, numbers: dict) -> int:
    """Return the sum of the values in numbers corresponding to key1 and key2.

    numbers is a dictionary mapping strings to integers. You can assume
    that key1 and key2 are always in numbers.

    >>> numbers = {'a': 1, 'b': 10, 'c': 20}
    >>> sum_of_values_two('a', 'c', numbers)
    21
    >>> sum_of_values_two('b', 'b', numbers)
    20
    """


def sum_of_values_many(keys: set, numbers: dict) -> int:
    """Return the sum of the values in numbers corresponding to the given keys.

    keys is a set of strings, and numbers is a dictionary mapping strings to integers.
    As before, you can assume that all given keys are in numbers.

    >>> numbers = {'a': 1, 'b': 10, 'c': 20}
    >>> sum_of_values_many({'a', 'c'}, numbers)
    21
    >>> sum_of_values_many(set(), numbers)
    0

    HINT: you'll need to write a *comprehension* to get all of the values corresponding
    to the given keys (and call "sum" on the result).
    This is the trickiest problem in this sequence, so please ask for help if you get
    stuck!
    """


###############################################################################
# Exercise 4: Representing colour data
###############################################################################
# In this task, you'll work with tuples representing colour data in the RGB24
# colour model. Each of the functions you'll define in this section returns a
# list of colours. To visualize your work, run this file and call the function,
# and save the returned list in a variable.
# Then run the following in the Python console:
#   >>> tutorial1_colours.show_colours(<YOUR VARIABLE HERE>)
#
# This should open a Pygame window showing your colours. :)


def my_favourite_colours() -> list:
    """Return a list of 5-7 colours that you think look pretty.
my
    Pick some colours from https://en.wikipedia.org/wiki/Web_colors#Extended_colors
    (take RGB values from the "Decimal" column).
    """


def stripes(colour1: tuple, colour2: tuple, n: int) -> list:
    """Return a list of length 2*n that alternates between the two colours.

    >>> stripes((64, 224, 208), (100, 100, 100), 3)
    [(64, 224, 208), (100, 100, 100), (64, 224, 208), (100, 100, 100), (64, 224, 208), (100, 100, 100)]
    """


def rgb_combinations(nums: set) -> list:
    """Return a list of colours of every possible combination of RGB values from the given set.

    >>> rgb_combinations({10, 150})

    """


def colours_to_grayscale(colours: list) -> list:
    """Return a list containing the *grayscale version* of each given colour.

    The grayscale version of a colour (r, g, b) is equal to (x, x, x), where
    x is the average of r, g, and b, rounded down to the nearest integer.

    >>> colours = [(10, 50, 70), (200, 200, 200)]
    >>> colours_to_grayscale(colours)
    [(43, 43, 43), (200, 200, 200)]
    """


def gradient(colour0: tuple, colour1: tuple, n: int) -> list:
    """Return a linear gradient between the given colours (of length n + 1).

    >>> gradient((10, 20, 100), (70, 80, 10), 3)
    [(10, 20, 100), (30, 40, 70), (50, 60, 40), (70, 80, 10)]
    """


def waves(colour1: tuple, colour2: tuple, n: int) -> list:
    """Return a "wave gradient" pattern that alternates between the two given colours n times.

    (Experiment with different numbers for the gradient length.)
    """
