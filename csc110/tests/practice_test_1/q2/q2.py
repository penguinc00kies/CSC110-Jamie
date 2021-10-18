"""CSC110 Fall 2021: Mock Term Test, Question 2

Module Description
==================
This Python file contains instructions for this question. There is only ONE
part to this question (for the real term test you may see multiple parts).
The comments in this file contain instructions on how to complete this question,
so please read those comments carefully.

At the bottom of the file we've provided code to run doctest and python_ta.
This is NOT required for grading, but you may find these tools helpful when
completing this question.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""
from dataclasses import dataclass


# This is the definition of the data class you'll use for this question.
# Don't change this!
@dataclass
class MovieData:
    """A data class that represents a movie.

    Instance Attributes:
        - name: The name of the movie
        - scifi: Yes if the movie is science fiction, No otherwise
        - score: The movie's rating on IMDb

    Representation Invariants:
        - 0.0 <= self.score <= 10.0
        - self.scifi in {'Yes', 'No'}

    >>> movie_1 = MovieData('1', 'Yes', 9.5)
    """
    name: str
    scifi: str
    score: float


# Your task is to implement the following function by filling in to the TODOs.
def is_scifi(data: MovieData) -> bool:
    """TODO: Include a description of the function and remove this todo

    TODO: Include two doctest examples and remove this todo
    """
    # TODO: Implement the function body and remove this todo


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'dataclasses'],
        'max-line-length': 100
    })

    import doctest
    doctest.testmod()
