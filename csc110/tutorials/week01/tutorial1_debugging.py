"""CSC110 Tutorial 1: Data and Functions (Exercise 3)

Module Description
==================
This file contains all of the code snippets from Exercise 3: Debugging Corner.
Feel free to try to fix each code snippet in this file (and note that if you're
using PyCharm, some errors will be highlighted for you already---though some
errors in earlier code snippet may interfere with PyCharm detecting errors in
later code snippets).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Mario Badr.
"""

###############################################################################
# Syntax Errors
###############################################################################
5 = x

numbers = [1 2 3]

message = Hello
World!


fruit_to_color = {
    'banana': 'yellow',
    'kiwi': 'green'
            'blueberries': 'blue'}


result0 = max
{3, 4}


def is_same_length(list0: list, list2: list) -> bool


# Function body omitted


def is_much_greater(num0: int, num2: int) -> bool:
    return num0 >= 2 * num2


###############################################################################
# Name Errors
###############################################################################
my_number = 10
result1 = 15 + my_nubmer

result2 = Sum([1, 2, 3])


def repeat(string: str) -> str:
    return s + s


result3 = repeat('Hello')

###############################################################################
# Type Errors
###############################################################################
result4 = [1, 2, 3] + 4

x = 'hi'
y = 5
result5 = x + y

numbers = {1, 2, 3}
result6 = numbers[0]

x = [1, 2, 3]
result7 = x[2.5]


def add_incorrect(n: int) -> int:
    return n + 'one'


result8 = add_incorrect(3)

###############################################################################
# Other errors
###############################################################################
nums = [110, 111, 200]
n0 = nums[0]  # 110
n1 = nums[1]  # 111
n2 = nums[2]  # 200
n3 = nums[3]  # Error!

result9 = 1 // 0

empty_list = []
result10 = max(empty_list)
