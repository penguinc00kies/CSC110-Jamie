"""CSC110 Fall 2021 Assignment 4, Part 4: Two New Cryptosystems

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

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""


################################################################################
# Task 1 - The Grid Transpose Cryptosystem
################################################################################
def grid_encrypt(k: int, plaintext: str) -> str:
    """Encrypt the given plaintext using the grid cryptosystem.

    Preconditions:
        - k >= 1
        - len(plaintext) % k == 0
        - plaintext != ''

    >>> grid_encrypt(8, 'DAVID AND MARIO TEACH COMPUTER SCIENCE!!')
    'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!'
    """
    return grid_to_ciphertext(plaintext_to_grid(k, plaintext))


def grid_decrypt(k: int, ciphertext: str) -> str:
    """Decrypt the given ciphertext using the grid cryptosystem.

    Preconditions:
        - k >= 1
        - len(ciphertext) % k == 0
        - ciphertext != ''

    >>> grid_decrypt(8, 'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!')
    'DAVID AND MARIO TEACH COMPUTER SCIENCE!!'
    """
    return grid_to_plaintext(ciphertext_to_grid(k, ciphertext))


def plaintext_to_grid(k: int, plaintext: str) -> list[list[str]]:
    """Return the grid with k columns from the given plaintext.

    Preconditions:
        - k >= 1
        - len(plaintext) % k == 0
        - plaintext != ''
    """
    grid = []
    c = len(plaintext) // k
    for i in range(0, c):
        row = []
        for j in range(i * k, (i + 1) * k):
            row.append(plaintext[j])
        grid.append(row)

    return grid


def grid_to_ciphertext(grid: list[list[str]]) -> str:
    """Return the ciphertext corresponding to the given grid.

    Preconditions:
        - grid != []
        - grid[0] != []
        - all({len(row1) == len(row2) for row1 in grid for row2 in grid})
    """
    ciphertext = ''
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid)):
            ciphertext = ciphertext + grid[j][i]

    return ciphertext


def ciphertext_to_grid(k: int, ciphertext: str) -> list[list[str]]:
    """Return the grid corresponding to the given ciphertext.

    Note that this grid should be the one that is used to generate the ciphertext.

    Preconditions:
        - k >= 1
        - len(ciphertext) % k == 0
        - ciphertext != ''
    """
    grid = []
    c = len(ciphertext) // k
    for i in range(0, c):
        row = []
        for j in range(0, len(ciphertext)):
            if j % c == i:
                row.append(ciphertext[j])
        grid.append(row)

    return grid


def grid_to_plaintext(grid: list[list[str]]) -> str:
    """Return the plaintext message corresponding to the given grid.


    Preconditions:
        - grid != []
        - grid[0] != []
        - all({len(row1) == len(row2) for row1 in grid for row2 in grid})
    """
    plaintext = ''
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            plaintext = plaintext + grid[i][j]

    return plaintext


################################################################################
# Task 2 - Breaking The Grid Transpose Cryptosystem
################################################################################
def grid_break(ciphertext: str, candidates: set[str]) -> set[int]:
    """Return the set of possible secret keys that decrypt the given ciphertext into a message
    that contains at least one of the candidate words.

    >>> candidate_words = {'DAVID', 'MINE'}
    >>> grid_break('DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!', candidate_words) == {8, 10}
    True
    """
    possible_keys = set()
    number_of_rows = {k for k in range(1, len(ciphertext) + 1) if len(ciphertext) % k == 0}
    for word in candidates:
        for row_length in number_of_rows:
            for i in range(0, len(ciphertext) // row_length):
                row = []
                for j in range(0, len(ciphertext)):
                    if j % row_length == i:
                        row.append(ciphertext[j])
                if word in ''.join(row):
                    possible_keys.add(len(ciphertext) // row_length)

    return possible_keys


def run_example_break(ciphertext_file: str, candidates: set[str]) -> list[str]:
    """Return a list of possible plaintexts for the ciphertext found in the given file.

    Based on the A4 directory structure, you can call this function like this:
        >>> possible_plaintexts = run_example_break('ciphertexts/grid_ciphertext1.txt', {'climate'})
    """
    with open(ciphertext_file, encoding='utf-8') as f:
        ciphertext = f.read()

    # (Not to be handed in) Try completing this function by calling grid_break and returning a
    # list of the possible plaintext messages.

    # return [ciphertext] + list(candidates)  # This is a dummy line, please replace it!
    possible_plaintexts = []
    possible_keys = grid_break(ciphertext, candidates)
    for key in possible_keys:
        possible_plaintexts.append(grid_decrypt(key, ciphertext))

    return possible_plaintexts


################################################################################
# Task 3 - The Permuted Grid Transpose Cryptosystem
################################################################################
def permutation_grid_encrypt(k: int, perm: list[int], plaintext: str) -> str:
    """Encrypt the given plaintext using the grid cryptosystem.

    Preconditions:
        - k >= 1
        - len(plaintext) % k == 0
        - sorted(perm) == list(range(0, k))
        - plaintext != ''

    >>> permutation_grid_encrypt(8, [0, 1, 2, 3, 4, 5, 6, 7],
    ...                          'DAVID AND MARIO TEACH COMPUTER SCIENCE!!')
    'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!'
    >>> permutation_grid_encrypt(8, [3, 2, 5, 0, 7, 1, 6, 4],
    ...                          'DAVID AND MARIO TEACH COMPUTER SCIENCE!!')
    'IACTNVMAUE I REDDTMCN OS!A EPIAOC !DRHEC'
    >>> permutation_grid_encrypt(8, [1, 0, 2, 3, 4, 5, 6, 7],
    ...                          'DAVID AND MARIO TEACH COMPUTER SCIENCE!!')
    'A EPIDDTMCVMAUEIACTNDRHEC I REAOC !N OS!'
    """
    grid = plaintext_to_grid(8, plaintext)
    return grid_to_ciphertext(shift_columns(perm, grid))


def permutation_grid_decrypt(k: int, perm: list[int], ciphertext: str) -> str:
    """Return the grid corresponding to the given ciphertext.

    Note that this grid should be the one that is used to generate the ciphertext.

    Preconditions:
        - k >= 1
        - len(ciphertext) % k == 0
        - sorted(perm) == list(range(0, k))
        - ciphertext != ''

    >>> permutation_grid_decrypt(8, [0, 1, 2, 3, 4, 5, 6, 7],
    ...                          'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!')
    'DAVID AND MARIO TEACH COMPUTER SCIENCE!!'
    >>> permutation_grid_decrypt(8, [3, 2, 5, 0, 7, 1, 6, 4],
    ...                          'IACTNVMAUE I REDDTMCN OS!A EPIAOC !DRHEC')
    'DAVID AND MARIO TEACH COMPUTER SCIENCE!!'
    """
    grid = ciphertext_to_grid(8, ciphertext)
    return grid_to_plaintext(unshift_columns(perm, grid))


def shift_columns(perm: list[int], grid: list[list[str]]) -> list[list[str]]:
    """Return the grid with its columns moved around as according to perm

    Preconditions:
        - len(perm) = len(grid[0])

    >>> original_grid = [['D', 'A', 'V', 'I', 'D', ' ', 'A', 'N'],
    ...                   ['D', ' ', 'M', 'A', 'R', 'I', 'O', ' '],
    ...                   ['T', 'E', 'A', 'C', 'H', ' ', 'C', 'O'],
    ...                   ['M', 'P', 'U', 'T', 'E', 'R', ' ', 'S'],
    ...                   ['C', 'I', 'E', 'N', 'C', 'E', '!', '!']]
    >>> shifted_grid = [['I', 'V', ' ', 'D', 'N', 'A', 'A', 'D'],
    ...                   ['A', 'M', 'I', 'D', ' ', ' ', 'O', 'R'],
    ...                   ['C', 'A', ' ', 'T', 'O', 'E', 'C', 'H'],
    ...                   ['T', 'U', 'R', 'M', 'S', 'P', ' ', 'E'],
    ...                   ['N', 'E', 'E', 'C', '!', 'I', '!', 'C']]
    >>> shift_columns([3, 2, 5, 0, 7, 1, 6, 4], original_grid) == shifted_grid
    True
    >>> shift_columns([0, 1, 2, 3, 4, 5, 6, 7], original_grid) == original_grid
    True
    """
    permutated_list = []
    for i in range(0, len(grid)):
        row = []
        for j in perm:
            row.append(grid[i][j])
        permutated_list.append(row)

    return permutated_list


def unshift_columns(perm: list[int], grid: list[list[str]]) -> list[list[str]]:
    """Return the grid with its columns restored to their original position as according to perm

    Preconditions:
        - len(perm) = len(grid[0])

    >>> original_grid = [['D', 'A', 'V', 'I', 'D', ' ', 'A', 'N'],
    ...                   ['D', ' ', 'M', 'A', 'R', 'I', 'O', ' '],
    ...                   ['T', 'E', 'A', 'C', 'H', ' ', 'C', 'O'],
    ...                   ['M', 'P', 'U', 'T', 'E', 'R', ' ', 'S'],
    ...                   ['C', 'I', 'E', 'N', 'C', 'E', '!', '!']]
    >>> shifted_grid = [['I', 'V', ' ', 'D', 'N', 'A', 'A', 'D'],
    ...                   ['A', 'M', 'I', 'D', ' ', ' ', 'O', 'R'],
    ...                   ['C', 'A', ' ', 'T', 'O', 'E', 'C', 'H'],
    ...                   ['T', 'U', 'R', 'M', 'S', 'P', ' ', 'E'],
    ...                   ['N', 'E', 'E', 'C', '!', 'I', '!', 'C']]
    >>> unshift_columns([3, 2, 5, 0, 7, 1, 6, 4], shifted_grid) == original_grid
    True
    """
    permutated_list = []
    for i in range(0, len(grid)):
        row = []
        while len(row) < len(grid[0]):
            for j in range(0, len(perm)):
                for k in range(0, len(perm)):
                    if j == perm[k]:
                        row.append(grid[i][k])

        permutated_list.append(row)

    return permutated_list


if __name__ == '__main__':
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # Leave this code uncommented when you submit your files.
    #
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['python_ta.contracts'],
    #     'allowed-io': ['run_example_break'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200']
    # })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
