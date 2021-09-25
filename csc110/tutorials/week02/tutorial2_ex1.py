"""CSC110 Tutorial 2: Functions and Logic (Exercise 1)

Module Description
==================
Write your functions for Exercise 1 in this file. Note that you're responsible
for the entire function design, following the steps of the Function Design
Recipe: see Section 2.5 in https://www.teach.cs.toronto.edu/~csc110y/fall/notes/.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import doctest


def is_sum(float1: float, float2: float, float3: float) -> bool:
    """
    Returns whether or not one of float1, float2, and float3 is the sum of the other two

    >>> is_sum(1.5, 3.5, 2.0)
    True
    >>> is_sum(3.0, 2.1, 1.7)
    False
    """
    if float1 + float2 == float3 or float2 + float3 == float1 or float3 + float1 == float2:
        return True
    else:
        return False

def average_length(strings: list) -> float:
    """
    Returns the average length of the strings in a list as a float. If the list is empty, returns -1.0

    >>> average_length(['John', 'Fitzgerald', 'Kennedy'])
    7.0
    >>> average_length([])
    -1.0
    """
    if strings == []:
        return -1.0;
    else:
        return sum([len(x) for x in strings]) / len(strings)

def is_short_enough(string_set: set, max_size: int):
    """
    Returns a set only containing strings from string_set whose lengths are equal to or less then
    max_length
    
    ASSUME that the integer is non negative
    
    >>> is_short_enough({'John', 'Fitzgerald', 'Kennedy'}, 5)
    {'John'}
    >>> is_short_enough({'supercalifragilisticexpialidocious'}, 10)
    set()
    """
    return {x for x in string_set if len(x) <= max_size}

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
