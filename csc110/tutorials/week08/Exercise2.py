"""Exercise 2"""


def f2(n: int) -> None:
    """Precondition: n > 0"""
    i = 0

    while i < n:
        print(i)
        i = i + 2

    for j in range(0, n - 1):
        print(j)


def f3(n: int) -> int:
    """Precondition: n >= 0"""
    i = n + 100

    while 2 * i > n:
        print(i)
        i -= 4

    return i


def f4(n: int) -> int:
    """Precondition: n > 0."""
    i = 0

    while i != n:
        print(i)
        i = n - i

    return i
