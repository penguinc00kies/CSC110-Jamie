"""CSC110 Fall 2021 Assignment 1, Bitmap Handling

Instructions (READ THIS FIRST!)
===============================

Do not make changes to this file.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""

from PIL import Image


def load_image(filename: str) -> tuple:
    """Return a three-element tuple containing data on the image found at filename.

    The first element of the tuple is a list of all the pixels in the image. Each pixel is a
    three-element tuple that represents the red, green, and blue colour channels.
    The second element of the tuple is the width of the image, in pixels.
    The third element of the tuple is the height of the image, in pixels.

    Assumes that a valid image can be found at filename.
    """
    image = Image.open(filename)

    pixel_data = image.load()
    width, height = image.size
    pixel_1d = [pixel_data[x, y] for y in range(height) for x in range(width)]

    return pixel_1d, width, height


def save_image(filename: str, pixels: list, width: int, height: int) -> None:
    """Create a width by height image containing pixels and save it to a file called filename.
    """
    image = Image.new('RGB', (width, height))

    [image.putpixel((x, y), pixels[x + y * width]) for x in range(width) for y in range(height)]

    image.save(filename)
