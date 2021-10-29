"""Can I mutate an unmutatable attribute of a dataclass within a function?"""
from dataclasses import dataclass


@dataclass
class Fruit:
    """"A fruit object found anywhere"""
    color: str
    price: int

def change_price_of_fruit(old_price: int, new_price: int) -> int:
    """docstring"""
    old_price = new_price
    return new_price
