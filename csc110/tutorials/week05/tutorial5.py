"""CSC110 Tutorial 5: Mutation"""

from dataclasses import dataclass

# The annotation Any (case-sensitive) can be used to indicate "any type"
from typing import Any


def only_evens(lst: list[list[int]]) -> list[list[int]]:
    """Return a new list of the lists in lst that contain only even integers.

    lst must not be mutated.

    >>> only_evens([[1, 2, 4], [4, 0, 6], [22, 4, 3], [2]])
    [[4, 0, 6], [2]]
    """

    even_lists = []

    breakpoint()
    for sublist in lst:
        if all([x % 2 == 0 for x in sublist]):
            list.append(even_lists, sublist)

    return even_lists


def get_quantities(table_to_foods: dict[str, list[str]]) -> dict[str, int]:
    """Return a new dictionary where each key is a food from table_to_foods and
    each value is the quantity of that food that was ordered.

    The table_to_foods dict has table names as keys (e.g., 't1', 't2', and
    so on) and each value is a list of foods ordered for that table.

    >>> ex_dict = {'t1': ['Vegetarian stew', 'Poutine', 'Vegetarian stew'],\
't3': ['Steak pie', 'Poutine', 'Vegetarian stew'], 't4': ['Steak pie', 'Steak pie']}
    >>> get_quantities(ex_dict) == {'Vegetarian stew': 3, 'Poutine': 2, 'Steak pie': 3}
    True
    """

    food_to_quantity = {}

    breakpoint()
    for foods in table_to_foods.values():
        for food in foods:
            if food not in food_to_quantity:
                food_to_quantity[food] = 0
            food_to_quantity[food] = food_to_quantity[food] + 1

    return food_to_quantity


@dataclass
class CashRegister:
    """A cash register with separate totals for value ($) of coins and bills within.

    Representation Invariants:
        - coins >= 0
        - bills >= 0
    """
    coins: float
    bills: float


def count_money(money: list[str]) -> CashRegister:
    """Return a CashRegister with the total dollar values for all the coins and bills in
    money, which is a list of strings representing coins or bills of various denominations.

    Preconditions:
        - all([item in ['Nickel', 'Dime', 'Quarter', 'Loonie', 'Toonie', 'Five', 'Ten',
        'Twenty Five', 'Fifty', 'One Hundred', 'One Thousand'] for item in money])

    >>> count_money(['Nickel', 'Toonie', 'Five'])
    CashRegister(coins=2.05, bills=5.0)
    >>> count_money(['Five', 'Ten',\
        'Twenty Five', 'Fifty', 'One Hundred', 'One Thousand'])
    CashRegister(coins=0.0, bills=1190.0)
    """
    register_so_far = CashRegister(0.00, 0.00)
    # Or you can make a dictionary mapping the name of each denomination to its value
    for denomination in money:
        if denomination == 'Nickel':
            register_so_far.coins += 0.05
        elif denomination == 'Dime':
            register_so_far.coins += 0.10
        elif denomination == 'Quarter':
            register_so_far.coins += 0.25
        elif denomination == 'Loonie':
            register_so_far.coins += 1.00
        elif denomination == 'Toonie':
            register_so_far.coins += 2.00
        elif denomination == 'Five':
            register_so_far.bills += 5.00
        elif denomination == 'Ten':
            register_so_far.bills += 10.00
        elif denomination == 'Twenty Five':
            register_so_far.bills += 25.00
        elif denomination == 'Fifty':
            register_so_far.bills += 50.00
        elif denomination == 'One Hundred':
            register_so_far.bills += 100.00
        else:
            register_so_far.bills += 1000.00

    return register_so_far


def square_list(lst: list[int]) -> list[int]:
    """Return a new list of every element in lst squared.

    >>> square_list([1, 2, 3])
    [1, 4, 9]
    """
    # lst2 = []
    # for item in lst:
    #     lst2.extend(item)
    # return lst2
    # list.extend() only takes iterables as arguments. It would be better to use list.append()
    # here. Also, item needs to be squared
    lst2 = []
    for item in lst:
        lst2.append(item ** 2)
    return lst2


