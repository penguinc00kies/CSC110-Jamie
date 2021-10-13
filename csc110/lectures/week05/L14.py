"""CSC110 Lecture 14 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
from dataclasses import dataclass
import datetime


####################################################################################################
# Exercise 1
####################################################################################################
def move_item(items: list, other_items: set) -> None:
    """Remove the first item from items and add it to other_items.

    Preconditions:
        - items != []


    >>> numbers_list = [1, 2, 3]
    >>> numbers_set = {10, 20}
    >>> move_item(numbers_list, numbers_set)
    >>> numbers_list
    [2, 3]


    >>> numbers_set == {10, 20, 1}
    True
    """
    set.add(other_items, list.pop(items, 0))




####################################################################################################
# Demo 1
####################################################################################################
def squares(nums: list[int]) -> list[int]:
    """Return a list of the squares of the given numbers.

    >>> squares([1, 2, 3])
    [1, 4, 9]
    """
    # return [num ** 2 for num in nums]

    # squares_so_far = []

    # for num in nums:
    # using '+=' on a list is not reassignment, it calls list.extend, so use it only on immutable types
    # the below is a reassignment
    #     squares_so_far = squares_so_far + [num ** 2]
    # return squares_so_far

    # for num in nums:
    # the below is mutation
    #     list.append(squares_so_far, num ** 2)
    # return squares_so_far


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

    Representation Invariant omitted.
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


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


def filter_by_name(data: list[MarriageData], name: str) -> list[MarriageData]:
    """Return all rows in data with the matching civic centre <name>.

    Equivalent to:
      [row for row in data if row.civic_centre == name]
    """
    rows_so_far = []
    for row in data:
        if row.civic_centre == name:
            list.append(rows_so_far, row)
    return rows_so_far

def num_issued_by(data: list[MarriageData], centre: str) -> set[int]:
    """Return the unique numbers of marriage licenses issued in a month at the
    given civic centre.

    Equivalent to:
      {row.num_licenses for row in data if row.civic_centre == name}
    """
    licenses_so_far = set()
    for row in data:
        if row.civic_centre == centre:
            set.add(licenses_so_far, row.num_licenses)
    return licenses_so_far


def marriages_by_centre(data: list[MarriageData], month: datetime.date) -> dict[str, int]:
    """Return mapping from civic centre name to the number of marriage licenses
    issued by that centre in the given month.

    Preconditions:
        - Each civic centre has only one row of MarriageData for the given month.

    Equivalent to:
      {row.civic_centre: row.num_licenses for row in data if row.month == month}
    """
    dict_so_far = {}
    for row in data:
        if row.month == month:
            dict_so_far[row.civic_centre] = row.num_licenses
    return dict_so_far


####################################################################################################
# Demo 2
####################################################################################################
def total_marriages_by_centre(data: list[MarriageData]) -> dict[str, int]:
    """Return mapping from civic centre name to the total number of marriage licenses ever
    issued by that centre.
    """
    dict_so_far = {}
    for row in data:
        # if row.civic_centre not in dict_so_far:
        #     dict_so_far[row.civic_centre] = row.num_licenses
        # else:
        #     dict_so_far[row.civic_centre] += row.num_licenses

        if row.civic_centre not in dict_so_far:
            dict_so_far[row.civic_centre] = 0
        # unconditional branches are very useful for debugging
        dict_so_far[row.civic_centre] += row.num_licenses
    return dict_so_far
