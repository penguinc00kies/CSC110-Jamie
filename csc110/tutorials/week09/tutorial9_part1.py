"""CSC110 Tutorial 9: More Running-Time Analysis

Module Description
==================
This module contains a function that you will analyse for this part of the tutorial.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""


def int_to_binary(n: int) -> list[int]:
    """Return the binary representation of the given number with a leading 1.

    Note that the binary representation is read left-to-right, with the units (2^0) digit
    in the LAST position of the list.
    This matches how we usually read binary representations.

    Preconditions:
        - n >= 1

    >>> int_to_binary(34)  # 32 + 0 + 0 + 0 + 2 + 0
    [1, 0, 0, 0, 1, 0]
    >>> int_to_binary(111)  # 64 + 32 + 0 + 8 + 4 + 2 + 1
    [1, 1, 0, 1, 1, 1, 1]
    """
    x = n
    bin_rep_so_far = []
    while x > 0:
        x, r = x // 2, x % 2  # Or, divmod(x, 2)
        # list.insert(bin_rep_so_far, 0, r)
        list.append(bin_rep_so_far, r)

    list.reverse(bin_rep_so_far)
    return bin_rep_so_far
    # Now running time is 1 + 1 + log_2(n) * 1 + log_2(n) which is big O (log_2(n))


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
