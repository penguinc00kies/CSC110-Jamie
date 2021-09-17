"""
Testing
"""
def add_two(x: int) -> int:
    """Return x plus two

    >>> add_two(6)
    8
    >>> add_two(15)
    17
    """
    x += 2
    return x

def add_to_list(lst: list, item: str) -> list:
    """Append str to the start of lst

    >>> add_to_list(['milk'], 'cereal')
    ['cereal', 'milk']
    """
    placeholder_list = [item]
    lst = placeholder_list + lst
    return lst

x = 7
print('Inside:', add_two(x))
print('Outside:', x)
print()
lst = ['jam']
print('Inside:', add_to_list(lst, 'peanut butter'))
print('Outside:', lst)
