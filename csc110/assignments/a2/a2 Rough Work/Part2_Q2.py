"""a2 Part 2 Question 2 Rough Work"""


def mystery_2a_if(x: int, y: int, z: set[int]) -> bool:
    """Mystery 2a."""
    if x >= y:
        if x in z:
            return True
        elif y not in z:
            return False
        else:
            return False
    else:
        if x in z:
            return False
        elif y not in z:
            return True
        else:
            return False


def mystery_2a_no_if(x: int, y: int, z: set[int]) -> bool:
    """Mystery 2a."""
    return (x >= y and x in z) or (x < y and x not in z and y not in z)


def mystery_2b_if(n: int) -> bool:
    """Mystery 2b."""
    if n % 2 == 0:
        if n % 3 == 1:
            return True
        else:
            return False
    elif n <= 4:
        if n < 0:
            return True
        else:
            return False
    else:
        if n % 3 == 1:
            return False
        else:
            return True


def mystery_2b_no_if(n: int) -> bool:
    """Mystery 2b."""
    return (n % 2 == 0 and n % 3 == 1) or (n % 2 == 1 and ((n <= 4 and n < 0) or (n > 4 and n % 3 != 1)))


def mystery_2c_if(c1: int, c2: int, c3: int) -> bool:
    """Mystery 2c."""
    if c1 == c2:
        return False
    elif c1 > c2:
        if c3 <= c2:
            return False
        else:
            return True
    else:
        if c2 < c3:
            return True
        else:
            return False


def mystery_2c_no_if(c1: int, c2: int, c3: int) -> bool:
    return not (c1 == c2) and ((c1 > c2 or c1 < c2) and c3 > c2)
