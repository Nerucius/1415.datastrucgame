__author__ = 'xavier'

from adt.LinkedList import *

class LinkedStack(LinkedList):
    """
        Stack implementation using a LinkedList. It has been decided to use native LinkedList methods
        due to ease of implementation and to avoid bugs. All operations are near O(1) as they
        operate at the head of the LinkedList.
    """

    def __init__(self):
        LinkedList.__init__(self)

    def push(self, item):
        self.insert(0, item)

    def pop(self):
        item = self.get(0)
        self.remove(item)

        return item

    def peek(self):
        return self.get(0)

    @staticmethod
    def test():
        stack = LinkedStack()

        stack.push("Uno")
        stack.push("Dos")
        stack.push("Tres")
        print stack

        stack.pop()
        print stack

        stack.pop()
        print stack

        stack.pop()
        print stack

if __name__ == "__main__":
    LinkedStack.test()



