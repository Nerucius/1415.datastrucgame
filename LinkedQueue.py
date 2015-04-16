__author__ = 'xavier'

from LinkedList import *


class LinkedQueue(LinkedList):
    def __init__(self):
        super(LinkedQueue, self).__init__()

    def enqueue(self, item):
        new_node = Node(item)

        if self._head == None:
            self._head = Node(item)
        else:
            probe = self._head
            while (probe.next() != None):
                probe = probe.next()

            probe.set_next(new_node)

    def dequeue(self):
        if len(self) == 1:
            temp = self._head
            self._head = None
            return temp

        if len(self) == 2:
            temp = self._head.next()
            self._head.set_next(None)
            return temp

        probe = self._head
        while probe.next().next():
            probe = probe.next()

        temp = probe.next()
        probe.set_next(None)
        return temp



