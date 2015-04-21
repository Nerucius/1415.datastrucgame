from adt.Node import *


class LinkedList():
    def __init__(self):
        self._head = None

    def get(self, index):
        if index > len(self) - 1:
            return None
        if not self._head:
            return None

        probe = self._head
        while index > 0:
            probe = probe.next()
            index -= 1
        return probe

    def remove(self, item):
        if not self._head:
            False

        if self._head.get_data() == item:
            self._head = self._head.next()
            return True

        probe = self._head
        while probe and probe.next():
            if probe.next().get_data() == item:
                probe.set_next(probe.next().next())
                return True
            probe = probe.next()

        return False

    def is_empty(self):
        return self._head is None

    def append(self, item):
        # Insert at last position
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
        return self.get(index)

    def __delitem__(self, index):
        """ Delete Index """
        if index > len(self) - 1 or not self._head:
            return

        if index == 0:
            self._head = self._head.next()
            return

        probe = self._head
        while index > 1:
            probe = probe.next()
            index -= 1
        probe.set_next(probe.next().next())

    def __iter__(self):
        probe = self._head
        while probe:
            yield probe
            probe = probe.next()
        return

    def __str__(self):
        probe = self._head
        res = "["
        item_list = []

        while probe:
            item_list += [str(probe.get_data())]
            probe = probe.next()

        res = res + ", ".join(item_list)

        return res + "]"

    def __len__(self):
        i = 0
        probe = self._head
        while probe:
            probe = probe.next()
            i += 1
        return i

    @staticmethod
    def test():
        linked = LinkedList()

        linked.append("zero")
        linked.append("uno")
        linked.append("dos")

        print linked
        print "lenght:", len(linked)
        linked.insert(0, "NUEVO")
        print linked

        print "for: ",
        for item in linked:
            print item.get_data(),

        print "\nitem at index 1:", linked[1].get_data()

        print linked.remove("zero")
        print "removed item:", linked


LinkedList.test()
