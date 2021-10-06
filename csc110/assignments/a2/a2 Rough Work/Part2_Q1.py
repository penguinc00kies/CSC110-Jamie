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


def mystery_1a_nested_rearranged(x: int, y: set[int]) -> str:
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


def solved_1a_nested(x: int, y: set[int]) -> str:
    return 'hello'
