"""CSC110 Lecture 12 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
from dataclasses import dataclass
from typing import Iterable

import datetime


####################################################################################################
# Demo
####################################################################################################
def my_sum(numbers: list[int]) -> int:
    """Return the sum of the given numbers.

    >>> my_sum([10, 20, 30])
    60my
    """
    breakpoint()
    # ACCUMULATOR sum_so_far: keep track of the running sum of the elements in numbers
    sum_so_far = 0

    for number in numbers:
        sum_so_far = sum_so_far + number

    # sum_so_far = sum_so_far + numbers[0]
    # sum_so_far = sum_so_far + numbers[1]
    # sum_so_far = sum_so_far + numbers[2]

    return sum_so_far


def average_menu_price(menu: dict[str, float]) -> float:
    """Return the average price of an item from the menu.

    >>> average_menu_price({'fries': 3.5, 'hamburger': 6.5})
    5.0
    """
    # ACCUMULATOR len_so_far: keep track of the number of
    # items in the menu seen so far in the loop.
    len_so_far = 0
    # ACCUMULATOR total_so_far: keep track of the cost of
    # all items in the menu seen so far in the loop.
    total_so_far = 0.0

    for item in menu:
        len_so_far = len_so_far + 1
        total_so_far = total_so_far + menu[item]

    return total_so_far / len_so_far


def count_vowels(s: str) -> int:
    """Return the number of vowels in s.

    >>> count_vowels('aeiou')
    5
    >>> count_vowels('David')
    2
    """
    # ACCUMULATOR vowels_so_far: keep track of the number of vowels
    # seen so far in the loop.
    vowels_so_far = 0

    for letter in s:
        if letter in 'aeiou':
            vowels_so_far = vowels_so_far + 1

    return vowels_so_far


def starts_with_v3(strings: Iterable[str], char: str) -> bool:
    """..."""
    for s in strings:
        if s[0] == char:
            return True
    return False


####################################################################################################
# Exercise 1
####################################################################################################
def sum_of_squares(numbers: list[int]) -> int:
    """Return the sum of the squares of the given numbers.

    >>> sum_of_squares([4, -2, 1])  # 4 ** 2 + (-2) ** 2 + 1 ** 2
    21
    """
    sum_so_far = 0

    for number in numbers:
        sum_so_far = sum_so_far + number ** 2

    return sum_so_far


def long_greeting(names: list[str]) -> str:
    """Return a greeting message that greets every person in names.

    Each greeting should have the form "Hello <name>! " (note the space at the end).
    The returned string should be the concatenation of all the greetings.

    >>> long_greeting(['David', 'Mario'])  # Note the "extra" space at the end
    'Hello David! Hello Mario! '
    """
    extended_greeting = ''
    for name in names:
        extended_greeting = extended_greeting + 'Hello ' + name + '! '

    return extended_greeting

####################################################################################################
# Exercise 2
####################################################################################################
@dataclass
class MarriageData:
    """A record of the number of marriage licenses issued in a civic centre
    in a given month.

    Instance Attributes:
      - id: a unique identifier for the record
      - civic_centre: the name of the civic centre
      - num_licenses: the number of licenses issued
      - month: the month these licenses were issued

    Representation Invariants:
        - self.civic_centre in {'ET', 'NY', 'TO', 'SC}
        - self.num_licenses >= 0
        - self.month.day == 1

    >>> some_data = MarriageData(123, 'ET', 54, datetime.date(2011, 1, 1))
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


def create_nested_list_data() -> list[list]:
    """Return a small sample of the marriage data dataset."""
    return [
        [1657, 'ET', 80, datetime.date(2011, 1, 1)],
        [1658, 'NY', 136, datetime.date(2011, 1, 1)],
        [1659, 'SC', 159, datetime.date(2011, 1, 1)],
        [1660, 'TO', 367, datetime.date(2011, 1, 1)],
        [1661, 'ET', 109, datetime.date(2011, 2, 1)],
        [1662, 'NY', 150, datetime.date(2011, 2, 1)],
        [1663, 'SC', 154, datetime.date(2011, 2, 1)],
        [1664, 'TO', 383, datetime.date(2011, 2, 1)]
    ]


def create_dataclass_data() -> list[MarriageData]:
    """Return a small sample of the marriage data dataset."""
    return [
        MarriageData(1657, 'ET', 80, datetime.date(2011, 1, 1)),
        MarriageData(1658, 'NY', 136, datetime.date(2011, 1, 1)),
        MarriageData(1659, 'SC', 159, datetime.date(2011, 1, 1)),
        MarriageData(1660, 'TO', 367, datetime.date(2011, 1, 1)),
        MarriageData(1661, 'ET', 109, datetime.date(2011, 2, 1)),
        MarriageData(1662, 'NY', 150, datetime.date(2011, 2, 1)),
        MarriageData(1663, 'SC', 154, datetime.date(2011, 2, 1)),
        MarriageData(1664, 'TO', 383, datetime.date(2011, 2, 1))
    ]


def total_licenses_for_centre_v1(data: list[list], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre."""
    return sum([row[2] for row in data if row[1] == civic_centre])


def total_licenses_for_centre_v2(data: list[MarriageData], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre."""
    return sum([row.num_licenses for row in data if row.civic_centre == civic_centre])


def total_licenses_for_centre_v3(data: list[MarriageData], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre."""
    # ACCUMULATOR
    licences_issued_so_far = 0

    for row in data:
        if row.civic_centre == civic_centre:
            licences_issued_so_far = licences_issued_so_far + row.num_licenses

    return licences_issued_so_far


def civic_centre_meets_threshold_v1(data: list[list], civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data; don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}
        - data satisfies all of the properties described in Worksheet 9, Exercise 2
    """
    licenses_issued = [row[2] for row in data if row[1] == civic_centre]
    return all(num_issued >= num for num_issued in licenses_issued)


def civic_centre_meets_threshold_v2(data: list[MarriageData], civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data; don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}
    """
    licenses_issued = [row.num_licenses for row in data if row.civic_centre == civic_centre]
    return all(num_issued >= num for num_issued in licenses_issued)


def civic_centre_meets_threshold_v3(data: list[MarriageData], civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data; don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}
    """
    threshold_met_so_far = []

    breakpoint()
    for licenses in data:
        if licenses.civic_centre == civic_centre:
            threshold_met_so_far = threshold_met_so_far + [(licenses.num_licenses >= num)]

    return all(threshold_met_so_far)


####################################################################################################
# Exercise 3
####################################################################################################
def count_uppercase(s: str) -> int:
    """Return the number of uppercase letters in s.
    """
    num_of_uppercase = 0

    for char in s:
        if str.isupper(char):
            num_of_uppercase = num_of_uppercase + 1

    return num_of_uppercase


def all_fluffy(s: str) -> bool:
    """Return whether every character in s is fluffy.

    Fluffy characters are those that appear in the word 'fluffy'.
    """

    num_of_fluffy_chars = []

    for char in s:
        if not (char in 'fluffy'):
            return False

    return True


def sum_davids(scores: dict[str, int]) -> int:
    """Return the sum of all values in scores that correspond to a key that contains 'David'."""
    sum_of_scores = 0
    for key in scores:
        if 'David' in key:
            sum_of_scores = sum_of_scores + scores[key]

    return sum_of_scores


def david_vs_mario(scores: dict[str, int]) -> str:
    """Return the name of the person with the highest total score in scores.

    David's score is the sum of all values in scores that correspond
    to a key that contains the string 'David'.

    Mario's score is the sum of all values in scores that correspond
    to a key that contains the string 'Mario'.
    """
    davids_score = sum_davids(scores)
