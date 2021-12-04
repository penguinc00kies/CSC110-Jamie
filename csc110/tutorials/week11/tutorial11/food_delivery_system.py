"""CSC110 Fall 2020: Food Delivery System Class

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
from __future__ import annotations

import datetime
import math
from typing import Optional

# This is the Python module containing the individual entity data classes.
from entities import Restaurant, Customer, Courier, Order


class FoodDeliverySystem:
    """A system that maintains all entities (restaurants, customers, couriers, and orders).

    Representation Invariants:
        - self.name != ''
        - all(r == self._restaurants[r].name for r in self._restaurants)
        - all(c == self._customers[c].name for c in self._customers)
        - all(c == self._couriers[c].name for c in self._couriers)
    """
    # Private Instance Attributes:
    #   - _restaurants: a mapping from restaurant name to Restaurant object.
    #       This represents all the restaurants in the system.
    #   - _customers: a mapping from customer name to Customer object.
    #       This represents all the customers in the system.
    #   - _couriers: a mapping from courier name to Courier object.
    #       This represents all the couriers in the system.
    #   - _orders: a list of all orders (both open and completed orders).
    _restaurants: dict[str, Restaurant]
    _customers: dict[str, Customer]
    _couriers: dict[str, Courier]
    _orders: list[Order]

    ###########################################################################
    # Exercise 2: Developing the FoodDeliverySystem class
    ###########################################################################
    def __init__(self) -> None:
        """Initialize a new food delivery system.

        The system starts with no entities.
        """
        self._restaurants = {}
        self._customers = {}
        self._couriers = {}
        self._orders = []

    def add_restaurant(self, restaurant: Restaurant) -> bool:
        """Add the given restaurant to this system.

        Do NOT add the restaurant if one with the same name already exists.

        Return whether the restaurant was successfully added to this system.
        """
        if restaurant.name in self._restaurants:
            return False
        else:
            self._restaurants[restaurant.name] = restaurant
            return True

    def add_customer(self, customer: Customer) -> bool:
        """Add the given customer to this system.

        Do NOT add the customer if one with the same name already exists.

        Return whether the customer was successfully added to this system.
        """
        if customer.name in self._customers:
            return False
        else:
            self._customers[customer.name] = customer
            return True

    def add_courier(self, courier: Courier) -> bool:
        """Add the given courier to this system.

        Do NOT add the courier if one with the same name already exists.

        Return whether the courier was successfully added to this system.
        """
        if courier.name in self._couriers:
            return False
        else:
            self._couriers[courier.name] = courier
            return True

    def place_order(self, order: Order) -> Optional[int]:
        """Add an order to this system.

        Do NOT add the order if no couriers are available (i.e., are already assigned orders).

        - If a courier is available, add the order and assign it a courier, and return True.
        - Otherwise, do not add the order, and return False.

        Preconditions:
            - order not in self._orders
        """
        courier = self._assign_courier(order)

        if courier is None:
            return None
        else:
            self._orders.append(order)
            return estimate_delivery_time(order)

    def _assign_courier(self, order: Order) -> Optional[Courier]:
        """Find an available courier and assign the order to them.

        Return the courier assigned to the order, or None if no courier was
        available.
        """
        for _, courier in self._couriers.items():
            if courier.current_order is None:
                order.courier = courier
                courier.current_order = order

                return courier

        return None

    def complete_order(self, order: Order, timestamp: datetime.datetime) -> None:
        """Record that the given order has been delivered successfully at the given timestamp.

        Make the courier who was assigned this order available to take a new order.

        Preconditions:
            - order in self._orders
            - order.end_time is None
            - order.start_time < timestamp
        """
        order.courier.current_order = None
        order.end_time = timestamp

    def completed_orders(self) -> list[Order]:
        """Return a list of all the completed orders by this system."""
        return [order for order in self._orders if order.end_time is not None]

    def get_restaurants(self) -> list[Restaurant]:
        """Return a list of all restaurants registered with this system."""
        return list(self._restaurants.values())

    def get_customers(self) -> list[Customer]:
        """Return a list of all customers registered with this system."""
        return list(self._customers.values())


###############################################################################
# Exercise 1: Incorporating Distances
###############################################################################
EARTH_RADIUS = 6373.0  # km
COURIER_SPEED = 20  # km/h


def calculate_distance(location1: tuple[float, float],
                       location2: tuple[float, float]) -> float:
    """Return the distance between location1 and location 2 given in (latitude, longitude) pairs.

    We illustrate using *spherical* distance rather than Euclidean (2-D) distance.
    It doesn't make a difference in our case because the points are very close together,
    but we wanted to illustrate yet another example of implementing a mathematical
    formula in Python!

    Further reading: https://en.wikipedia.org/wiki/Great-circle_distance

    NOTE: the locations are in degrees, but the math module functions expect radians.
    Use math.radians to convert from degrees to radians before computing the given formula.
    """
    phi_1 = math.radians(location1[0])
    phi_2 = math.radians(location2[0])
    lambda_1 = math.radians(location1[1])
    lambda_2 = math.radians(location2[1])
    delta_phi = abs(phi_2 - phi_1)
    delta_lambda = abs(lambda_2 - lambda_1)
    root = ((math.sin(delta_phi / 2)) ** 2 + math.cos(phi_1) * math.cos(phi_2) * (math.sin(delta_lambda / 2)) ** 2)
    theta = 2 * math.asin(math.sqrt(root))

    return theta * EARTH_RADIUS


def estimate_delivery_time(order: Order) -> int:
    """Return an estimate time (in seconds) for the delivery in order to be completed.

    This delivery time is calculated as follows:
      1. Add the distance between the the courier and the restaurant, and the distance
         between the restaurant and the customer.
      2. Calculate the time taken for the courier to travel this distance, using the
         constant COURIER_SPEED. Because with the units here: COURIER_SPEED is given in km/h,
         but you need to return a number of seconds. Use the function `round` to round your
         final result to the nearest integer.
    """
    km_per_sec = COURIER_SPEED / 3600
    cou_to_res = calculate_distance(order.courier.location, order.restaurant.location)
    res_to_cus = calculate_distance(order.restaurant.location, order.customer.location)

    total_time = (cou_to_res + res_to_cus) / km_per_sec
    return round(total_time)


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['dataclasses', 'datetime', 'python_ta.contracts', 'math', 'entities'],
    #     'allowed-io': ['run_example'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200', 'R0201']
    # })
