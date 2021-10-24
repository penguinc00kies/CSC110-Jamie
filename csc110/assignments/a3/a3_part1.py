"""CSC110 Fall 2021 Assignment 3, Part 1: Text Generation, Uniformly Random Model (SOLUTIONS)

Instructions (READ THIS FIRST!)
===============================
Implement each of the functions in this file. As usual, do not change any function headers
or preconditions. You do NOT need to add doctests.

You may create some additional helper functions to help break up your code into smaller parts.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""
import random


def generate_text_uniform(model: dict[str, int], n: int) -> str:
    """Return a string of n randomly-generated words chosen from the given model.

    Each word in the returned string is separated by a single space.

    Preconditions:
        - n >= 0
        - model != {}
    """
    # Unpack model into two lists whose indexes correspond to one another
    words = []
    word_frequencies = []
    for word in model:
        words.append(word)
        word_frequencies.append(model[word])

    new_words = random.choices(words, weights=word_frequencies, k=n)
    return str.join(' ', new_words)


def create_model_uniform(text: str) -> dict[str, int]:
    """Return a model of the words in text.

    The model is a mapping of words to the number of times the word occurs in text. A "word"
    contains no spaces.

    This function should return model that is valid input to generate_text_uniform.

    Preconditions:
        - text != ''

    IMPLEMENTATION NOTE: Use the str.split method to get a list of words.
    """


def run_example(filename: str, num_words: int) -> str:
    """Run an example to demonstrate random text generation with num_words words based on the data
    in filename.

    To call this function:
        - Make sure you see that the 'data' folder is in the same directory as this file
        - Use an argument for filename like: 'data/texts/sample_text_raw.txt'
        - Try out the other plaintext files in  'data/texts', too
    """
    with open(filename) as f:
        file_text = f.read()

    stripped_text = str.strip(file_text)  # str.strip removes leading/trailing whitespace
    model_from_file = create_model_uniform(stripped_text)
    generated_words = generate_text_uniform(model_from_file, num_words)

    return generated_words


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # python_ta.check_all(config={
    #     'allowed-io': ['run_example'],
    #     'extra-imports': ['python_ta.contracts', 'random'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200']
    # })
