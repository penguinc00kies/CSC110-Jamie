"""CSC110 Fall 2020: Food Delivery Simulation

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import datetime
import logging
import random
import statistics

from L30_entities import Courier, Customer, Restaurant
from L32_food_delivery_system import FoodDeliverySystem
from L31_events import Event, GenerateOrdersEvent
from L31_event_queue import EventQueue, EventQueueList


###############################################################################
# Function version of simulation
###############################################################################
def run_simulation(initial_events: list[Event],
                   system: FoodDeliverySystem) -> None:
    """Run a simulation by mutating the system with events, starting with the initial_events."""
    events = EventQueueList()  # Initialize an empty priority queue
    for event in initial_events:
        events.enqueue(event)

    while not events.is_empty():
        event = events.dequeue()

        new_events = event.handle_event(system)
        for new_event in new_events:
            events.enqueue(new_event)


###############################################################################
# Class version of simulation
###############################################################################
class FoodDeliverySimulation:
    """A simulation of the food delivery system.

    >>> simulation = FoodDeliverySimulation(datetime.datetime(2020, 11, 30), 7, 4, 100, 50)
    >>> simulation.run()
    """
    # Private Instance Attributes:
    #   - _system: The FoodDeliverySystem instance that this simulation uses.
    #   - _events: A priority queue of the events to process during the simulation.
    _system: FoodDeliverySystem
    _events: EventQueue

    def __init__(self, start_time: datetime.datetime, num_days: int,
                 num_couriers: int, num_customers: int,
                 num_restaurants: int) -> None:
        """Initialize a new simulation with the given simulation parameters.

        start_time: the starting time of the simulation
        num_days: the number of days that the simulation runs
        num_couriers: the number of couriers in the system
        num_customers: the number of customers in the system
        num_restaurants: the number of restaurants in the system
        """
        self._events = EventQueueList()
        self._system = FoodDeliverySystem()

        self._populate_initial_events(start_time, num_days)
        self._generate_system(num_couriers, num_customers, num_restaurants)

    ###########################################################################
    # Exercise 1: Completing FoodDeliverySimulation
    ###########################################################################
    def _populate_initial_events(self, start_time: datetime.datetime, num_days: int) -> None:
        """Populate this simulation's Event priority queue with GenerateOrdersEvents.

        One new GenerateOrdersEvent is generated per day for num_days, starting with start_time.
        Each GenerateOrdersEvent's duration is 24 hours.
        """
        for i in range(0, num_days):
            goe = GenerateOrdersEvent(start_time + datetime.timedelta(hours=i*24), 24)
            self._events.enqueue(goe)

    def _generate_system(self, num_couriers: int, num_customers: int, num_restaurants: int) -> None:
        """Populate this simulation's FoodDeliverySystem with the specified number of entities.

        You can initialize restaurants with empty menus.
        """
        for i in range(0, num_customers):
            location = _generate_location()
            customer = Customer(f'Customer {i}', location)
            self._system.add_customer(customer)

        for i in range(0, num_couriers):
            location = _generate_location()
            courier = Courier(f'Courier {1}', location)
            self._system.add_courier(courier)

        for i in range(0, num_restaurants):
            location = _generate_location()
            restaurant = Restaurant(f'Restaurant {i}', '123 Fake Street', {}, location)
            self._system.add_restaurant(restaurant)

    def run(self) -> None:
        """Run this simulation."""
        while not self._events.is_empty():
            event = self._events.dequeue()

            new_events = event.handle_event(self._system)
            for new_event in new_events:
                self._events.enqueue(new_event)

    ###########################################################################
    # Exercise 2: Reporting statistics
    ###########################################################################
    def restaurant_order_stats(self) -> dict[str, float]:
        """Return summary statistics for how many orders each restaurant received.

        The returned dictionary contains three keys:
            - 'max': the maximum number of orders made to a single restaurant
            - 'min': the minimum number of orders made to a single restaurant (can be 0)
            - 'average': the average number of orders made to a single restaurant

        Preconditions:
            - self.run() has already been called
        """
        # As we discussed yesterday, we can add a new method FoodDeliverySystem.get_restaurants()
        # instead of accessing a private attribute _restaurants.
        restaurant_to_order_count = {restaurant.name: 0 for restaurant in self._system.get_restaurants()}

        orders = self._system.get_orders()
        for order in orders:
            restaurant_to_order_count[order.restaurant.name] += 1

        return {'max': max(restaurant_to_order_count.values()),
                'min': min(restaurant_to_order_count.values()),
                'average': statistics.mean((restaurant_to_order_count.values()))}


###############################################################################
# Helper functions for generating random entities
###############################################################################
TORONTO_COORDS = (43.707743, 43.641170, -79.533951, -79.276646)


def _generate_location() -> tuple[float, float]:
    """Return a randomly-generated location (latitude, longitude) within Toronto bounds.
    """
    return (random.uniform(TORONTO_COORDS[0], TORONTO_COORDS[1]),
            random.uniform(TORONTO_COORDS[2], TORONTO_COORDS[3]))


def run_example_simulation() -> None:
    """Create and run a FoodDeliverySimulation.
    """
    print('Creating simulation.')
    simulation = FoodDeliverySimulation(datetime.datetime(2021, 12, 2), 7, 4, 100, 50)
    print('Starting simulation.')
    simulation.run()
    print('Simulation complete.')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    #
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['dataclasses', 'datetime', 'python_ta.contracts', 'random',
    #                       'entities', 'food_delivery_system', 'events', 'load_data',
    #                       'event_queue', 'sim_stats'],
    #     'max-line-length': 100,
    #     'allowed-io': ['run_example_simulation', 'print_report'],
    #     'disable': ['R1705', 'C0200', 'R0201']
    # })

    # logging.basicConfig(filename='simulation.log', encoding='utf-8', level=logging.DEBUG)

    run_example_simulation()
