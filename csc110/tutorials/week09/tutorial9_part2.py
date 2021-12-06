"""CSC110 Tutorial 9: More Running-Time Analysis (SOLUTIONS)

Module Description
==================
This module contains functions headers you should implement for finding the
convex hull of a set of points. A function that animates the convex hull
one line at a time is also provided.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import math


def convex_hull(points: set[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return the convex hull of the given points.

    The first point in the convex hull is the one with the smallest x-coordinate,
    breaking ties by picking the point with the smallest y-coordinate.
    The points in the convex hull appear in clockwise order.

    Preconditions:
        - len(points) >= 3

    >>> convex_hull({(150, 350), (200, 100), (250, 200), (425, 100), (500, 300), (500, 500), (700, 30)})
    [(150, 350), (200, 100), (700, 30), (500, 500), (150, 350)]
    >>> convex_hull({(125, 450), (375, 125), (675, 450)})
    [(125, 450), (375, 125), (675, 450), (125, 450)]
    """
    hull_list = []

    smallest_point_so_far = (math.inf, math.inf)
    for point in points:
        if point[0] < smallest_point_so_far[0]:
            smallest_point_so_far = point
        elif point[0] == smallest_point_so_far[0]:
            if point[1] < smallest_point_so_far[1]:
                smallest_point_so_far = point
    hull_list.append(smallest_point_so_far)

    next_point_to_add = next_point((int(smallest_point_so_far[0]),
                                    int(smallest_point_so_far[1] + 1)),
                                    smallest_point_so_far, points)
    hull_list.append(next_point_to_add)

    while hull_list[-1] != smallest_point_so_far:
        next_point_to_add = next_point(hull_list[-2], hull_list[-1], points)
        hull_list.append(next_point_to_add)

    return hull_list


def leftmost(points: set[tuple[int, int]]) -> tuple[int, int]:
    """Return the leftmost (smallest x-coordinate) point in points.

    If there is a tie, return the one with the smallest y-coordinate.

    Note: because we're using pygame's coordinate system here, small y-coordinates
    translate to *higher* points in the visualization window.

    Preconditions:
        - points != set()

    >>> my_set = {(150, 350), (200, 100), (250, 200), (425, 100)}
    >>> leftmost(my_set)
    (150, 350)
    >>> my_set = {(150, 350), (150, 100), (150, 200), (150, 100)}
    >>> leftmost(my_set)
    (150, 100)
    """
    leftmost_so_far = (math.inf, math.inf)
    for cord in points:
        if cord[0] < leftmost_so_far[0]:
            leftmost_so_far = cord
        elif cord[0] == leftmost_so_far[0] and cord[1] < leftmost_so_far[1]:
            leftmost_so_far = cord

    return leftmost_so_far


def angle_between(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> float:
    """Return the angle between line segments ab and ac, in radians.

    Preconditions:
        - b != a
        - c != a

    Hint: The `math` module has a function that you need!

    >>> result = angle_between((150, 350), (150, 351), (200, 100))
    >>> math.isclose(result, 2.9441970937399122)
    True
    >>> result = angle_between((150, 350), (150, 351), (150, 351))
    >>> math.isclose(result, 0.0)
    True

    Note: to avoid rounding error, you should use min and max to make sure
    your "cos" values are between -1 and 1.
    """
    numerator = (b[0] - a[0]) * (c[0] - a[0]) + (b[1] - a[1]) * (c[1] - a[1])
    denominator = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) * math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)

    return math.acos(max(-1.0, min(1.0, numerator / denominator)))


def next_point(prev: tuple[int, int], curr: tuple[int, int], points: set[tuple[int, int]]) -> tuple[int, int]:
    """Return the next point in the convex hull after curr and prev.

    If there is a tie in the angle calculation, pick the point that is *furthest* away from curr.

    Preconditions:
      - len(points) >= 3
      - curr in points
      - curr and prev are both in the convex hull of points

    Implementation notes:
        - Call angle_between, but make sure you are passing in the arguments in the correct order
        - curr is in points; you need to skip over this point to ensure you don't violate a
          precondition for angle_between

    >>> pts = {(200, 100), (250, 200), (500, 300), (425, 100), (150, 350), (700, 30), (500, 500)}
    >>> next_point((150, 351), (150, 350), pts)
    (200, 100)
    """
    greatest_angle_so_far = 0
    furthest_point = ()
    for point in points:
        if point != curr:
            angle = angle_between(curr, prev, point)
            if greatest_angle_so_far < angle:
                greatest_angle_so_far = angle
                furthest_point = point
    return furthest_point


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
