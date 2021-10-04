"""CSC110 Lecture 11 - Starter file

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
# Exercise 2
####################################################################################################
@dataclass
class Student:
    """A student at the University of Toronto.

    Representation Invariants:
        - len(self.given_name) > 0
        - len(self.family_name) > 0
        - self.year_of_study > 0
        - len(self.utorid) == 8
        - self.utorid.isalnum() == True
    """
    given_name: str
    family_name: str
    year_of_study: int
    utorid: str


@dataclass
class Cssu:
    """The Computer Science Student Union at the University of Toronto.

    Instance Attributes:
        - execs: A mapping from executive role (president, treasurer, etc.)
                 to Student.
        - merch: A mapping from clothing item (t-shirt, hoodie, etc.)
                 to price.

    Representation Invariants:
        - all([self.merch[x] >= 0 for x in self.merch])
        - all([str.isalpha(x) for x in self.execs])
        - all([self.execs[x] != self.execs[y] for x \
            in self.execs for y in self.execs if x != y])
    """
    execs: dict[str, Student]
    merch: dict[str, float]


####################################################################################################
# Exercise 3
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
        - self.civic_centre in {'TO', 'ET', 'NY', 'SC'}
        - self.num_licenses >= 0
        - self.month.day == 1

    >>> some_data = MarriageData(123, 'ET', 54, datetime.date(2011, 1, 1))
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


def civic_centres(data: list[MarriageData]) -> set[str]:
    """Return a set of all the civic centres found in data.
    """
    return {x.civic_centre for x in data}


def civic_centre_meets_threshold(data: list[MarriageData], civic_centre: str,
                                 num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every
    month.

    You only need to worry about the rows that appear in data; don't worry about
    "missing" months.

    Preconditions:
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}

    HINT: you'll need to use a list comprehension with a filter.
    """
    filtered_data = [x for x in data if x.civic_centre == civic_centre]
    return all([x.num_licenses >= num for x in filtered_data])


def issued_licenses_in_range(data: list[MarriageData], start: datetime.date,
                             end: datetime.date) -> int:
    """Return the number of marriage licenses issued between start and end,
    inclusive.

    Preconditions:
        - end > start

    HINT: You can use <, <=, >, and >= to compare date values chronologically.
    """
    return sum([x.num_licenses for x in data if start <= x.month <= end])


####################################################################################################
# Sample data for Exercise 3
####################################################################################################
marriage_data = [
    MarriageData(1657, 'ET', 80, datetime.date(2011, 1, 1)),
    MarriageData(1658, 'NY', 136, datetime.date(2011, 1, 1)),
    MarriageData(1659, 'SC', 159, datetime.date(2011, 1, 1)),
    MarriageData(1660, 'TO', 367, datetime.date(2011, 1, 1)),
    MarriageData(1661, 'ET', 109, datetime.date(2011, 2, 1)),
    MarriageData(1662, 'NY', 150, datetime.date(2011, 2, 1)),
    MarriageData(1663, 'SC', 154, datetime.date(2011, 2, 1)),
    MarriageData(1664, 'TO', 383, datetime.date(2011, 2, 1))
    ]


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'dataclasses'],
        'max-line-length': 100,
        'disable': ['R1705']
    })
