"""
Author: Gurjot Kahlon
Last updated: October 18, 2026
Custom Queue (FIFO) and Stack (FILO) classes backed by a Python list.
Both classes expose the same methods (add, remove, is_empty) so that the
search code in game_data.py can switch between BFS (Queue) and DFS (Stack)
without any other changes. Index 0 is the beginning of the structure.
"""

class Queue():
    """ First in, first out (FIFO) structure used for breadth first search """

    def __init__(self):
        # The items currently in the queue; index 0 is the front
        self.items = []

    def add(self, item) -> None:
        """ "Enqueue" the item to the end of the queue """
        self.items.append(item)

    def remove(self):
        """ "Dequeue" the item from the front of the queue and return it """
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """ Returns whether or not the queue is empty """
        return len(self.items) == 0


class Stack():
    """ First in, last out (FILO) structure used for depth first search """

    def __init__(self):
        # The items currently in the stack; the last item is the top
        self.items = []

    def add(self, item) -> None:
        """ Push an item to the top (end) of the stack """
        self.items.append(item)

    def remove(self):
        """ Pop the item from the top (end) of the stack and return it """
        return self.items.pop()

    def is_empty(self) -> bool:
        """ Returns whether or not the stack is empty """
        return len(self.items) == 0
