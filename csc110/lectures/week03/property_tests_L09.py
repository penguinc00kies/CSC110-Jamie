"""CSC110 Lecture 9 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
from hypothesis import given                # for the @given decorator
from hypothesis.strategies import integers, lists  # for generating integers and lists

from L09 import is_even, num_evens


####################################################################################################
# Lecture Demo
####################################################################################################
@given(x=integers())
def test_is_even_2x(x: int) -> None:
    """Test that is_even returns True when given a number of the form 2*x."""
    assert is_even(2*x)


@given(x=integers())
def test_is_even_2x_plus_1(x: int) -> None:
    """Test that is_even returns False when given a number of the form 2*x + 1."""
    assert not is_even(2 * x + 1)

@given(nums=lists(integers()), x = integers())
def test_num_evens_one_more_even(nums: list[int], x: int) -> None:
    """Test num_evens when you add one more even element."""
    assert num_evens(nums + [2 * x]) == num_evens(nums) + 1


####################################################################################################
# Exercise 1
####################################################################################################
# from L09 import divides
# @given(a=integers(), d=integers())
# def test_a(a: int, d: int) -> None:
#     """Tests that d divides the product of d and a"""
#     assert divides(d, d * a)
#
# @given(n=integers())
# def test_b(n: int) -> None:
#     """Tests that 1 divides any integer n"""
#     assert divides(1,n)
#
#
# @given(n=integers())
# def test_c(n: int) -> None:
#     """Tests if an integer n can divide itself"""
#     assert divides(n, n)
#
#
# @given(n=integers(), d=integers())
# def test_d(n: int, d: int) -> None:
#     """Test that if d divides n, then d divides n + d"""
#     assert not divides(d, n) or divides(d, n + d)


if __name__ == '__main__':
    import pytest
    pytest.main(['test_L09.py', '-v'])
