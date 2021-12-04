"""CSC110 Fall 2020: Food Delivery Simulation

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import datetime
import logging
import random
import statistics
from typing import Dict, List, Tuple

from entities import Courier, Customer, Restaurant
from food_delivery_system import FoodDeliverySystem
from events import Event, GenerateOrdersEvent
from event_queue import EventQueue, EventQueueList


###############################################################################
# Function version of simulation
###############################################################################
def run_simulation(initial_events: List[Event],
                   system: FoodDeliverySystem) -> None:
    """Main simulation loop (as a function)"""
    events = EventQueueList()  # Initialize an empty priority queue
    for event in initial_events:
        events.enqueue(event)

    while not events.is_empty():
        event = events.dequeue()

        logging.debug(f'Executing event: {event.timestamp} {type(event)}')
        # logging.debug('Executing event: ' + str(event.timestamp) + ' ' + str(type(event)))

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

    def _populate_initial_events(self, start_time: datetime.datetime, num_days: int) -> None:
        """Populate this simulation's Event priority queue with GenerateOrdersEvents.

        One new GenerateOrdersEvent is generated per day for num_days, starting with start_time.
        Each GenerateOrdersEvent's duration is 24 hours.
        """
        for day in range(0, num_days):
            time = start_time + datetime.timedelta(days=day)

            # Assume each "rush" lasts 24 hours
            self._events.enqueue(GenerateOrdersEvent(time, 24))

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
            courier = Courier(f'Courier {i}', location)
            self._system.add_courier(courier)

        for i in range(0, num_restaurants):
            location = _generate_location()
            menu_list = load_menu_data('data/menu_items.txt')
            restaurant = Restaurant(name=f'Restaurant {i}', address=f'{i} Fake St.',
                                    menu=generate_random_menu(menu_list), location=location)
            self._system.add_restaurant(restaurant)

    def run(self) -> None:
        """Run this simulation.
        """
        while not self._events.is_empty():
            event = self._events.dequeue()

            # logging.debug(f'Executing event: {event.timestamp} {type(event)}')
            # logging.debug('Executing event: ' + str(event.timestamp) + ' ' + str(type(event)))

            new_events = event.handle_event(self._system)
            for new_event in new_events:
                self._events.enqueue(new_event)

    def restaurant_order_stats(self) -> Dict[str, float]:
        """Return summary statistics for how many orders each restaurant received.

        The returned dictionary contains three keys:
            - 'max': the maximum number of orders made to a single restaurant
            - 'min': the minimum number of orders made to a single restaurant (can be 0)
            - 'average': the average number of orders made to a single restaurant

        Preconditions:
            - self.run() has already been called
        """
        restaurant_to_order_count = {restaurant.name: 0
                                     for restaurant in self._system.get_restaurants()}

        for order in self._system.completed_orders():
            name = order.restaurant.name
            restaurant_to_order_count[name] += 1

        order_counts = [restaurant_to_order_count[name]
                        for name in restaurant_to_order_count]

        return {
            'max': float(max(order_counts)),
            'min': float(min(order_counts)),
            'average': statistics.mean(order_counts)
        }


###############################################################################
# Helper functions for generating random entities
###############################################################################
TORONTO_COORDS = (43.707743, 43.641170, -79.533951, -79.276646)


def _generate_location() -> Tuple[float, float]:
    """Return a randomly-generated location (latitude, longitude) within Toronto bounds.
    """
    return (random.uniform(TORONTO_COORDS[0], TORONTO_COORDS[1]),
            random.uniform(TORONTO_COORDS[2], TORONTO_COORDS[3]))


def run_example_simulation() -> None:
    """Create and run a FoodDeliverySimulation.
    """
    print('Creating simulation.')
    simulation = FoodDeliverySimulation(datetime.datetime(2020, 11, 30), 7, 4, 100, 50)
    print('Starting simulation.')
    simulation.run()
    print('Simulation complete.')


###############################################################################
# Exercise 2: Generating Menus
###############################################################################
def load_menu_data(menu_data_file: str) -> List[str]:
    """Return a list of names for menu items based on the data in menu_data_file.

    See the file in data/menu_items.txt as an example.
    """
    with open(menu_data_file, encoding='utf-8') as file:
        # You can use `file` as an iterable in a comprehension or for loop, where
        # the comprehension/loop variable will refer to each line of the file (a str).
        # Use str.strip to remove the trailing '\n' in each string.
        ...
        return [str.strip(item) for item in file]


def generate_random_menu(items: List[str]) -> Dict[str, float]:
    """Generate a random menu from the given list of possible menu items.

    Notes:
        - Choose a random number of items
        - Choose a random price for each item (you can pick a random number in a
          reasonable range, and possibly include a cent value as well)
    """
    number_of_items = random.randint(3, 10)
    new_menu = {}

    for _ in range(0, number_of_items):
        new_item = random.choice(items)
        while new_item in new_menu.keys():
            new_item = random.choice(items)
        new_menu[new_item] = random.randint(1, 12) + random.randint(0, 99) * 0.01

    return new_menu


# def order_cost_stats()


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

    # Logging demo
    logging.basicConfig(level=logging.DEBUG)

    run_example_simulation()
