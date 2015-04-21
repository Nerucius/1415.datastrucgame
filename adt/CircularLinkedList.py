from adt.LinkedList import *


class CircularLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def insert(self, index, item):
        LinkedList.insert(self, index, item)

        # Link queue
        self._get_node(len(self)-1).set_next(self._head)

    def remove(self, item):
        if not self._head:
            return False

        # Special case for head
        if self._head.get_data() == item:
            tail = self._get_tail()
            self._head = self._head.next()
            tail.set_next(self._head)
            return True

        probe = self._head
        # While we have next, and the next one is not the head
        while probe.next() and probe.next() is not self._head:
            # print probe.next().get_data()
            if probe.next().get_data() == item:
                probe.set_next(probe.next().next())
                return True
            probe = probe.next()

        return False

    @staticmethod
    def test():
        circular = CircularLinkedList()

        circular.append("ZERO")
        circular.append("ONE")
        circular.append("TWO")
        print "3 items:", circular
        print "item 1:", circular.get(1)

        circular.insert(2, "NEW TWO")
        print "insert at 2", circular

        circular.remove("ZERO")
        print "remove ZERO:", circular

if __name__ == "__main__":
    CircularLinkedList.test()
