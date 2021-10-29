"""CSC110 Tutorial 7: The RSA Cryptosystem, Proofs and in Practice, Part 2

Module Description
==================
This module contains the functions for you to implement in Part 2 of this week's tutorial.
There's a lot of reading for this part, so don't worry if you don't finish everything here;
it's more important that you go slow and understand all of the concepts at each step.

We've given the "final answer" for our sample public key file in the tutorial handout,
so that you can check your work after the tutorial is over too.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import base64


###############################################################################
# 1. Binary representation of numbers
###############################################################################
def binary_to_int(bin_rep: list[int]) -> int:
    """Return the integer represented by the given binary representation.

    Note that the binary representation is read left-to-right, with the units (2^0) digit
    in the LAST position of the list.

    Preconditions:
        - all({b in {0, 1} for b in bin_rep})

    >>> binary_to_int([1])
    1
    >>> binary_to_int([1, 0, 1, 0, 1, 1])  # Fill this in based on your answer to Q1
    43

    NOTE: this function can be implemented by either a for loop or a comprehension.
    For practice, we strongly recommend choosing the technique you are LESS comfortable with.
    """
    return sum([bin_rep[i] * (2 ** (len(bin_rep) - 1 - i)) for i in range(len(bin_rep))])
    # use bin_rep[-i] somewhere


###############################################################################
# 2. From bits to bytes
###############################################################################
def bytes_to_int(byte_sequence: list[int]) -> int:
    """Return the integer represented by the given sequence of bytes.

    Each byte is represented as an int in the range 0-255, inclusive.
    Note that the representation is read left-to-right, with the units (256^0) digit
    in the LAST position of the list.

    Preconditions:
      - all({0 <= b <= 255 for b in byte_sequence})

    >>> bytes_to_int([1, 0, 5])  # (256 ** 2) * 1 + (256 ** 0) * 5
    65541
    >>> bytes_to_int([0, 0, 0, 7])  # (256 ** 0) * 7
    7

    NOTE: this function is extremely similar to binary_to_int. You should be able to
    implement this function by making a very small change.
    """
    return sum([byte_sequence[i] * (256 ** (len(byte_sequence) - 1 - i)) for i in range(len(byte_sequence))])


###############################################################################
# 3. The RSA public key format and Base64 encoding
###############################################################################
def public_key_to_bytes(public_key_file: str) -> list[int]:
    """Return a list of ints corresponding to the Base64-encoded string in public_key_file.

    Preconditions:
        - public_key_file refers to a file in the format described on the tutorial handout

    >>> result = public_key_to_bytes('sample_public_key.txt')
    >>> len(result)
    279
    >>> result[0:11]  # The first 11 elements of result
    [0, 0, 0, 7, 115, 115, 104, 45, 114, 115, 97] # an int represents 4 characters
    """
    with open(public_key_file) as f:
        line = f.readline()

    sep = line.split(' ')
    key = sep[1]
    return list(base64.b64decode(key))


###############################################################################
# 4. Extracting e and n
###############################################################################
def bytes_to_public_key(byte_sequence: list[int]) -> tuple[int, int]:
    """Return the value of the RSA public key (n, e) from byte_sequence.

    >>> bytes_to_public_key([
    ...     0, 0, 0, 7,
    ...     115, 115, 104, 45, 114, 115, 97,  # 'ssh-rsa'
    ...     0, 0, 0, 2,
    ...     2, 1,                             # e = 513
    ...     0, 0, 0, 3,
    ...     1, 0, 1                           # n = 65537
    ... ])
    (65537, 513)

    NOTE: use *list slicing* (which is similar to string slicing, which you saw on A3)
    to extract a sublist from a list. Examples:

        >>> lst = [10, 20, 30, 40, 50, 60]
        >>> lst[0:2]
        [10, 20]
        >>> lst[3:6]
        [40, 50, 60]
    """


def extract_public_key(public_key_file: str) -> tuple[int, int]:
    """Parse an RSA public key (n, e) from a file in the format described on the tutorial handout.

    Preconditions:
        - public_key_file refers to a file in the format described on the tutorial handout
    """


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
