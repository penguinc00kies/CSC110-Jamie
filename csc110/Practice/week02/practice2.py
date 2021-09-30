"""CSC110 Extra MarkUs Practice Solutions - Week 2

Instructions (READ THIS FIRST!)
===============================

Complete the function(s) in this module according to their docstring.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TO-DO comment---this is a
good habit to get into early! To check your work, you should run this file in
the Python console and then call each function manually.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""


def generate_sequence(lst: list[int]) -> list[int]:
    """Return a new list that contains the sequence of integers between the minimum and maximum of
    lst, inclusive.

    When the minimum and maximum of lst are the same, the list should only contain one element.

    Assume that len(lst) >= 1.

    >>> generate_sequence([2])
    [2]
    >>> generate_sequence([15, 19, 18])
    [15, 16, 17, 18, 19]
    """
    return [x for x in range(min(lst), max(lst) + 1)]


def max_occurrences(string_set: set[str], substring: str) -> int:
    """Return the maximum number of times substring appears in any of the strings in string_set.

    >>> max_occurrences({'Montreal', 'Toronto', 'Halifax', 'Ottawa'}, 'a')
    2
    >>> max_occurrences({'Montreal', 'Toronto', 'Halifax', 'Ottawa'}, 'tt')
    1
    """
    return max([x.count(substring) for x  in string_set])


def longest_string_starts_with(string_set: set[str], prefix: str) -> str:
    """Return the longest string in string_set that starts with prefix.

    Assume that:
        - no two strings in string_set that start with prefix have the same length.
        - at least one string in string_set starts with prefix.

    Consider using the following algorithm:
        1. Create a list1 of the strings in string_set that begin with prefix. See the notes on
           filtering comprehensions and str.startswith.
        2. Create a list2 that corresponds with list1, except the elements are the length of each
           string. Order matters!
        3. Find the index of the maximum length in list2. See built-ins list.index and max.
        4. list1 and list2 should have the same number of elements and the same order. So the index
           from list2 in step 3 can be used as an index for list1.

    Can you think of different ways to solve the problem? See what you can do when you restrict
    yourself to concepts from specific chapters. Remember you can re-submit and re-test practice
    exercises on MarkUs.

    >>> longest_string_starts_with({'David', 'Doe', 'Disturbance'}, 'D')
    'Disturbance'
    >>> longest_string_starts_with({'David', 'Disturbance', 'Money', 'Monday', 'Mothers'}, 'Mon')
    'Monday'
    """
    valid_strings = [x for x in string_set if x.startswith(prefix)]
    valid_strings.sort(key=len)
    return valid_strings[len(valid_strings)-1]

# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'max-line-length': 100,
#         'max-nested-blocks': 4
#     })
#
#     import python_ta.contracts
#     python_ta.contracts.check_all_contracts()
#
#     import doctest
#     doctest.testmod()
