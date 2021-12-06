"""CSC110 Tutorial 9: More Running-Time Analysis

Module Description
==================
This module contains code to animate the convex hull you developed in this week's tutorial.
Read through this file and try running it, and feel free to change it as well.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import pygame
from pygame.colordict import THECOLORS

from tutorial9_part2 import convex_hull


def draw_points(screen: pygame.Surface, points: set[tuple[int, int]]) -> None:
    """Render points as black circles onto the screen.

    Preconditions:
        - all(0 <= p[0] < screen.width for p in points)  # x-coordinates in range
        - all(0 <= p[1] < screen.height for p in points)  # y-coordinates in range
    """
    for p in points:
        pygame.draw.circle(screen, THECOLORS['black'], p, 3)


def draw_hull(screen: pygame.Surface, points: list[tuple[int, int]]) -> None:
    """Render points as turquoise circles and adjacent points as turquoise lines onto the screen.

    Preconditions:
        - all(0 <= p[0] < screen.width for p in points)  # x-coordinates in range
        - all(0 <= p[1] < screen.height for p in points)  # y-coordinates in range
    """
    for i in range(0, len(points)):
        pygame.draw.circle(screen, THECOLORS['darkturquoise'], points[i], 6)

        if i > 0:
            pygame.draw.line(screen, THECOLORS['darkturquoise'], points[i - 1], points[i])


def animate_convex_hull(points: set[tuple[int, int]]) -> None:
    """Animate the convex hull algorithm using pygame."""
    hull = convex_hull(points)
    assert len(hull) >= 3

    pygame.init()
    screen_size = (800, 800)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Use the left and right arrow keys on your keyboard.')
    screen.fill(THECOLORS['white'])

    hull_so_far = [hull[0], hull[1]]
    current_index = 2

    # Start the event loop
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the event loop
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and current_index < len(hull):
                    list.append(hull_so_far, hull[current_index])
                    current_index = current_index + 1
                elif event.key == pygame.K_LEFT and current_index > 2:
                    list.pop(hull_so_far)
                    current_index = current_index - 1

        # Visualize the hull
        screen.fill(THECOLORS['white'])
        draw_points(screen, points)
        draw_hull(screen, hull_so_far)
        pygame.display.flip()


if __name__ == '__main__':
    import random

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    NUM_POINTS = 100

    # A random set of points
    RANDOM_POINTS = {(random.randint(10, SCREEN_WIDTH - 10), random.randint(10, SCREEN_HEIGHT - 10))
                     for _ in range(0, NUM_POINTS)}

    animate_convex_hull(RANDOM_POINTS)
