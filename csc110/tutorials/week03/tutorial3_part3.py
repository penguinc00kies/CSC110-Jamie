"""CSC110 Tutorial 3: Correctness, More Logic, and Nested Data (Exercise 3)

Module Description
==================
This is the starter file for Exercise 3 (using pdb, the Python debugger).
Please follow the step-by-step instructions in that exercise.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""


def union_and_intersection(set1: set, set2: set) -> tuple[set, set]:
    """Return a tuple containing the union and intersection of set1 and set2.

    >>> result = union_and_intersection({1, 2, 3}, {2, 5, 10, 20})
    >>> result[0] == {1, 2, 3, 5, 10, 20}
    True
    >>> result[1] == {2}
    True
    """
    breakpoint()
    union = set.union(set1, set2)
    intersection = set.intersection(set1, set2)
    return (union, intersection)
