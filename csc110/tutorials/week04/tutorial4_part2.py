"""CSC110 Tutorial 4: Data Classes and For Loops, Exercise 2

Module Description
==================
This module contains a set of erroneous functions involving for loops.

Run this file in the Python interpreter, and call the doctests for each function
one at a time. This will start pdb (the Python debugger), which you can use to
step through the function body and identify the exact line of code where an
error occurs.

Useful pdb commands:
    - next (execute the current line of code)
    - continue (stop pdb and keep running the current code)
    - list (show the current line of code and surrounding lines)
    - any valid Python expression/statement: evaluate/execute that code
        (same as Python console)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
from typing import Iterable, List, Set


def monkeys_in_barrel(barrel: List[str]) -> int:
    """Return the number of time 'monkey' appears in the barrel.

    >>> monkeys_in_barrel(['monkey', 'David', 'monkey'])
    2
    """
    # breakpoint()
    # for item in barrel:
    #     if item == 'monkey':
    #         monkey_count_so_far = monkey_count_so_far + 1
    # return monkey_count_so_far
    # Missing initial assignment statement for monkey_count_so_far
    monkey_count_so_far = 0
    for item in barrel:
        if item == 'monkey':
            monkey_count_so_far = monkey_count_so_far + 1
    return monkey_count_so_far



def total_string_size(strings: Iterable[str]) -> int:
    """Return the total length of the given strings.

    >>> total_string_size({'Hello', 'a', 'David is cool'})
    19
    """
    # breakpoint()
    # total_size = 0
    # for s in strings:
    #     total_size = len(s)
    # return total_size
    # total_size is not accumulating, it's just being reassigned each iteration
    total_size = 0
    for s in strings:
        total_size = total_size + len(s)
    return total_size


def total_vowels(strings: Iterable[str]) -> int:
    """Return the total number of vowels found in the given strings.

    >>> total_vowels({'Hello', 'a', 'David is cool'})
    8
    """
    # breakpoint()
    # for s in strings:
    #     vowel_count_so_far = 0
    #     for char in s:
    #         if char in 'aeiou':
    #             vowel_count_so_far += 1
    #
    # return vowel_count_so_far
    # vowel_count_so_far resets every time we iterate through strings
    vowel_count_so_far = 0
    for s in strings:
        for char in s:
            if char in 'aeiou':
                vowel_count_so_far += 1
    return vowel_count_so_far


def has_special(strings: Iterable[str]) -> bool:
    """Return whether there is a special string in the given collection of strings.

    We say that a string is special when it has length >= 2 and it starts and ends
    with the same character.

    >>> has_special(['a', 'bc', 'david'])
    True
    """
    # breakpoint()
    # for s in strings:
    #     if len(s) >= 2 and s[0] == s[-1]:
    #         return True
    #     else:
    #         return False
    # Don't return false, it terminates the whole function
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            return True
    return False


def any_divisible_by(numbers: Iterable[int], d: int) -> bool:
    """Return whether any of the given numbers is divisible by d.

    >>> any_divisible_by({101, 13, -57}, 25)
    False
    """
    # breakpoint()
    # for n in numbers:
    #     if n % d != 0:
    #         return True
    #
    # return False
    # The condition is checking if n is not divisible by d, it's checking the negation of what we want
    for n in numbers:
        if n % d == 0:
            return True

    return False


def bonus_score(strings: Iterable[str], bonus_chars: Set[str]) -> int:
    """Return the total "bonus score" for the given strings and bonus_chars.

    The "bonus score" is calculated as follows:
        - for each string in strings, calculate the number of characters in
          the string that are also in bonus_chars
        - if there are 3 or more such characters, add the number of characters
          to the total bonus score

    Preconditions:
        - all({len(c) == 1 for c in bonus_chars})

    >>> bonus_score(['David', 'Mario', 'Banana', 'CSC110'], {'M', 'a', 'r', 'i', 'o'})
    8
    """
    # breakpoint()
    # total_bonus_so_far = 0
    # string_bonus_so_far = 0
    #
    # for s in strings:
    #     for char in s:
    #         if char in bonus_chars:
    #             string_bonus_so_far = string_bonus_so_far + 1
    #
    #     if string_bonus_so_far >= 3:
    #         total_bonus_so_far = total_bonus_so_far + string_bonus_so_far
    #
    # return total_bonus_so_far
    # string_bonus_so_far isn't reset after each iteration through a string
    total_bonus_so_far = 0
    string_bonus_so_far = 0

    for s in strings:
        string_bonus_so_far = 0
        for char in s:
            if char in bonus_chars:
                string_bonus_so_far = string_bonus_so_far + 1

        if string_bonus_so_far >= 3:
            total_bonus_so_far = total_bonus_so_far + string_bonus_so_far

    return total_bonus_so_far
