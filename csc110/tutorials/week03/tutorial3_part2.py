"""CSC110 Tutorial 3: Correctness, More Logic, and Nested Data (Exercise 2)

Module Description
==================
Write your functions for Exercise 2 in this file.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
from hypothesis import given
from hypothesis.strategies import integers


def divides(d: int, n: int) -> bool:
    """Return whether d divides n."""
    possible_divisors = range(- abs(n), abs(n) + 1)
    return any({n == k * d for k in possible_divisors})


def is_cd(d: int, m: int, n: int) -> bool:
    """Return whether d divides both m and n.

    >>> is_cd(2, 10, 6)
    True
    >>> is_cd(3, 10, 6)
    False
    """
    return divides(d, m) and divides(d, n)


def is_gcd(d: int, m: int, n: int) -> bool:
    """Return whether d is the greatest common divisor of m and n.

    >>> is_gcd(2, 12, 30)
    False
    >>> is_gcd(6, 12, 30)
    True

    HINT: there should be a m = 0, n = 0 case in your implementation,
    following the definition of gcd.

    For the other case, you'll need to define a range of possible common divisors
    for m and n. Note that gcd(x, 0) = abs(x) for all x, since every number
    divides 0.
    """
    return gcd(m, n) == d


def gcd(m: int, n: int) -> int:
    """Return the greatest common divisor of m and n.

    This should follow the same structure as is_gcd, and you may find it easier
    to implement this one first.

    >>> gcd(12, 30)
    6
    >>> gcd(124, 256)
    4

    HINT: there should be a m = 0, n = 0 case in your implementation,
    following the definition of gcd.

    For the other case, you'll need to define a range of possible common divisors
    for m and n. Note that gcd(x, 0) = abs(x) for all x, since every number
    divides 0.
    """
    if m == 0 and n == 0:
        return 0
    else:
        return max({x for x in range(0, max(abs(m), abs(n)) + 1) if divides(x, m) and divides(x, n)})


# you can also write integers(-100, 100)
@given(m=integers(min_value=-100, max_value=100), n=integers(min_value=-100, max_value=100))
def test_a(m: int, n: int) -> None:
    """Test that one is a common denominator of any two integers."""
    assert is_gcd(1, m, n) or (m == 0 and n == 0)


@given(m=integers(min_value=-100, max_value=100), n=integers(min_value=-100, max_value=100))
def test_b(m: int, n: int) -> None:
    """Test that either m and n are both 0 or gcd(m, n) is always greater than or equal to 1."""
    assert (m == 0 and n == 0) or gcd(m, n) >= 1


@given(m=integers(min_value=-100, max_value=100), n=integers(min_value=-100, max_value=100))
def test_c(m: int, n: int) -> None:
    """Test that gcd(m, n) as d in is_gcd(d, m, n) will always return true."""
    assert is_gcd(gcd(m, n), m, n) == True


@given(m=integers(min_value=-100, max_value=100), n=integers(min_value=-100, max_value=100))
def test_d(m: int, n: int) -> None:
    """Test that the gcd of 2m and 2n is always equal to 2 * gcd(m, n)"""
    assert gcd(2*m, 2*n) == 2*gcd(m,n)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    # Uncomment the next two lines when you are ready to run the property-based tests.
    import pytest
    pytest.main(['tutorial3_part2.py'])
