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

from L30_entities import Order
from L30_food_delivery_system import FoodDeliverySystem


class Event:
    """An abstract class representing an event in a food delivery simulation.

    Instance Attributes:
        - timestamp: the start time of the event
    """
    timestamp: datetime.datetime

    def __init__(self, timestamp: datetime.datetime) -> None:
        """Initialize this event with the given timestamp."""
        self.timestamp = timestamp

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate the given food delivery system to process this event.
        """
        raise NotImplementedError


###############################################################################
# Demo 1
###############################################################################
class NewOrderEvent(Event):
    """An event representing when a customer places an order at a restaurant."""
    # Private Instance Attributes:
    #   _order: the new order to be added to the FoodDeliverySystem
    _order: Order

    def __init__(self, order: Order, timestamp: datetime.datetime) -> None:
        """ Initialize"""
        Event.__init__(self, timestamp)
        self._order = order

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Update the system by placing an order"""
        system.place_order(self._order)

        completion_time = self.timestamp + datetime.timedelta(minutes = 10)
        return [CompleteOrderEvent(self._order, completion_time)]


###############################################################################
# Exercise 1: Representing events
###############################################################################
# TODO: Create a new CompleteOrderEvent class in the space below.
class CompleteOrderEvent(Event):
    """An event representing when an order is delivered to a customer by a courier."""
    _order: Order

    def __init__(self, order: Order, timestamp: datetime.datetime) -> None:
        """ Initialize"""
        Event.__init__(self, timestamp)
        self._order = order

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Update the system by completing an order"""
        system.complete_order(self._order, self.timestamp)

        return []


###############################################################################
# Exercise 2: The GenerateOrdersEvent
###############################################################################
class GenerateOrdersEvent(Event): # Dinnertime
    """An event that causes a random generation of new orders.
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
        # Technically the lines below access a private attribute of system,
        # which is a poor practice. We'll discuss an alternate approach in class.
        customers = system.get_customers()
        restaurants = [system._restaurants[name] for name in system._restaurants]

        events = []  # Accumulator

        current_time = self.timestamp
        end_time = self.timestamp + datetime.timedelta(hours=self._duration)

        while current_time <= end_time:
            new_order = Order(random.choice(customers),
                              random.choice(restaurants),
                              {},
                              current_time)
            new_order_event = NewOrderEvent(new_order, current_time)  # Create a randomly-generated NewOrderEvent

            events.append(new_order_event)
            current_time = current_time + datetime.timedelta(minutes =random.randint(1, 60))

        return events


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['dataclasses', 'datetime', 'python_ta.contracts', 'random',
                          'L30_entities', 'L30_food_delivery_system', 'generate_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200', 'R0201']
    })
