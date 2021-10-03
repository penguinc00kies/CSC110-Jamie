"""CSC110 Fall 2020 Assignment 2, Part 4: Processing Raw Course Data

Instructions (READ THIS FIRST!)
===============================
This Python module contains the functions you should complete for Part 4 of this assignment.
Your task is to complete this module by writing the body of the functions so that they do what
their descriptions claim.

You may, but are not required, to write doctests for this part.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import datetime
import json

import a2_part3


###################################################################################################
# Part 4: Processing Raw Data
###################################################################################################
def read_course_data(file: str) -> dict:
    """Return a dictionary mapping course codes to course data from the data in the given file.

    In the returned dictionary:
        - each key is a string representing the course code
        - each corresponding value is a tuple representing a course value, in the format
          descried in Part 3 of the assignment handout.

    Note that the implementation of this function provided to you is INCOMPLETE since it just
    returns a dictionary in the same format as the raw JSON file. It's your job to implement
    the functions below, and then modify this function body to get the returned data
    in the right format.

    Preconditions:
        - file is the path to a JSON file containing course data using the same format as
          the data in data/course_data_small.json.
    file is the name (or path) of a JSON file containing course data using the format in
    the sample file course_data_small.json.
    """
    with open(file) as json_file:
        data = json.load(json_file)

    return data  # TODO: transform data into the format specified in Part 4, then remove this TODO


def transform_course_data(course_data: dict) -> tuple[str, str, set]:
    """Transform the given course_data into a tuple representing that course.

    The returned tuple is in the course format described on the assignment handout.

    Preconditions:
        - course_data is a dictionary containing data about a single course, in the format
          found in course_data_small.json.
    """


def transform_section_data(section_data: dict) -> tuple[str, str, tuple]:
    """Transform the given section_data into a tuple representing that section.

    The returned tuple is in the "section" format described on the assignment handout.

    Preconditions:
        - section_data is a dictionary containing data about a single section, in the format
          found in course_data_small.json.
    """


def transform_meeting_time_data(meeting_time_data: dict) \
        -> tuple[str, datetime.time, datetime.time]:
    """Transform the given meeting_time_data into a tuple representing that section.

    The returned tuple is in the "meeting time" format described on the assignment handout.

    Preconditions:
        - meeting_time_data is a dictionary containing data about a single meeting time, in the
          format found in course_data_small.json.

    Hint: The times in the JSON file are length-5 strings in format HH:MM using a 24-hour clock.
    You'll need to do some string processing to extract the hours and minutes, and convert
    these to ints and then to a datetime.time. The str.split method is one approach.
    """


def get_valid_schedules(course_data: dict[str, tuple[str, str, set]],
                        courses: set[str],
                        term: str) -> list[dict[str, tuple]]:
    """Return a list of all valid schedules for the given courses and in the given term.

    courses is a set of course codes; use the given course_data to look up each course code
    to get the corresponding course tuple.

    All sections in each returned schedule should meet in the given term; 'Y' sections meet
    in both 'F' and 'S' terms.

    Return an empty list if there are no valid schedules for the given course codes, or if
    at least one of the courses does not have any sections that meet in the given term.

    Preconditions:
      - len(courses) == 5
      - term in {'F', 'S'}
      - all({course_code in course_data for course_code in courses})

    Hints:
        1. You can use a2_part3.valid_five_course_schedules.
        2. You'll need to process each course to filter to keep only the sections
           that appear in the given term. See the function we've started for you below.
    """


def filter_by_term(course: tuple[str, str, set], term: str) -> tuple[str, str, set]:
    """Return a copy of the given course with only sections that meet in the given term.

    The returned tuple has the same course code and title as the given course, and its
    sections set is a subset of the original.

    Note that a 'Y' section meets in BOTH 'F' and 'S' terms, and so should always be
    included in the returned course tuple.

    Preconditions:
      - term in {'F', 'S'}
    """


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # IMPORTANT: Leave this code uncommented when you submit your files.
    # python_ta.check_all(config={
    #     'extra-imports': ['a2_part3', 'datetime', 'json', 'python_ta.contracts'],
    #     'max-line-length': 100,
    #     'disable': ['R1705'],
    #     'allowed-io': ['read_course_data']
    # })
