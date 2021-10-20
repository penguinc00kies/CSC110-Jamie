"""CSC110 Fall 2021: Term Test 1, Question 1 (Function Design)

Module Description
==================
This Python file contains instructions for this question. There are THREE
parts of this question, labelled "Part (a)", "Part (b)", etc.
The comments in this file contain instructions on how to complete each part,
so please read those comments carefully.

At the bottom of the file we've provided code to run doctest, pytest, and python_ta.
python_ta is not required for grading.

SUBMIT THIS FILE FOR GRADING!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""

from hypothesis import given
from hypothesis.strategies import integers, tuples


####################################################################################################
# Part (a)
####################################################################################################
# Here is a definition:
#
# Let p be a 3-item tuple of the form (a, b, c) where a, b and c are positive integers.
# We say that p is a Pythagorean triple whenever c squared is equal to the sum of a squared plus b
# squared.
# For example, p = (3, 4, 5) is a Pythagorean triple because 25 = 9 + 16.
#
# Use the Function Design Recipe to define a function is_pythagorean_triple that returns
# whether a given 3-item tuple is a Pythagorean triple. You need to write:
#
# 1. A precondition (as a Python expression) expressing that the items in p are positive integers.
# 2. TWO different doctest examples.
# 3. A correct function body.


def is_pythagorean_triple(p: tuple[int, int, int]) -> bool:
    """Return whether p is a Pythagorean triple.

    Preconditions:
        - p[0] > 0
        - p[1] > 0
        - p[2] > 0

    >>> is_pythagorean_triple((13, 5, 12))
    True
    >>> is_pythagorean_triple((7, 5, 11))
    False
    """
    hypotenuse_0 = p[0] ** 2 == p[1] ** 2 + p[2] ** 2
    hypotenuse_1 = p[1] ** 2 == p[2] ** 2 + p[0] ** 2
    hypotenuse_2 = p[2] ** 2 == p[0] ** 2 + p[1] ** 2

    return hypotenuse_0 or hypotenuse_1 or hypotenuse_2


####################################################################################################
# Part (b)
####################################################################################################
# Here is another definition:
#
# Let L be a list where every item is a tuple of three positive integers that we will call (a,b,c).
# We say that L is a *Pythagorean list* when every item in the list is a Pythagorean triple.
# An empty list is NOT considered to be a Pythagorean triple.
#
# Use the Function Design Recipe to define a function is_pythagorean_list that returns
# whether a given list is a Pythagorean list. You need to write:
#
# 1. A precondition (as a Python expression) expressing that every item in list lst is a tuple that
#    contains positive integers.
# 2. TWO different doctest examples.
# 3. A correct function body that uses a comprehension and any/all.
#    You must call is_pythagorean_triple in this function, and you may NOT use loops.


def is_pythagorean_list(lst: list[tuple[int, int, int]]) -> bool:
    """Return whether lst is a Pythagorean list.

    Preconditions:
        - all([all([integer > 0 for integer in tuple]) for tuple in lst])

    >>> is_pythagorean_list([(4, 5, 3), (5, 12, 13), (8, 15, 17)])
    True
    >>> is_pythagorean_list([(4, 5, 3), (1, 2, 3)])
    False
    """

    if lst == []:
        return False
    return all([is_pythagorean_triple(p_triple) for p_triple in lst])


####################################################################################################
# Part (c)
####################################################################################################
# Consider the following property:
#
# For all positive integers a, b, c and k,
#   if p = (a, b, c) is a Pythagorean triple then (k*a, k*b, k*c) is also a Pythagorean triple.
#
# Complete the property-based test below to express this property.
# We have started it for you; you only need to fill in the body of the test.


@given(p=tuples(integers(min_value=1), integers(min_value=1), integers(min_value=1)),
       k=integers(min_value=1))
def test_multiplier_pyth_triple(p: tuple[int, int, int], k: int) -> None:
    """Test the multiplier property of Pythagorean triples."""
    new_tuple = (k * p[0], k * p[1], k * p[2])
    assert is_pythagorean_triple(p) == is_pythagorean_triple(new_tuple)


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    # You can uncomment this to check your test in Part (c).
    import pytest
    pytest.main(['q1.py'])

    import python_ta
    python_ta.check_all(config={
        'disable': ['R1729', 'C0412'],
        'extra-imports': ['python_ta.contracts', 'hypothesis.strategies'],
        'max-line-length': 100
    })
