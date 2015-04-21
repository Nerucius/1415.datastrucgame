from adt.CircularLinkedList import *


class CircularDoubleLinkedList(CircularLinkedList):
    def __init__(self):
        CircularLinkedList.__init__(self)

    def insert(self, index, item):
        # Special cases
        if not self._head:
            self._head = Node(item)
            self._head.set_next(self._head)
            self._head.set_prev(self._head)
            return

        # Insert at index 0
        if index == 0:
            prev_head = self._head
            tail = self._get_tail()
            print "tail:", tail

            new_node = Node(item, prev_head, tail)
            self._head = new_node
            tail.set_next(new_node)
            prev_head.set_prev(new_node)

            return

        # Bounds checking, max insertion is at the end of list
        index = min(index, len(self))

        # General insertion
        probe = self._head
        while index > 1:
            probe = probe.next()
            index -= 1

        new_node = Node(item, probe.next(), probe)
        probe.next().set_prev(new_node)
        probe.set_next(new_node)


    def remove(self, item):
        if not self._head:
            return False

        # Special case for head
        if self._head.get_data() == item:
            tail = self._get_tail()
            # Move head to next item, set new head back to tail and tail to new head
            self._head = self._head.next()
            self._head.set_prev(tail)
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
        circular = CircularDoubleLinkedList()

        circular.append("zero")
        circular.append("uno")
        circular.append("dos")

        print ""
        print "Status:"
        print circular
        circular.print_nodes()
        print ""

        print "lenght:", len(circular)
        circular.insert(0, "NUEVO")
        print "inserted at 0:", circular

        print "\nitem at index 1:", circular[1], "\n"

        print "list:"
        print circular
        circular.remove("zero")
        print "removed item:"
        print circular

if __name__ == "__main__":
    CircularDoubleLinkedList.test()