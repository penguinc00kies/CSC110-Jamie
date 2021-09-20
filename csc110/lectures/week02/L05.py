"""CSC110 Lecture 5 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""


####################################################################################################
# Exercise 1: Function design practice
####################################################################################################
def check_lengths(strings: list, max_length: int) -> bool:
    """Returns if max_length is greater than the length of the longest string in strings

    Assume that strings is not empty

    >>> check_lengths(['cat', 'no', 'maybe'], 4)
    False
    >>> check_lengths(['grape', 'banana', 'pear'], 20)
    True
    """
    return max([len(x) for x in strings]) < max_length


def string_lengths(strings: list) -> dict:
    """Returns a dictionary of the lengths of each element in strings mapped to that element in strings

    >>> string_lengths(['aaa', 'david']) == {'aaa': 3, 'david': 5}
    True
    >>> string_lengths(['John', 'Alexander', 'Macdonald']) == {'John': 4, 'Alexander': 9, 'Macdonald': 9}
    True
    """
    return {s: len(s) for s in strings}

# TODO: Given a float representing the price of a product and another float representing a tax rate
#  (e.g., a 13% tax rate represented as the float value 0.13), calculate the after-tax cost of the product.
def taxed_price(item_price: float, tax_rate: float) -> float:
    """Returns a taxed price of an item that costs item_price taxed at a rate of tax_rate
    >>> taxed_price(1.00, 0.13)
    1.13
    >>> taxed_price(5.00, 0.4)
    7.0
    """
    return item_price + item_price * tax_rate

# TODO: given a dictionary mapping names of products (as strings) to prices (as floats), which represents
#  a customer order at a store, and a tax rate, calculate the total after-tax cost of the products.
def taxed_total(order: dict, tax_rate: float) -> float:
    """Returns a taxed total of the prices of the items in order at a rate of tax_rate
    >>> taxed_total({'grapes': 2.00, 'apple': 1.00}, 0.13)
    3.39
    >>> taxed_total({'bread': 4.50, 'ham': 3.10}, 0.2)
    9.12
    """
    prices = {order[x] for x in order}
    return sum(prices) + sum(prices) *  tax_rate
####################################################################################################
# Exercise 2: Function design practice, math edition
####################################################################################################
# TODO: Given three side lengths of a triangle (as floats), calculate the angles in the triangle.
import math
# def calculate_angles(side_a: float, side_b: float, side_c: float) -> tuple:
    #"""Returns a tuple of 3 angles in degrees of a triangle given the triangle has side1, side2, and side3

    #The angeles in the tuple are ordered by...
    #>>> calculate_angles(2.0, 2.0, 3.0)
    #{43.71931114, 43.71931114, 97.18075578}
    #"""
    # angle1 = (side_a**2 - side_b**2 - side_c**2)/(-2*side_b*side_c)
    # return

####################################################################################################
# Additional exercises
####################################################################################################
