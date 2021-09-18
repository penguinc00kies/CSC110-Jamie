"""CSC110 Fall 2020 Prep 2: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
Your task is to complete this module by doing the following for EACH function below:

1. Add a new doctest example to the function description in the space provided.
   This will ensure you understand what the function is supposed to do.
2. Write the body of the function so that it does what its description claims.

In some function descriptions, we have written "You may ASSUME..." This means that
when you are writing each function body, you only have to consider possible values
for the parameters that satisfy these assumptions.

We have marked each place you need to write a doctest/code with the word "TODO".
As you complete your work in this file, delete each TO-DO comment---this is a
good habit to get into early! To check your work, you should run this file in
the Python console and then call each function manually (you can also copy-and-paste)
with your doctest examples, and possibly other examples.

(We'll cover more techniques for testing your code this week.)

By the way, we *will* be checking that you've added new doctest examples, and that
your examples correctly illustrate a call to that function. Don't skip this!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""


def total_slices(num_pizzas: int, slices_per_pizza: int) -> int:
    """Return the total number of pizza slices in `num_pizzas` pizzas.

    One pizza has `slices_per_pizza` slices.

    You may ASSUME that num_pizzas and slices_per_pizza are both >= 0.

    >>> total_slices(5, 8)  # 5 pizzas with 8 slices per pizza
    40
    >>> # TODO: write another doctest example
    >>> total_slices(0, 6)
    6
    """
    # TODO: Complete this function body.
    return num_pizzas * slices_per_pizza


def scale_grade(original_grade: float, multiplier: float, bonus: float) -> float:
    """Return an adjusted grade.

    The original grade is first multiplied by the given multiplier,
    and then the result is added to the given bonus.

    Grades are capped at 100.0; if the scaling causes the grade to exceed 100.0,
    100.0 is returned instead.

    You may ASSUME that the original_grade, multiplier, and bonus are all >= 0.

    >>> scale_grade(60.0, 1.2, 10.0)  # 60.0 * 1.2 = 72.0, and 72.0 + 10.0 = 82.0
    82.0
    >>> # TODO: write another doctest example
    >>> scale_grade(50.0, 2.0, 5.0)
    100.0

    HINT: one of the max or min functions is useful.
    """
    # TODO: Complete this function body.
    return min(100.0, original_grade * multiplier + bonus)


def first_characters(strings: set) -> set:
    """Return a set containing all of the first characters of the given strings.

    You may ASSUME that all of the given strings are non-empty.
    (An empty string has no first character!)

    >>> letters = first_characters({'David', 'is', 'cool'})
    >>> letters == {'D', 'i', 'c'}
    True
    >>> # TODO: write another doctest example (follow the same format as the given one)
    >>> initials = first_characters({'John', 'Alexander', 'Macdonald'})
    >>> initials == {'J', 'A', 'M'}
    True

    HINT: use a set comprehension (review Section 1.5 of the Course Notes).
    You may also need to review Section 1.3 for how to extract a single character
    from a string.
    """
    # TODO: Complete this function body.
    return {word[0] for word in strings}


def scale_grades(original_grades: list, multiplier: float, bonus: float) -> list:
    """Return a list of adjusted grades.

    original_grades is a list of floats representing the original grades.
    The multiplier and bonus parameters have the same role as with scale_grade.
    Each grade is adjusted in the way described in scale_grade above.

    You may ASSUME that the original grades, multiplier, and bonus are all >= 0.

    >>> scale_grades([10.0, 20.2], 1.5, 3.0)
    [18.0, 33.3]
    >>> # TODO: write another doctest example
    >>> scale_grades([43.7, 88.0], 1.1, 2.0)
    [50.07, 98.8]

    HINT: use a list comprehension, and call your scale_grade function on each
    original grade.
    """
    # TODO: Complete this function body.
    return [grade * multiplier + bonus for grade in original_grades]


def word_lengths(text: str) -> dict:
    """Return a dictionary mapping the words in text to their lengths.

    In the returned dictionary, each key is a word that appears in text,
    and its corresponding value is its length (number of characters).

    In the given text, words are separated by one or more spaces.

    >>> result = word_lengths('David is   cool')
    >>> result == {'David': 5, 'is': 2, 'cool': 4}
    True
    >>> # TODO: write another doctest example (follow the same format as the given one)
    >>> initials = word_lengths('John Alexander Macdonald')
    >>> initials == {'John': 4, 'Alexander': 9, 'Macdonald': 9}
    True

    HINT: this is a bit longer than the previous functions. Try the following
    approach:

        1. Split the given text into words using the str.split method.
           (Review Section 2.1 if you aren't sure about "methods".)
           Store the resulting value in a variable.
        2. Use a dictionary comprehension on the result of Step 1.
    """
    # TODO: Complete this function body.
    words = str.split(text)
    return {words[x]: len(words[x]) for x in range(len(words))}

