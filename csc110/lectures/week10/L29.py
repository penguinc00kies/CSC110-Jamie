"""CSC110 Lecture 27 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
from typing import Any


####################################################################################################
# Demo 2 (see Demo 1 below)
####################################################################################################
class EmptyStackError(Exception):
    """Exception raised when calling pop on an empty stack."""


class Stack:
    """A last-in-first-out (LIFO) stack of items."""

    def is_empty(self) -> bool:
        """Return whether this stack contains no items."""

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.
        """


class Stack1:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in first-in, last-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    >>> s = Stack1()
    >>> s.is_empty()
    True
    >>> s.push('hello')
    >>> s.is_empty()
    False
    >>> s.push('goodbye')
    >>> s.pop()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - _items: The items stored in the stack. The end of the list represents
    #     the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack.
        """
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        # return self._items == []
        return len(self._items) == 0

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop()


class Stack2:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    >>> s = Stack2()
    >>> s.is_empty()
    True
    >>> s.push('hello')
    >>> s.is_empty()
    False
    >>> s.push('goodbye')
    >>> s.pop()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - items: a list containing the items in the stack. The FRONT of the list
    #            represents the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return len(self._items) == 0

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        # list.insert(self._items, 0, item)
        self._items.insert(0, item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop(0)


####################################################################################################
# Demo 1
####################################################################################################
def push_and_pop(stack: ..., item: Any) -> None:  # What should the type annotation be?
    """Push item onto stack and then pop it from stack."""
    stack.push(item)
    stack.pop()


# def push_and_pop(stack: Stack1, item: Any) -> None:
#     stack.push(item)
#     stack.pop()
#
#
# def push_and_pop(stack: Stack2, item: Any) -> None:
#     stack.push(item)
#     stack.pop()
#
#
# def push_and_pop(stack: Any, item: Any) -> None:
#     stack.push(item)
#     stack.pop()


####################################################################################################
# Demo 3
####################################################################################################
# >>> my_stack = Stack1()
# >>> type(my_stack) is Stack1
# True
# >>> type(my_stack) is Stack
# False
# >>> isinstance(my_stack, Stack1)
# True
# >>> isinstance(my_stack, Stack)
# True
