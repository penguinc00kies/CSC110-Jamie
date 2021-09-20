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
def calculate_angles(side_a: float, side_b: float, side_c: float) -> tuple:
    """Returns a tuple of 3 angles in degrees of a triangle given the triangle has side_a, side_b, and side_c

    The first angle in the tuple is the angle opposite of side_a, the second angle is opposite of side_b,
    and the third angle is opposite of side_c
    >>> calculate_angles(2.0, 2.0, 3.0)
    (41.40962210927086, 41.40962210927086, 97.18075578145829)
    """
    angle_a = (math.acos((side_a**2 - side_b**2 - side_c**2)/(-2*side_b*side_c))) * 180.0 / math.pi
    angle_b = (math.acos((side_b ** 2 - side_a ** 2 - side_c ** 2) / (-2 * side_a * side_c))) * 180.0 / math.pi
    angle_c = (math.acos((side_c ** 2 - side_a ** 2 - side_b ** 2) / (-2 * side_a * side_b))) * 180.0 / math.pi
    return (angle_a, angle_b, angle_c)

####################################################################################################
# Additional exercises
####################################################################################################

# TODO: Given a set of strings, calculate the length of the longest string.
def longest_length(strings: set) -> int:
    """Returns the longest length of a string in the set strings

    >>> longest_length({'University', 'of', 'Toronto'})
    10
    >>> longest_length({'John', 'Alexander', 'Macdonald'})
    9
    """
    return max((len(x) for x in strings))

# TODO: You are renting a car to make a road trip across Canada. The car rental company you plan to
#  use charges a fee of $50 plus $15 per day you rent the car.
import datetime
def total_rental_fee(start_day: datetime.date, end_day: datetime.date) -> int:
    """Returns the total fee of renting a car between start_day and end_day, the fee is $50 + $15
    per day the car is rented

    >>> total_rental_fee(datetime.date(2020, 9, 20), datetime.date(2020, 9, 20))
    65
    >>> total_rental_fee(datetime.date(2020, 9, 20), datetime.date(2020, 10, 20))
    515
    """
    return ((end_day - start_day).days + 1) * 15 + 50
