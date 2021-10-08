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
import math
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
        - date: the date of the delay
        - time: the time of the delay
        - day: the day of the week on which the delay occurred
        - station: the name of the subway station where the delay occurred
        - code: the TTC delay code, which usually describes the cause of the delay
        - min_delay: the length of the subway delay (in minutes)
        - min_gap: the length of time between subway trains (in minutes)
        - bound: the direction in which the train was travelling. This is dependent on the line the train was on
        - line: the abbreviated name of the subway line where the delay occurred
        - vehicle: the id number of the train on which the delay occurred

    Representation invariants:
        - day in {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
        - min_delay >= 0
        - min_gap >= 0
    """
    date: datetime.date
    time: datetime.time
    day: str
    station: str
    code: str
    min_delay: int
    min_gap: int
    bound: str
    line: str
    vehicle: int


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
    with open(filename) as file:
        # This line creates a csv reader, which is a Python value that
        # can read csv data from a given file (essentially splitting up the
        # file into rows, and splitting each row by commas).
        reader = csv.reader(file)

        # This line reads the first row of the csv file, which contains the headers.
        # The result is a list of strings.
        headers = next(reader)

        # This list comprehension reads each remaining row of the file,
        # where each row is represented as a list of strings.
        # The header row is *not* included in this list.
        data = [process_row(row) for row in reader]

    return (headers, data)


def process_row(row: List[str]) -> Delay:
    """Convert a row of subway delay data to Delay object.

    Notes:
    - This function is very similar to the process_row function from tutorial3_part4.py,
      except now you're returning a Delay object instead of list.

    Preconditions:
        - row has the correct format for the TTC subway delay data set
    """
    return Delay(
        str_to_date(row[0]),  # date
        str_to_time(row[1]),  # time
        row[2],  # day
        row[3],  # station
        row[4],  # code
        int(row[5]),  # min delay
        int(row[6]),  # min gap
        row[7],  # bound
        row[8],  # line
        int(row[9])  # vehicle
    )


def str_to_date(date_string: str) -> datetime.date:
    """Convert a string in mm/dd/yyyy format to a datetime.date.

    Hints:
    1. You can use str.split(date_string, '/') to first obtain
       the three strings corresponding to month, day, and year separately.
    2. Create a new datetime.date value by calling this type on three arguments:
       datetime.date(year, month, day).

    Preconditions:
    - date_string has format mm/dd/yyyy

    >>> str_to_date('01/01/2014')
    datetime.date(2014, 1, 1)
    """
    day = str.split(date_string, '/')
    return datetime.date(int(day[2]), int(day[0]), int(day[1]))


def str_to_time(time_string: str) -> datetime.time:
    """Convert a string in HH:mm format to a datetime.time.

    The hours are specified in 24-hour format (from 00 to 23).

    Similar hint as str_to_date. datetime.time takes two arguments:
    hour and minute, in that order.

    >>> str_to_time('00:21')
    datetime.time(0, 21)
    """
    time = str.split(time_string, ':')
    return datetime.time(int(time[0]), int(time[1]))


###############################################################################
# From nested lists to data classes
###############################################################################
def longest_delay_v1(data: List[Delay]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
        - data != []
    """
    return max([row.min_delay for row in data])


def average_delay_v1(data: List[Delay]) -> float:
    """Return the average subway delay in data.

    Preconditions:
        - data != []
    """
    return sum([row.min_delay for row in data]) / len(data)


def num_delays_by_month_v1(data: List[Delay], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
        - 0 <= month < 12
        - 2014 <= year <= 2018
    """
    return len([row for row in data if row.date.year == year and row.date.month == month])


###############################################################################
# From comprehensions to loops
###############################################################################
def longest_delay_v2(data: List[Delay]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
        - data != []
    """
    max_so_far = -math.inf
    for i in data:
        if i.min_delay > max_so_far:
            max_so_far = i.min_delay
    return max_so_far


def average_delay_v2(data: List[Delay]) -> float:
    """Return the average subway delay in data.

    Preconditions:
        - data != []
    """
    sum_so_far = 0.0
    for i in data:
        sum_so_far = sum_so_far + i
    return sum_so_far / len(data)


def num_delays_by_month_v2(data: List[Delay], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
    - 0 <= month < 12
    - 2014 <= year <= 2018
    """
    delays_so_far = 0
    for i in data:
        if i.date.month == month and i.date.year == year:
            delays_so_far = delays_so_far + 1
    return delays_so_far
