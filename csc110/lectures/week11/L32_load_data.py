"""CSC110 Fall 2020: Generating Data for the Simulation

Module Description
==================
This module contains a function for reading in data from a restaurant data set:

- A list of Toronto restaurant data (from Yelp)

We can use this function as a source of data for our food delivery system.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import csv

from L30_entities import Restaurant


def load_restaurant_data(restaurant_data: str, count: int) -> list[Restaurant]:
    """Return a list of Restaurant objects based on the data in restaurant_data.

    The returned list contains at most count Restaurant objects.
    Each Restaurant object has an empty menu.
    """
    restaurants_so_far = []

    with open(restaurant_data, newline='') as file:
        r = csv.reader(file)

        # Skip header row
        next(r)
        for row in r:
            address = row[1]
            name = row[2]
            lat = float(row[7])
            lon = float(row[8])

            # Replace all new line characters in the address
            address = address.replace('\n', ' ')

            restaurants_so_far.append(Restaurant(name, address, {}, (lat, lon)))

            if len(restaurants_so_far) >= count:
                return restaurants_so_far

    return restaurants_so_far


if __name__ == '__main__':
    import pprint

    restaurants = load_restaurant_data('toronto_restaurants.csv', 100)
    pprint.pprint(restaurants)
