def propositional_formula(p: bool, q: bool, r: bool) -> bool:
    """Return the value of ((p ⇒ q) ∧ r) ⇔ (p ⇒ (q ∧ r)).

    >>> propositional_formula(True, False, False)
    True
    >>> propositional_formula(False, False, False)
    False
    """
    left = (not p or q) and r
    right = not p or (q and r)
    return left == right

# a predicate is a function that returns a Boolean
