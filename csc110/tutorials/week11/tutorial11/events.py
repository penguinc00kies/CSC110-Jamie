"""CSC110 Fall 2020: Food Delivery System Events

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
import random

from entities import Restaurant, Order
from food_delivery_system import FoodDeliverySystem


class Event:
    """An abstract class representing an event in a food delivery simulation.

    Instance Attributes:
        - timestamp: when the event occurs
    """
    timestamp: datetime.datetime

    def __init__(self, timestamp: datetime.datetime) -> None:
        """Initialize this event with the given timestamp."""
        self.timestamp = timestamp

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate the given food delivery system to process this event.
        """
        raise NotImplementedError


class NewOrderEvent(Event):
    """An event representing when a customer places an order at a restaurant."""
    # Private Instance Attributes:
    #   _order: the new order to be added to the FoodDeliverySystem
    _order: Order

    def __init__(self, order: Order) -> None:
        """Initialize a NewOrderEvent for the given order."""
        Event.__init__(self, order.start_time)
        self._order = order

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate system by placing an order.
        """
        estimated_time = system.place_order(self._order)

        if estimated_time is None:
            self._order.start_time = self.timestamp + datetime.timedelta(minutes=5)
            return [NewOrderEvent(self._order)]
        else:
            completion_time = self.timestamp + datetime.timedelta(seconds=estimated_time)
            return [CompleteOrderEvent(completion_time, self._order)]


class CompleteOrderEvent(Event):
    """An event representing when an order is delivered to a customer by a courier."""
    # Private Instance Attributes:
    #   _order: the order to be completed by this event
    _order: Order

    def __init__(self, timestamp: datetime.datetime, order: Order) -> None:
        Event.__init__(self, timestamp)
        self._order = order

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate the system by recording that the order has been delivered to the customer."""
        system.complete_order(self._order, self.timestamp)
        return []


class GenerateOrdersEvent(Event):
    """An event that causes a random generation of new orders.

    Private Representation Invariants:
        - self._duration > 0
    """
    # Private Instance Attributes:
    #   - _duration: the number of hours to generate orders for
    _duration: int

    def __init__(self, timestamp: datetime.datetime, duration: int) -> None:
        """Initialize this event with timestamp and the duration in hours.

        Preconditions:
            - duration > 0
        """
        Event.__init__(self, timestamp)
        self._duration = duration

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Generate new orders for this event's timestamp and duration."""
        customers = system.get_customers()
        restaurants = system.get_restaurants()

        events = []

        current_time = self.timestamp
        end_time = self.timestamp + datetime.timedelta(hours=self._duration)

        while current_time < end_time:
            customer = random.choice(customers)
            restaurant = random.choice(restaurants)
            # food_items = self.generate_food_items(restaurant)
            food_items = {}
            order = Order(customer=customer, restaurant=restaurant, food_items=food_items,
                          start_time=current_time)
            events.append(NewOrderEvent(order))

            current_time = current_time + datetime.timedelta(minutes=random.randint(1, 60))

        return events

    def generate_food_items(self, restaurant: Restaurant) -> dict[str, int]:
        """"fwoubwjcb"""
        # number_of_items = random.randint(3, 10)
        # new_items = {}
        #
        # for _ in range(0, number_of_items):
        #     menu = [keys for keys in restaurant.menu.keys()]
        #
        #     new_item = random.choice(menu)
        #     while new_item in new_items.keys():
        #         new_item = random.choice(menu)
        #
        #     new_items[new_item] = random.randint(1, 10)
        #
        # return new_items
        possible_items = list(restaurant.menu.keys())

        food_items = {}
        for _ in range(0, random.randint(1, 10)):
            item = random.choice(possible_items)

            if item not in food_items:
                food_items[item] = 1
            else:
                food_items[item] += 1

        return food_items


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['dataclasses', 'datetime', 'python_ta.contracts', 'random',
                          'entities', 'food_delivery_system', 'generate_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200', 'R0201']
    })
