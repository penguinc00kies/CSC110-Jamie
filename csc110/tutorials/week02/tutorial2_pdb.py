def union_and_intersection(set1: set, set2: set) -> list:
    """Return a list containing the union and intersection of set1 and set2.

    >>> union_and_intersection({1, 2, 3}, {2, 5, 10, 20})
    [{1, 2, 3, 5, 10, 20}, {2}]
    """
    breakpoint()
    union = set.union(set1, set2)
    intersection = set.intersection(set1, set2)
    return [union, intersection]
