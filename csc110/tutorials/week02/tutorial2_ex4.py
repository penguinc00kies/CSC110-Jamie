"""CSC110 Tutorial 2: Functions and Logic (Exercise 4)

Module Description
==================
This module contains the functions you will implement for Exercise 4.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import tutorial2_words


def num_differing_characters(s1: str, s2: str) -> int:
    """Return the number of letter positions where s1 and s2 differ.

    Compare s1 and s2 letter by letter (so s1[0] vs. s2[0], s1[1] vs. s2[1], etc.)

    You may ASSUME that:
        - s1 and s2 have the same length
        - s1 and s2 are both non-empty
        - s1 and s2 consist of only lowercase letters (a-z)

    >>> num_differing_characters('the', 'tre')
    1
    >>> num_differing_characters('banana', 'amazon')
    6

    HINT: you can use range(0, len(s1)) in a comprehension to get the indexes
    where s1 and s2 differ.
    """


def is_suggestion(s1: str, s2: str) -> bool:
    """Return whether s2 is a suggestion for s1.

    You may ASSUME that:
        - s1 and s2 are non-empty
        - si and s2 consist of only lowercase letters
        - s2 is a valid English word

    >>> is_suggestion('tre', 'the')
    True
    >>> is_suggestion('tre', 'tree')
    False
    """


def get_suggestions(s: str) -> list:
    """Return the list of valid English words that are suggestions for s, sorted alphabetically.

    Uses the set of words WORDS imported from tutorial2_words.py.
    s may or may not be a valid English word.

    You can sort a list of lowercase strings alphabetically by using the builtin sorted function.

    You may ASSUME that:
        - s is non-empty
        - s contains only lowercase letters (a-z)

    >>> get_suggestions('tre')
    ['are', 'the', 'toe']

    Hint: you can use "for word in tutorial2_words.WORDS" in a comprehension to access the
    different valid English words.
    """


def autocorrect_word(s: str) -> str:
    """Return an autocorrected version of s.

    Return s itself if it is a valid English word (i.e., is in tutorial2_words.WORDS) or
    has no suggestions, and its first (in alphabetical order) suggestion if it is invalid
    but has at least one suggestion.

    >>> autocorrect_word('the')
    'the'
    >>> autocorrect_word('tre')
    'are'
    >>> autocorrect_word('hiiiii')
    'hiiiii'
    """


def autocorrect_words(words: list) -> list:
    """Return a list containing autocorrected versions of each string in strings.

    Hint: Use a list comprehension on strings, calling autocorrect_word on each one.

    You may ASSUME that:
        - Every element of strings is a valid argument to autocorrect_word.

    >>> autocorrect_words(['you', 'tre', 'zool'])
    ['you', 'are', 'cool']
    """


def autocorrect_text(text: str) -> str:
    """Return an autocorrected version of text.

    Here, text is a string containing lowercase letter words separated by spaces.
    The returned string should have an autocorrected version of each word in the
    given text.

    You may ASSUME that:
        - text consists of words separated by a single space
        - each word in the given text consists of only lowercase letters

    >>> autocorrect_text('you tre zool')
    'you are cool'

    HINTS:
        - You've already seen str.split on Prep 2, which can convert from a string
          to a list of words.
        - The opposite is str.join, which takes a separator string and a list of
          strings, and joins the strings together into one string, using the
          given separator string in between.

          >>> str.join(' ', ['David', 'is', 'cool'])
          'David is cool'
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # Try uncommenting the following lines to run python_ta to check your work in this file.
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['tutorial2_words'],
    #     'max-line-length': 100,
    #     'disable': ['R1705']
    # })
