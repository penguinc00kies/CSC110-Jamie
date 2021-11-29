"""CSC110 Fall 2021 Prep 11: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains the data class definitions that serve as the foundation
for our computational model of a food delivery system, as we discussed in this week's
prep reading.

Please read through this file carefully, and follow all instructions described below.
We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
from __future__ import annotations

from dataclasses import dataclass
import datetime
from typing import Optional


@dataclass
class Restaurant:
    """A place that serves food.

    Attributes:
      - name: the name of the restaurant
      - address: the address of the restaurant
      - menu: the menu of the restaurant with the name of the dish mapping to
        the price
      - location: the location of the restaurant as (latitude, longitude)

    Representation Invariants:
      - self.name != ''
      - self.address != ''
      - all(self.menu[item] >= 0 for item in self.menu)
      - -90 <= self.location[0] <= 90
      - -180 <= self.location[1] <= 180

    Sample Usage:
    >>> mcdonalds = Restaurant(name='McDonalds', address='160 Spadina Ave',\
                               menu={'fries': 4.5}, location=(43.649, -79.397))
    """
    name: str
    address: str
    menu: dict[str, float]
    location: tuple[float, float]


@dataclass
class Customer:
    """A person who orders food.

    Instance Attributes:
        - name: the name of the customer
        - location: a tuple containing the latitude and longitude of the customer

    Representation Invariants:
        - self.name != ''
        - -90 <= self.location[0] <= 90
        - -180 <= self.location[1] <= 180

    Sample Usage:

    >>> david = Customer('David', (44.649, -79.115))
    >>> david.name
    'David'
    >>> david.location
    (44.649, -79.115)
    """
    name: str
    location: tuple[float, float]


@dataclass
class Order:
    """A food order from a customer.

    Attributes:
      - customer: the customer who placed this order
      - restaurant: the restaurant the order is placed for
      - food_items: a mapping from names of food to the quantity being ordered
      - start_time: the time the order was placed
      - courier: the courier assigned to this order (initially None)
      - end_time: the time the order was completed by the courier (initially None)

    Representation Invariants:
      - self.food_items != {}
      - all(self.food_items[item] > 0 for item in self.food_items)
      - all(food in self.restaurant.menu.keys() for food in self.food_items.keys())

    Sample Usage:

    >>> david = Customer('David', (44.649, -79.115))
    >>> mcdonalds = Restaurant(name='McDonalds', address='160 Spadina Ave',\
                               menu={'fries': 4.5}, location=(43.649, -79.397))
    >>> order = Order(customer=david, restaurant=mcdonalds,\
                      food_items={'fries': 10},\
                      start_time=datetime.datetime(2020, 11, 5, 11, 30))
    >>> order.courier is None  # Illustrating default values
    True
    >>> order.end_time is None
    True
    """
    customer: Customer
    restaurant: Restaurant
    food_items: dict[str, int]
    start_time: datetime.datetime
    courier: Optional[Courier] = None
    end_time: Optional[datetime.datetime] = None


@dataclass
class Courier:
    """A person who delivers food orders from restaurants to customers.

    Deliberately left blank (you don't need to do anything here).
    We'll discuss this data class in lecture!
    """


def total_cost(order: Order) -> float:
    """Return the total cost of the food items in this order.

    >>> import math
    >>> david = Customer('David', (44.649, -79.115))
    >>> mcdonalds = Restaurant(name='McDonalds', address='160 Spadina Ave',\
                               menu={'fries': 4.5, 'Big Mac': 6.0}, location=(43.649, -79.397))
    >>> order = Order(customer=david, restaurant=mcdonalds,\
                      food_items={'fries': 10, 'Big Mac': 5},\
                      start_time=datetime.datetime(2020, 11, 5, 11, 30))
    >>> math.isclose(75, total_cost(order))
    True
    """
    cost_so_far = 0
    for food in order.food_items:
        cost_so_far = cost_so_far + order.food_items[food] * order.restaurant.menu[food]

    return cost_so_far


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'dataclasses', 'datetime'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
