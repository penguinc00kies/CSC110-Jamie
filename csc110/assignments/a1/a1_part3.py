"""CSC110 Fall 2021 Assignment 1, Part 3: Debugging Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains the program and tests described in Part 3.
You can run this file as given to see the pytest report given in the handout.
Your task is to fix all errors in this file so that each test passes
(see assignment handout for details).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import math
import pytest


###############################################################################
# Professor Xavier's program
###############################################################################
def class_average(class_grades: list) -> float:
    """Return the weighted average grade of students for all grades in class_grades.

    Each element of class_grades is itself a list, containing three floats
    representing the grades of a particular student on the three assignments.

    See assignment handout for details.

    You may ASSUME that:
        - class_grades is non-empty
        - class_grades contains only lists
        - the lists in class_grades contain exactly three floats
        - each float in each list is between 0.0 and 100.0.

    """
    student_averages = [student_average(grades) for grades in class_grades]

    # Return the average grade across all students in this section
    return sum(student_averages) / len(student_averages)


def student_average(grades: list) -> float:
    """Return the weighted average of a student's grades.

    You may ASSUME that:
        - grades consists of exactly three float values
    """
    # Sort the student's grades
    sorted_grades = sorted(grades)

    # These are the weights for the assignment grades
    weights = [0.25, 0.35, 0.4]

    return (
        weights[0] * sorted_grades[0] +
        weights[1] * sorted_grades[1] +
        weights[2] * sorted_grades[2]
    )


###############################################################################
# Tests for section_average
###############################################################################
def test_section_average_all_grades_equal() -> None:
    """Test section_average when students have the same grade on each assignment.
    """
    grades = [[80.0, 80.0, 80.0],
              [90.0, 90.0, 90.0]]

    expected = 85.0
    actual = class_average(grades)
    assert math.isclose(actual, expected)


def test_class_average_no_grades_equal() -> None:
    """Test class_average when every grade is different.
    """
    grades = [[60.0, 70.0, 75.0], [80.0, 65.0, 85.0]]

    expected = 73.875
    actual = class_average(grades)
    assert math.isclose(actual, expected)


def test_class_average_many_students() -> None:
    """Test class_average when there are a lot of students in a section.
    """
    grades = [[80.0, 70.0, 75.0],
              [90.0, 78.0, 65.0],
              [66.0, 74.0, 60.0],
              [60.0, 55.0, 75.0],
              [82.0, 80.0, 88.0],
              [50.0, 88.0, 73.0]]

    expected = 74.15
    actual = class_average(grades)
    assert math.isclose(actual, expected)


if __name__ == '__main__':
    pytest.main(['a1_part3.py', '-v'])