# courses = {'CSC110', 'CSC111', 'MAT157'}
# courses = courses.remove('MAT157')
# courses = courses.add('MAT137')
# Item mutation statements don't return anything and thus, do not have to be assigned to be anything,
# it's useless to do so anyways. So just remove the 'courses = ' and everything will work


def swap_values(d: dict, key1: Any, key2: Any) -> None:
    """Update d by swapping the values for key1 and key2.

    Preconditions:
        - key1 in d
        - key2 in d

    >>> food_prices = {'Apple': 2.25, 'Orange': 2.5}
    >>> swap_values(food_prices, 'Apple', 'Orange')
    >>> food_prices == {'Apple': 2.5, 'Orange': 2.25}
    True
    """
    # d[key1] = d[key2]
    # d[key2] = d[key1]
    # d[key2] is just being reassigned its own value. Since you can't swap both values simultaneously,
    # there must be a placeholder to 'hold' the original value to assign later.
    value1_placeholder = d[key1]
    d[key1] = d[key2]
    d[key2] = value1_placeholder


def remove_composites(s: set[int]) -> None:
    """Update s by removing every element that is not a prime number.

    Note: `is_prime` is defined as in the course notes.

    >>> nums = {1, 2, 3, 4}
    >>> remove_composites(nums)
    >>> nums
    {2, 3}
    """
    # for n in s:
    #     if not is_prime(n):
    #        s = s - {n}
    # s = s - {n} is a reassignment statement and is creating a new id in memory. We don't want that.
    # It would be better to use a mutation method.
    composites = set()
    for n in s:
        if not is_prime(n):
            composites.add(n)
    for n in composites:
        s.remove(n)



def is_prime(p: int) -> bool:
    """Return whether p is prime."""
    possible_divisors = range(1, p + 1)
    return (
            p > 1 and
            all({d == 1 or d == p for d in possible_divisors if divides3(d, p)})  # <-- Note the "divides3"
    )


def divides3(d: int, n: int) -> bool:
    """Return whether d divides n."""
    if d == 0:
        # This is another new, equivalent check.
        return n == 0
    else:
        # This is a new but equivalent check.
        return n % d == 0


def square_list2(lst: list[int]) -> None:
    """Update lst by squaring every element.

    >>> ex_lst = [1, 2, 3]
    >>> square_list2(ex_lst)
    >>> ex_lst
    [1, 4, 9]
    """
    # for item in lst:
    #     item = item ** 2
    # This is meaningless, it's not actually assigning any value to an index in list. 'item' is a
    # useless variable that does nothing.
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2


def process_return(items: dict, register: CashRegister) -> None:
    """Return the total value of items being returned in items and update register to reflect
    the deductions. items is a dictionary mapping items being returned to their price.

    >>> register = CashRegister(10.00, 20.00)
    >>> process_return({'Apple': 2.25, 'Orange': 2.50, 'Banana': 1.65}, register)
    >>> register
    CashRegister(coins=10.0, bills=13.6)
    """
    total_value = sum(items.values())
    # if register.bills >= total_value:
    #     register.bills = register.bills - total_value
    # else:
    #     register.coins = register.coins - (total_value - register.bills)
    #     register.bills = 0.0
    # Object reassignment. Directly reassign the dataclass instance attributes rather than the
    # entire object itself.
    # if register.bills >= total_value:
    #     register.bills = register.bills - total_value
    # else:
    #     register.coins = register.coins - (total_value - register.bills)
    #     register.bills = 0.0
    # The code as-is has a possibility to violate the object invarients.


def make_full(lst: list[int]) -> None:
    """Update lst so that it includes, at the end, every integer between its min and max
    that is not already in lst.

    The new elements added to lst should be in ascending order.

    >>> ex_lst = [1, 7, 10, 2]
    >>> make_full(ex_lst)
    >>> ex_lst
    [1, 7, 10, 2, 3, 4, 5, 6, 8, 9]
    """
    # for num in range(min(lst), max(lst)):
    #     if num not in lst:
    #         lst = lst + [num]
    # Object reassignment. Use list.append()
    placeholder = lst.copy()
    for num in range(min(lst), max(lst)):
        if num not in lst:
            list.append(lst, num)
