"""CSC110 Tutorial 2: Functions and Logic (Exercise 3)

Module Description
==================
This module contains the (buggy) functions for Exercise 3, and skeletons of
unit tests for each function. The bottom of this file includes the boilerplate
code for running the unit tests using pytest. (Right-click and select
"Run File in Python Console", or go to Run -> Run... and select this file.)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import math


###############################################################################
# calculate_angles
###############################################################################
def calculate_angles(side_a: float, side_b: float, side_c: float) -> list:
    """Return the three angles of the triangle with lengths of side_a, side_b,
    and side_c.

    >>> calculate_angles(23.0, 23.0, 23.0)
    [1.0471975511965976, 1.0471975511965976, 1.0471975511965976]
    """
    side_a2 = side_a ** 2
    side_b2 = side_b ** 2
    side_c2 = side_c ** 2

    angle_a = math.acos((side_a2 - side_b2 - side_c2) / (-2 * side_b * side_c))
    angle_b = math.acos((side_b2 - side_a2 - side_c2) / (-2 * side_a * side_c))
    angle_c = math.acos((side_c2 - side_a2 - side_b2) / (-2 * side_a * side_b))

    return [angle_a, angle_b, angle_c]

# The formulae the calculate the angles opposite sides a and b are identical the the one that calculates
# the angle opposite of side c. That is wrong.

def test_calculate_angles_passing() -> None:
    """Test calculate_angles with 30.0, 30.0, 30.0

    TODO: complete this test (description and body) so that it calls max_corresponding_value
          and PASSES.
    """
    actual = calculate_angles(30.0, 30.0, 30.0)
    expected = [1.0471975511965976, 1.0471975511965976, 1.0471975511965976]
    assert actual == expected


def test_calculate_angles_failing() -> None:
    """Test calculate_angles with 2.0, 2.0, 3.0

    TODO: complete this test (description and body) so that it calls max_corresponding_value
          and FAILS.
    """
    actual = calculate_angles(2.0, 2.0, 3.0)
    expected = [0.7227342478134157, 0.7227342478134157, 1.696124157962962]
    assert actual == expected


###############################################################################
# max_corresponding_value
###############################################################################
def max_corresponding_value(map1: dict, map2: dict, key: str) -> int:
    """Compare the values corresponding to key in map1 and map2, and return the larger value.

    If key is only in one of the dicts, return its corresponding value in that dict.
    If key is in neither dict, return 0.

    You may ASSUME that:
        - map1 and map2 both map strings to integers
    """
    if key in map1 and key in map2:
        return max(map1[key], map2[key])
    elif key in map1:
        return map1[key]
    elif key in map2:
        return map2[key]
    else:  # the key is in neither dictionary
        return 0

# If key is in map1 and map2, it satisfies both the first and third condition. However, although
# the third condition is more accurate, the first condition will always trigger first. Therefore,
# the third condition is unreachable.

def test_max_corresponding_value_passing() -> None:
    """Test max_corresponding_value with {'grapes': 6}, {'pears': 14}, 'apples'

    TODO: complete this test (description and body) so that it calls max_corresponding_value
          and PASSES.
    """
    actual = max_corresponding_value({'grapes': 6}, {'pears': 14}, 'apples')
    expected = 0
    assert actual == expected


def test_max_corresponding_value_failing() -> None:
    """Test max_corresponding_value with {'grapes': 6}, {'pears': 14}, 'apples'

    TODO: complete this test (description and body) so that it calls max_corresponding_value
          and FAILS.
    """
    actual = max_corresponding_value({'grapes': 6}, {'grapes': 14}, 'grapes')
    expected = 14
    assert actual == expected


if __name__ == '__main__':
    import pytest

    pytest.main(['tutorial2_ex3.py', '-v'])
