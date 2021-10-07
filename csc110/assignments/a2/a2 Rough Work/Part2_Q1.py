"""a2 Part 2 Question 1 Rough Work"""


def mystery_1a_nested(x: int, y: set[int]) -> str:
    """Mystery 1a."""
    if len(y) > 1 and x <= 0:
        return 'David'
    else:
        if x > 1 and sum({n ** 2 for n in y}) >= 10:
            return 'Mario'
        else:
            return 'David'


def mystery_1a_nested_rearranged1(x: int, y: set[int]) -> str:
    """Mystery 1a."""
    if x > 1 and sum({n ** 2 for n in y}) >= 10:
        return 'Mario'
    else:
        if len(y) > 1 and x <= 0:
            return 'David'
        else:
            return 'David'


def mystery_1a_nested_rearranged2(x: int, y: set[int]) -> str:
    """Mystery 1a."""
    if x > 1 and sum({n ** 2 for n in y}) >= 10:
        return 'Mario'
    else:
        return 'David'


def mystery_1b_nested(n: int, rows_of_nums: list[list[int]]) -> int:
    """Mystery 1b."""
    if len(rows_of_nums) > n > 0:
        if n == 1:
            return 0
        elif n in rows_of_nums[n]:
            return sum(rows_of_nums[n]) + n
        else:
            return sum(rows_of_nums[0])
    else:
        if len(rows_of_nums) > 20:
            return 20
        else:
            return n


def mystery_1b_nested_rearranged1(n: int, rows_of_nums: list[list[int]]) -> int:
    """Mystery 1b."""
    if n == 1 and len(rows_of_nums) > 1:
        return 0
    elif len(rows_of_nums) > n > 0 and n in rows_of_nums[n]:
        return sum(rows_of_nums[n]) + n
    elif len(rows_of_nums) > n > 0:
        return sum(rows_of_nums[0])
    elif (n >= len(rows_of_nums) or n <= 0) and len(rows_of_nums) > 20:
        return 20
    else:
        return n


def mystery_1b_nested_rearranged2(n: int, rows_of_nums: list[list[int]]) -> int:
    """Mystery 1b."""
    if (n >= len(rows_of_nums) or n <= 0) and len(rows_of_nums) > 20:
        return 20
    elif (n >= len(rows_of_nums) or n <= 0) and len(rows_of_nums) <= 20:
        return n
    elif n == 1:
        return 0
    elif n in rows_of_nums[n]:
        return sum(rows_of_nums[n]) + n
    else:
        return sum(rows_of_nums[0])

