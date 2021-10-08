"""CSC110 Tutorial 4: Data Classes and For Loops (Pygame runner)

Module Description
==================
This Python file contains some code for running Pygame to display graphics in a window.

You do *not* need to understand how this code works for Tutorial 4. Please just save this
file into your tutorial folder.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import contextlib
import pygame


@contextlib.contextmanager
def pygame_surface(screen_width: int = 800, screen_height: int = 800) -> contextlib.AbstractContextManager:
    """A context manager for displaying static visualizations using Pygame.

    Yields a pygame.Surface object that can be drawn on using pygame.draw functions.
    Once the code in the with block is executed, the surface is displayed in a
    non-interactive Pygame window, which remains until the user closes the window
    (click on the "X" to close).

    Because the image is only displayed after the with block executes, this context
    manager does not support animations.
    """
    pygame.display.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))

    yield screen

    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.wait()

    pygame.display.quit()
