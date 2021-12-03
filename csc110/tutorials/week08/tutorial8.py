"""CSC110 Tutorial 8: Asymptotic Notation and Algorithm Running-Time Analysis

Module Description
==================
This module contains code for the timing experiments you'll run on the brute-force
algorithm for breaking the Diffie-Hellman key exchange.

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
import timeit
from typing import List, Tuple
import plotly
import plotly.express as px


###############################################################################
# Brute-force algorithm to break Diffie-Hellman (from lecture)
###############################################################################
def break_diffie_hellman(p: int, g: int, g_a: int, g_b: int) -> int:
    """Return the shared Diffie-Hellman secret key obtained from the eavesdropped information.

    Preconditions:
        - p, g, g_a, and g_b are the values exhanged between Alice and Bob
          in the Diffie-Hellman algorithm

    >>> p = 23
    >>> g = 2
    >>> g_a = 9  # g ** 5 % p
    >>> g_b = 8  # g ** 14 % p
    >>> break_diffie_hellman(p, g, g_a, g_b)  # g ** (5 * 14) % p
    16
    """
    secret_a = 1
    for possible_a in range(1, p):
        if pow(g, possible_a, p) == g_a:
            secret_a = possible_a

    # Note: 1 <= secret_a < p
    return pow(g_b, secret_a, p)


###############################################################################
# Timing experiments and visualization for break_diffie_hellman
###############################################################################
def time_to_break_diffie_hellman(p: int, g: int, g_a: int, g_b: int, number: int) -> float:
    """"Return the time taken to run break_diffie_hellman on the given arguments p, g, g_a, g_b.

    number is the number of times to execute the statement, and should be passed into timeit.timeit.

    IMPORTANT NOTE:
        you must pass in an additional argument "globals=globals()" to the timing function:

        timeit.timeit(..., number=..., globals=globals()),

        otherwise you'll get a NameError when calling timeit.timeit.

    Remember, the first argument of `timeit.timeit` is a *string* that represents the code
    to execute; it is up to you to construct the correct string expressing a call to
    break_diffie_hellman.

    Preconditions:
        - p, g, g_a, and g_b are the values exhanged between Alice and Bob
          in the Diffie-Hellman algorithm
        - number >= 1

    >>> time = time_to_break_diffie_hellman(23, 2, 9, 8, 1000)
    """

    time_so_far = 0
    secret_a = 1
    for possible_a in range(1, p):
        time_so_far += timeit.timeit('1 + 1', number=number, globals=globals())
        if pow(g, possible_a, p) == g_a:
            secret_a = possible_a

    return time_so_far


def time_diffie_hellman_runs(filename: str) -> List[Tuple[int, float]]:
    """Return the time taken to break the runs of Diffie-Hellman contained in the given file.

    The return value is a *list of tuples*, where each tuple corresponds to one row of the
    csv file, and contains the following data:
        - the first element of the tuple is the *prime p* used in the run
        - the second element of the tuple is the time taken by break_diffie_hellman
          to run on the corresponding row

    Preconditions:
        - filename refers to a CSV file in the format specified on the tutorial handout

    Note: you should call time_to_break_diffie_hellman. Pass in 1 as the number of times to run.
    """
    with open(filename) as file:
        return_list = []
        reader = csv.reader(file)
        for row in reader:
            data = process_row(row)
            time = time_to_break_diffie_hellman(data[0], data[1], data[2], data[3], 1)
            return_list.append((data[0], time))

        return return_list


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
        int(row[0]),  # p
        int(row[1]),  # g
        int(row[2]),  # g_a
        int(row[3]),  # g_b
    ]


def visualize_break_diffie_hellman_times(timing_data: List[Tuple[int, float]]) -> None:
    """Visualize the results of the timing experiments completed by time_diffie_hellman_runs.

    Use a plotly *scatterplot* to visualize the data. You can adapt the code we provided you
    back in Assignment 1, Part 4 (Simple Linear Regression).
    """
    fig = px.scatter(x=[data[0] for data in timing_data], y=[data[1] for data in timing_data])
    fig.show()


if __name__ == '__main__':
    import python_ta.contracts
    #
    # python_ta.contracts.check_all_contracts()
