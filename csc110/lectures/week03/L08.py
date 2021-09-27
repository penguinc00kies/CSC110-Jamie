def calculate_pay(start: int, end: int, pay_rate: float) -> float:
    """Return the pay of an employee who worked for the given time at the given pay rate.

    start and end represent the hour (from 0 to 23 inclusive) that the employee
    started and ended their work.

    pay_rate is the hourly pay rate and must be >= 15.0 (the minimum wage).

    Preconditions:
    - 0 <= start <= 23
    - 0 <= end <= 23
    - start < end
    - pay_rate >= 15.0

    >>> calculate_pay(3, 5, 15.5)
    31.0
    >>> calculate_pay(9, 21, 22.0)
    264.0
    """
    return (end - start) * pay_rate


def ticket_price(age: int) -> float:
    """Return the ticket price for a person who is age years old.

    Seniors 65 and over pay 4.75, kids 12 and under pay 4.25, and
    everyone else pays 7.50.

    Precondition:
      - age > 0

    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75
    """
    if age <= 12:
        return 4.25
    elif age < 65:
        return 7.5
    else:
        return 4.75


def bigger_max(nums1: set[int], nums2: set[int]) -> set[int]:

    if max(nums1) >= max(nums2):
        return nums1
    else:
        return nums2

# def tuples (tuple1: tuple[int], tuple2: tuple[int, int], tuple3: [int, int, int]) these all mean
# diferent things


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
