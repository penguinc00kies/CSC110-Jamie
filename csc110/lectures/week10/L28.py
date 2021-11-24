"""CSC110 Lecture 28 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
from typing import Any


class EmptyQueueError(Exception):
    """Exception raised when calling dequeue on an empty queue."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'dequeue may not be called on an empty queue'


####################################################################################################
# Demo - Implementing Queue
####################################################################################################
class Queue:
    """A first-in-first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the most recently-added item is the one that is removed.

    >>> q = Queue()
    >>> q.is_empty()
    True
    >>> q.enqueue('hello')
    >>> q.is_empty()
    False
    >>> q.enqueue('goodbye')
    >>> q.dequeue()
    'hello'
    >>> q.dequeue()
    'goodbye'
    >>> q.is_empty()
    True
    """

    def __init__(self) -> None:
        """Initialize a new empty queue."""

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.
        """

    def enqueue(self, item: Any) -> None:
        """Add <item> to the back of this queue.
        """

    def dequeue(self) -> Any:
        """Remove and return the item at the front of this queue.

        Raise an EmptyQueueError if this queue is empty.
        """


####################################################################################################
# Exercise 2
####################################################################################################
class PriorityQueueUnsorted:
    """A queue of items that can be dequeued in priority order.

    When removing an item from the queue, the highest-priority item is the one
    that is removed.

    >>> pq = PriorityQueueUnsorted()
    >>> pq.is_empty()
    True
    >>> pq.enqueue(1, 'hello')
    >>> pq.is_empty()
    False
    >>> pq.enqueue(5, 'goodbye')
    >>> pq.enqueue(2, 'hi')
    >>> pq.dequeue()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - _items: A list of the items in this priority queue.
    #             Each element is a 2-element tuple where the first element is
    #             the priority and the second is the item.

    _items: list[tuple[int, Any]]

    def __init__(self) -> None:
        """Initialize a new and empty priority queue."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this priority queue contains no items.
        """
        return self._items == []

    def enqueue(self, priority: int, item: Any) -> None:
        """Add the given item with the given priority to this priority queue.
        """
        self._items.append((priority, item))

    def dequeue(self) -> Any:
        """Remove and return the element of this priority queue with the highest priority.

        Preconditions:
            - not self.is_empty()
        """
        highest_priority = max({element[0] for element in self._items})
        highest_priority = max(self._items[0])
        length = len(self._items)
        for i in range(0, len(self._items)):
            if self._items[i][0] == highest_priority:
                return self._items.pop(i)


####################################################################################################
# Demo 2
####################################################################################################
class PriorityQueueSorted:
    """A queue of items that can be dequeued in priority order.

    When removing an item from the queue, the highest-priority item is the one
    that is removed.
    """
    # Private Instance Attributes:
    #   - _items: A list of the items in this priority queue.
    #             Each element is a 2-element tuple where the first element is
    #             the priority and the second is the item.

    _items: list[tuple[int, Any]]

    def __init__(self) -> None:
        """Initialize a new and empty priority queue."""

    def is_empty(self) -> bool:
        """Return whether this priority queue contains no items.
        """

    def enqueue(self, priority: int, item: Any) -> None:
        """Add the given item with the given priority to this priority queue.
        """

    def dequeue(self) -> Any:
        """Remove and return the element of this priority queue with the highest priority.

        Preconditions:
            - not self.is_empty()
        """
