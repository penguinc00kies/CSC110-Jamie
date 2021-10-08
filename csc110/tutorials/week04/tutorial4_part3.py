"""CSC110 Tutorial 4: Data Classes and For Loops, Exercise 3

Module Description
==================
This module contains functions for you to complete for Exercise 3. These functions
all involve displaying data (text or images) to the user directly, rather than through
a return value.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import random
from typing import Tuple
import pygame.draw

from tutorial4_pygame import pygame_surface


###############################################################################
# Example printing functions (from handout)
###############################################################################
def print_numbers(n: int) -> None:
    """Print out the numbers between 1 and n, inclusive, on separate lines.

    Preconditions:
        - n >= 1

    >>> print_numbers(5)
    1
    2
    3
    4
    5
    """
    for i in range(1, n + 1):
        print(i)


def print_numbers_v2(n: int) -> None:
    """Print out the numbers between 1 and n, inclusive, on a single line.

    Preconditions:
        - n >= 1

    >>> print_numbers_v2(5)
    12345
    """
    for i in range(1, n + 1):
        print(i, end='')


def print_pattern(n: int) -> None:
    """Print out the numbers between 1 and n, inclusive.

    Each number is printed on the same line as the preceding number *except*
    if the number is divisible by 3 or 5.

    Preconditions:
        - n >= 1

    >>> print_pattern(20)
    123
    45
    6
    789
    10
    1112
    131415
    161718
    1920
    """
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
        else:
            print(i, end='')


###############################################################################
# Printing function exercises (implement these)
###############################################################################
def print_squares(n: int) -> None:
    """Print out the squares of the numbers between 1 and n, inclusive, on separate lines.

    Preconditions:
        - n >= 1

    >>> print_squares(5)
    1
    4
    9
    16
    25
    """


def print_emoticons(n: int) -> None:
    """Given a number n, print n lines of an emoticon pattern.

    The pattern repeats the following four symbols, one per line:
        :-), >.<, ^_^, (/â—•ãƒ®â—•)/

    >>> print_emoticons(7)
    :-)
    >.<
    ^_^
    (/â—•ãƒ®â—•)/
    :-)
    >.<
    ^_^

    HINT: we've given you a variable emoticons to refer to the list of emoticons.
    If you're using a loop variable i, you can compute the remainder (i % 4)...
    """


def number_grid(n: int) -> None:
    """Print n lines of the following pattern:

    12345...n
    12345...n
    12345...n

    >>> number_grid(7)
    1234567
    1234567
    1234567
    1234567
    1234567
    1234567
    1234567

    HINT: you can start printing on a new line by calling print('') or simply print().

    Try doing this in two ways:
        1. Use a nested loop to print each number on a single line, and repeat that n times.
        2. Use one loop that calls another function from this file...
    """


def heart_box(n: int) -> None:
    """Print a 2n-by-n box of â™¥ characters.

    >>> heart_box(3)
    â™¥â™¥â™¥
    â™¥â™¥â™¥
    â™¥â™¥â™¥
    â™¥â™¥â™¥
    â™¥â™¥â™¥
    â™¥â™¥â™¥

    Try doing this in two ways:
        - Using a nested loop.
        - Creating a string of n â™¥ characters using string repetition.
    """
    # You can copy-and-paste the â™¥ character into a string literal in your code.


def catcade(n: int) -> None:
    """Print an n-by-n cascading pattern of ðŸ˜¸ characters.

    >>> catcade(4)
    ðŸ˜¸ðŸ˜¸ðŸ˜¸ðŸ˜¸
    ðŸ˜¸ðŸ˜¸ðŸ˜¸
    ðŸ˜¸ðŸ˜¸
    ðŸ˜¸

    Try doing this in two ways:
        - Using a nested loop.
        - Creating a string of repeated ðŸ˜¸ characters using string repetition.
    """
    # You can copy-and-paste the ðŸ˜¸ character into a string literal in your code.


###############################################################################
# Example drawing functions (from handout)
###############################################################################
def pygame_demo() -> None:
    """Run a simple pygame demo.

    (You'll be modifying this function as you follow the demo in the tutorial handout.
    """
    with pygame_surface() as screen:
        pygame.draw.circle(screen, (255, 189, 213), (100, 100), 75)


###############################################################################
# Additional drawing exercises
###############################################################################
def four_circles() -> None:
    """Draw four circles with sides touching in each quadrant of the screen, any colour."""


def sixteen_circles() -> None:
    """Draw four circles with sides touching in a 4-by-4 grid, any colour."""


def circle_grid(n: int) -> None:
    """Draw n ** 2 circles with sides touching in an n-by-n grid, any colour.

    Preconditions:
        - n >= 1
    """


def gridlines(n: int) -> None:
    """Draw an n-by-n grid of lines of thickness 2, with randomly-chosen colours.

    Preconditions:
        - n >= 1

    Hint: use random.randint to generate a random number in a certain range.
    """


def circle_gradient(n: int, c0: Tuple[int, int, int], c1: Tuple[int, int, int]) -> None:
    """Draw a row of circles coloured with a gradient from c0 to c1.

    Preconditions:
        - n >= 1
    """


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # You can uncomment the following to check doctests.
    # import doctest
    # doctest.testmod(verbose=True)
