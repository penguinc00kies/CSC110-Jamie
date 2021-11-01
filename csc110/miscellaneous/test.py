"""TEST"""
from typing import Callable
import math

s = 'gehknkwgnknwglllllslvglvmlsvlkvlmlkvlkmnblenmklenokgwnfnq da,.mckldnvksnvklwsvklsnmvklsnvqmlm,mzvjsdv, ,sdv'

print(s)

g = 'gehknkwgnknwglllllslvglvmlsvlkvlmlkvlkmnblenmklenokgwnfnq da,.mckldnvks'\
            'nvklwsvklsnmvklsnvqmlm,mzvjsdv, ,sdv'

print(g)


def compare_strings(str1: str, str2: str, func: Callable[[str, str], bool]) -> bool:
    """Compare strings"""
    # >>> compare_strings('Jamie', 'Matteo', longer_string)
    # 'Matteo'
    return func(str1, str2)


def longer_string(str1: str, str2: str) -> str:
    """Longer string"""
    if len(str1) >= len(str2):
        return str1
    else:
        return str2


print(any([all([x < y for y in set()]) for x in set()]))

print([x for x in range(5, 0, -1)])
