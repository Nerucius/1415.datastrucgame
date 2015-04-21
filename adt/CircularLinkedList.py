from adt.LinkedList import *


class CircularLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def insert(self, index, item):
        LinkedList.insert(self, index, item)

        if len(self) == 1:
            self._head.set_next(self._head)

    def __len__(self):
        n = 0
        probe = self._head
        while probe and probe.next() != self._head:
            n += 1
            probe = probe.next
        return n

    def __str__(self):
        probe = self._head
        res = "["
        item_list = []

        while probe and probe.next() != self._head:
            item_list += [str(probe.get_data())]
            probe = probe.next()

        res += ", ".join(item_list)

        return res + "]"

    @staticmethod
    def test():
        list = CircularLinkedList()
        list.append("Uno")
        list.append("Dos")
        list.append("Tres")
        list.append("Cuatro")

        print list

CircularLinkedList.test()
