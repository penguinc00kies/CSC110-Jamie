"""CSC110 Tutorial 3: Correctness, More Logic, and Nested Data (Exercise 4)

Module Description
==================
Write your functions for Exercise 4 in this file.

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
import datetime


def read_csv_file(filename: str) -> tuple[list[str], list[list[str]]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists of strings, where each inner list
      stores a row in the csv file.

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this as a Python expression)
    """
    # "open" is a builtin function that accesses a file on your computer,
    # looking in the same folder as the current Python module.
    # "with" is a special type of compound statement in Python that
    # works with "open" to create a new variable "file" that you can use
    # inside the with block to access the file.
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
        data = [row for row in reader]

    return (headers, data)


def process_row(row: list[str]) -> list:
    """Convert a row of subway delay data to a list with more appropriate data types.

    Notes:
    - You can use int(...) to convert from a string to an integer
    - You'll need to complete the str_to_date and str_to_time functions below
      to use them here.
    - We've left some comments to help you keep track of the values you're returning.

    Preconditions:
        - row has the correct format for the TTC subway delay data set
    """
    return [
        ...,  # date
        ...,  # time
        ...,  # day
        ...,  # station
        ...,  # code
        ...,  # min delay
        ...,  # min gap
        ...,  # bound
        ...,  # line
        ...  # vehicle
    ]


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


def str_to_time(time_string: str) -> datetime.time:
    """Convert a string in HH:mm format to a datetime.time.

    The hours are specified in 24-hour format (from 00 to 23).

    Similar hint as str_to_date. datetime.time takes two arguments:
    hour and minute, in that order.

    >>> str_to_time('00:21')
    datetime.time(0, 21)
    """


###############################################################################
# Operating on the data
###############################################################################
def longest_delay(data: list[list]) -> int:
    """Return the longest delay in the given data.

    Preconditions:
    - data is in the format of the TTC subway delays csv file
    """


def average_delay(data: list[list]) -> float:
    """Return the average subway delay in data.

    Preconditions:
    - data is in the format of the TTC subway delays csv file
    """


def num_delays_by_month(data: list[list], year: int, month: int) -> int:
    """Return the number of delays that occurred in the given month and year.

    Preconditions:
    - data is in the format of the TTC subway delays csv file
    - 0 <= month < 12
    - 2014 <= year <= 2018
    """


def delays_by_cause(data: list[list]) -> dict[str, int]:
    """Return a map from cause code to the number of delays for that cause.

    In the returned dictionary:
    - Each key is the code (from the "code" column in the CSV file)
    - Each corresponding value is the number of delays in data that
      have that cause.

    Preconditions:
    - data is in the format of the TTC subway delays csv file

    Hints:
        First extract just the "code" column from the data,
        and then the unique codes in that column.

        You can use the list.count method to find the number of times
        an element appears in a list. (This is a bit inefficient, though,
        and we'll learn about a better approach next week.)
    """


def sorted_delays_by_cause(cause_map: dict[str, int]) -> list[tuple[int, str]]:
    """Return a list of causes and their frequencies, sorted in descending order of frequency.

    cause_map has the same structure as the return value of delays_by_cause.
    The returned list contains tuples of (cause frequency, cause name) *in that order*.

    Hint: first generate a list of tuples using a comprehension.
    Then use sorted on the list of tuples, which sorts the tuples based on their first element,
    and breaks ties by comparing their second element.
    Pass reverse=True to sorted to sort in descending rather than ascending order:

        >>> sorted([(1, 'hi'), (10, 'bye'), (3, 'David')])
        [(1, 'hi'), (3, 'David'), (10, 'bye')]
        >>> sorted([(1, 'hi'), (10, 'bye'), (3, 'David')], reverse=True)
        [(10, 'bye'), (3, 'David'), (1, 'hi')]
    """
