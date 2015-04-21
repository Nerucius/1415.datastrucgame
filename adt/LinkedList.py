from adt.Node import *


class LinkedList():
    """
        Default LinkedList implementation. Please note this class includes some bounds checking for
        future CircularLinkedLists.
    """
    def __init__(self):
        self._head = None

    def get(self, index):
        return self.get_node(index).get_data()

    def get_node(self, index):
        """ Helper method to get node at index. """
        if index < 0 or index >= len(self):
            return None
        if not self._head:
            return None

        probe = self._head
        while index > 0:
            probe = probe.next()
            index -= 1
        return probe

    def _get_tail(self):
        """ Helper method to get the tail node. """
        return self.get_node(len(self)-1)

    def remove(self, item):
        if not self._head:
            return False

        if self._head.get_data() == item:
            self._head = self._head.next()
            return True

        probe = self._head
        while probe.next() and probe.next() is not self._head:
            # print probe.next().get_data()
            if probe.next().get_data() == item:
                probe.set_next(probe.next().next())
                return True
            probe = probe.next()

        return False

    def is_empty(self):
        return self._head is None

    def append(self, item):
        """ Method to insert at the last position in the list """
        self.insert(len(self), item)

    def insert(self, index, item):
        # Special cases
        if not self._head:
            self._head = Node(item)
            return
        if index == 0:
            self._head = Node(item, self._head)
            return

        # Bounds checking, max insertion is at the end of list
        index = min(index, len(self))

        probe = self._head
        while index > 1:
            probe = probe.next()
            index -= 1

        probe.set_next(Node(item, probe.next()))

    # Overload Methods

    def __getitem__(self, index):
        """ Get Index """
        if index < 0 or index >= len(self):
            raise Exception("ArrayIndexOutOfBounds")
        return self.get(index)

    def __delitem__(self, index):
        """ Delete Index """
        if index < 0 or index >= len(self):
            raise Exception("ArrayIndexOutOfBounds")

        if index == 0:
            self._head = self._head.next()
            return

        probe = self._head
        while index > 1:
            probe = probe.next()
            index -= 1
        probe.set_next(probe.next().next())

    def __len__(self):
        if not self._head:
            return 0
        if self._head.next() is self._head:
            return 1

        i = 1
        probe = self._head.next()
        # While we exist, and we are not the head again
        while probe and probe is not self._head:
            probe = probe.next()
            i += 1
        return i

    def __str__(self):
        item_list = []
        for item in self:
            item_list += [str(item)]
        return "[" + ", ".join(item_list) + "]"

    def __iter__(self):
        """" Overload for iterator loops """
        if self.is_empty():
            return
        if self._head.next() is self._head:
            yield self._head.get_data()
            return

        # Average case len > 1
        yield self._head.get_data()
        probe = self._head.next()
        # While we exist and we are not the head again
        while probe and probe is not self._head:
            yield probe.get_data()
            probe = probe.next()
        return

    def print_nodes(self):
        """ Helper and debug method. """
        if len(self) == 0:
            return

        print self._head
        if len(self) == 1:
            return

        probe = self._head
        while probe.next() is not self._head:
            probe = probe.next()
            print probe

    @staticmethod
    def test():
        linked = LinkedList()

        linked.append("zero")
        linked.append("uno")
        linked.append("dos")

        print linked.get(0)
        print linked.get(2)

        print linked
        print "lenght:", len(linked)
        linked.insert(0, "NUEVO")
        print linked

        print "\nitem at index 1:", linked[1]

        print linked
        linked.remove("dos")
        print "removed item:"
        print linked

if __name__ == "__main__":
    LinkedList.test()