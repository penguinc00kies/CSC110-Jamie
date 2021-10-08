"""CSC110 Tutorial 4: Data Classes and For Loops, Exercise 1

Module Description
==================
This module contains the data classes and functions you should complete for Exercise 1.
Note that this file is very similar to tutorial3_part4.py from last week, so you should
have that file open while you're working on this exercise.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import csv
from dataclasses import dataclass
import datetime
from typing import List, Tuple


###############################################################################
# The new data class
###############################################################################
@dataclass
class Delay:
    """A data type representing a specific subway delay instance.

    This corresponds to one row of the tabular data found in ttc-subway-delays.csv.

    Attributes:
        - TODO: fill in attribute names and descriptions here

    Representation invariants:
        - TODO: fill in representation invariants here
    """
    # TODO: fill in attribute names and type annotations


def read_csv_file(filename: str) -> Tuple[List[str], List[Delay]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of Delays (using the data class you just defined).

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this as a Python expression)

    HINT: you can reuse almost exactly the same code as your tutorial3_part4.py from
    last week. We didn't write this code for you here because we want to you take a
    moment to review that code and copy it here yourself.
    """


def process_row(row: List[str]) -> Delay:
    """Convert a row of subway delay data to Delay object.

    Notes:
    - This function is very similar to the process_row function from tutorial3_part4.py,
      except now you're returning a Delay object instead of list.

    Preconditions:
        - row has the correct format for the TTC subway delay data set
    """


###############################################################################
# From nested lists to data classes
###############################################################################
def longest_delay_v1(data: List[Delay]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
        - data != []
    """


def average_delay_v1(data: List[Delay]) -> float:
    """Return the average subway delay in data.

    Preconditions:
        - data != []
    """


def num_delays_by_month_v1(data: List[Delay], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
        - 0 <= month < 12
        - 2014 <= year <= 2018
    """


###############################################################################
# From comprehensions to loops
###############################################################################
def longest_delay_v2(data: List[Delay]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
        - data != []
    """


def average_delay_v2(data: List[Delay]) -> float:
    """Return the average subway delay in data.

    Preconditions:
        - data != []
    """


def num_delays_by_month_v2(data: List[Delay], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
    - 0 <= month < 12
    - 2014 <= year <= 2018
    """
