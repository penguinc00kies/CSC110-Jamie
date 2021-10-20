"""CSC110 Fall 2021: Term Test 1, Q3

Module Description
==================
This Python file contains instructions for this question. There are FOUR
parts of this question, labelled "Part (a)", "Part (b)", etc.
The docstrings in this file contain instructions on how to complete each part,
so please read those comments carefully.

python_ta is not required for grading.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""
from dataclasses import dataclass


####################################################################################################
# Part (a)
####################################################################################################
def create_nested_list_data() -> list[list]:
    """Return a small dataset in a nested list format.

    Each nested list is composed of items with type: str, str, int, in that order.
        - The first str is the title (i.e., name) of a song
        - The second str is the name of the artist
        - the int is the duration of the song in milliseconds

    INSTRUCTIONS: Do NOT change this function.
    """
    return [
        ['Shape of You', 'Ed Sheeran', 233713],
        ['Despacito - Remix', 'Luis Fonsi', 228827],
        ['Something Just Like This', 'The Chainsmokers', 247160],
        ['Galway Girl', 'Ed Sheeran', 170827],
        ['Closer', 'The Chainsmokers', 244960]
    ]


def playlist_duration(data: list[list]) -> int:
    """Return the total duration in milliseconds of all songs in data.

    INSTRUCTIONS: Complete the body of this function. You must follow the docstring description
        exactly. Do NOT add any more doctest examples.

    RESTRICTIONS:
        - You must use a for loop
        - You may not use any comprehensions
        - You may not use any built-in functions/methods

    >>> example_data = create_nested_list_data()
    >>> playlist_duration(example_data)
    1125487
    """
    playlist_length_so_far = 0

    for song in data:
        playlist_length_so_far = playlist_length_so_far + song[2]

    return playlist_length_so_far


def lowercase_titles(data: list[list], threshold: int) -> None:
    """Change (i.e., MUTATE) the titles of all songs with a duration of at least threshold
    (inclusive) so that those titles only contain lowercase characters.

    Preconditions:
        - data is in the format as specified in create_nested_list_data

    INSTRUCTIONS: Complete the body of this function and add ONE doctest example that demonstrates
        what the function does.

    RESTRICTIONS:
        - You must use a for loop
        - You may not use any comprehensions
        - You may not use any built-in functions/methods, EXCEPT FOR: str.lower

    TODO: include ONE doctest example and remove this todo. We have gotten you started.
    >>> example_data = create_nested_list_data()
    >>> lowercase_titles(example_data, 240000)
    >>> example_data[0][0] == 'Shape of You' and example_data[4][0] == 'closer'
    True
    """
    for song in data:
        if song[2] >= threshold:
            song[0] = str.lower(song[0])


####################################################################################################
# Part (b)
####################################################################################################
def contains_artist(data: list[list], artist: str) -> bool:
    """Return whether at least one song in data is sung by artist.

    Preconditions:
        - data is in the format as specified in create_nested_list_data
        - len(data) > 0

    INSTRUCTIONS: Do NOT change this function. We know that it contains at least one bug.
    """
    for song in data:
        if song[1] == artist:
            return True
        else:
            return False


def test_contains_artist() -> None:
    """Test contains_artist (see instructions).

    INSTRUCTIONS: There is at least one bug in contains_artist. Complete the body of this UNIT
        TEST so that it demonstrates a bug. That is, this unit test should fail when run on
        contains_artist.

    RESTRICTIONS:
        - You may not use hypothesis
        - You may not violate the function's preconditions (including the type contract)
    """
    example_data = create_nested_list_data()
    expected = True
    actual = contains_artist(example_data, 'Luis Fonsi')

    assert actual == expected


def has_contains_artist_bug() -> str:
    """Return a BRIEF English description of the bug you found in contains_artist.

    INSTRUCTIONS: Complete the body of this function so that it returns your description of the
        bug in a single string.

    RESTRICTIONS:
        - Your description must be less than 200 characters (i.e., len(contains_artist()) < 200)
    """
    return 'The function always returns true or false on the first iteration of the loop. Thus, the' \
           ' loop never gets to fully iterate over the list.'


####################################################################################################
# Part (c)
####################################################################################################
@dataclass
class Song:
    """A data class that represents a song in Spotify.

    INSTRUCTIONS: Do NOT change this dataclass.

    Instance Attributes:
        - title: the title (or name) of the song
        - artist: the name of the performing artist of the song
        - duration: the duration of the song in milliseconds

    Representation Invariants:
        - self.title != ''
        - self.artist != ''
        - self.duration > 0

    >>> a_song = Song('Shape of You', 'Ed Sheeran', 233713)
    """
    title: str
    artist: str
    duration: int


def create_dataclass_data() -> list[Song]:
    """Return a small dataset in a list of dataclass format.

    INSTRUCTIONS: Do NOT change this function.
    """
    return [
        Song('Shape of You', 'Ed Sheeran', 233713),
        Song('Despacito - Remix', 'Luis Fonsi', 228827),
        Song('Something Just Like This', 'The Chainsmokers', 247160),
        Song('Galway Girl', 'Ed Sheeran', 170827),
        Song('Closer', 'The Chainsmokers', 244960)
    ]


def collect_the_artists(data: list[Song]) -> set[str]:
    """Return the set of all artists in data where the performing artist name contains the word 
    'The' (case sensitive).

    INSTRUCTIONS: Complete the body of this function and add ONE doctest example that demonstrates
        what the function does.

    RESTRICTIONS:
        - You must use a for loop
        - You may not use any comprehensions
        - You may not use any built-in functions, EXCEPT FOR: set.add

    >>> example_data = create_dataclass_data()
    >>> collect_the_artists(example_data)
    {'The Chainsmokers'}
    """
    artists_so_far = set()

    for song in data:
        if 'The' in song.artist:
            set.add(artists_so_far, song.artist)

    return artists_so_far


####################################################################################################
# Part (d)
####################################################################################################
def add_artists(lst: list[str], data: list[Song], max_duration: int) -> None:
    """Add (i.e, MUTATE) to lst, in the order that they appear, the artists of the songs from data
    that are not longer than max_duration (inclusive).

    Precondition:
        - len(data) > 0
        - max_duration > 0

    INSTRUCTIONS: Do NOT change this function. We know that it contains at least one bug.
    """
    for song in data:
        if song.duration <= max_duration:
            list.extend(lst, song.artist)


def test_add_artists() -> None:
    """Test add_artists.

    INSTRUCTIONS: There is at least one bug in add_artists. Complete the body of this UNIT
        TEST so that it demonstrates a bug. That is, this unit test should fail when run on
        add_artists.

    RESTRICTIONS:
        - You may not use hypothesis
        - You may not violate the function's preconditions (including the type contract)
    """
    example_data = create_dataclass_data()
    example_list = []
    expected = ['Ed Sheeran', 'Luis Fonsi', 'Ed Sheeran']
    add_artists(example_list, example_data, 240000)

    assert example_list == expected


def add_artists_bug() -> str:
    """Return a BRIEF English description of the bug you found in add_artists.

    INSTRUCTIONS: Complete the body of this function so that it returns your description of the
        bug in a single string.

    RESTRICTIONS:
        - Your description must be less than 200 characters (i.e., len(add_artists()) < 200)
    """
    return 'list.extend will iterate through the artist\'s name and add each letter in the name as' \
           ' a separate element to lst, rather than adding the name as one element to lst.'
