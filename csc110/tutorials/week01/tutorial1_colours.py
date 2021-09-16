"""CSC110 Tutorial 1: Data and Functions (Colour Visualization)

Module Description
==================
This Python file contains some code for visualizing colours using Pygame.

You do *not* need to understand how any of this code works for Tutorial 1.
But don't worry, over the next few weeks you'll learn about how to use Pygame
to create your own visualizations.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Mario Badr.
"""
import pygame


def show_colours(colours: list) -> None:
    """Visualize the given list of colours using Pygame.

    Takes a list of colours, where each colour is represented as a tuple of three
    integers: (r, g, b). The list must not be empty.

    When this function is called, each colour appears as a solid vertical bar in
    a Pygame window. When the window is open, you can close it like a normal window
    (press the red X in the top-right corner).

    >>> colours = [(255, 105, 180), (46, 139, 87), (0, 0, 128)]
    >>> show_colours(colours)  # A Pygame window appears when this is called
    ...
    """
    assert colours != [], 'You must call show_colours with at least one colour.'
    pygame.display.init()

    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    rect_width = screen_width / len(colours)

    for i in range(len(colours)):
        pygame.draw.rect(
            screen, colours[i],
            pygame.Rect(int(rect_width * i), 0, int(rect_width) + 1, screen_height)
        )

    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.wait()

    pygame.display.quit()
