"""CSC110 Lecture 17 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""

import math

def divides(d: int, n: int) -> bool:
    """Return whether d divides n."""
    if d == 0:
        return n == 0
    else:
        return n % d == 0


def is_common_divisor(x: int, y: int, d: int) -> bool:
    """Return whether d is a common divisor of x and y."""
    return divides(d, x) and divides(d, y)


def naive_gcd(m: int, n: int) -> int:
    """Return the gcd of m and n."""
    if m == 0:
        return abs(n)
    elif n == 0:
        return abs(m)
    else:
        possible_divisors = range(1, min(abs(m), abs(n)) + 1)
        return max({d for d in possible_divisors if divides(d, m) and divides(d, n)})


def euclidean_gcd(a: int, b: int) -> int:
    """Return the gcd of a and b."""
    x, y = a, b

    while y != 0:
        # Loop invariant (we use naive_gcd to check that the gcd are correct)
        assert naive_gcd(x, y) == naive_gcd(a, b)

        r = x % y
        x, y = y, r

    return x


def gcd_extended(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that

    gcd(a, b) == p * a + b * q.

    >>> gcd_extended(10, 3)
    (1, 1, -3)
    """
    x, y = a, b

    # Initialize px, qx, py, and qy
    px, qx = 1, 0
    py, qy = 0, 1

    while y != 0:
        # Loop invariants
        assert math.gcd(a, b) == math.gcd(x, y)  # L.I. 1
        assert x == px * a + qx * b  # L.I. 2
        assert y == py * a + qy * b  # L.I. 3

        q, r = divmod(x, y)  # quotient and remainder when a is divided by b

        # Update x and y
        x, y = y, r

        # Update px, qx, py, and qy
        px, qx, py, qy = ...

    return (x, px, qx)
