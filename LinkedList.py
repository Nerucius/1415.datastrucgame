from Node import *


class LinkedList():

    def __init__(self):
        self._head = None

    def __len__(self):
        if not self._head : return 0
        probe= self._head
        count =1
        while probe.next:
            conunt +=1
            probe = probe.next
        return count

    def get (self, index):
        if index > len(self)-1: return None
        if not self._head: return None

        probe = self._head
        while index>0:
            probe=probe.next
            index-=1
        return probe

    def __getitem__(self, index):
        return self.get(index)

    def isEmpty(self):
        return self._head ==None

    def append(self, item):
        self.insert(len(self)-1, item)

    def insert(self,index,item):
        if not self._head:
            self._head = Node(item)
            return

        probe= self._head

        while index>0:
            if not probe.next():
                probe.set_next(Node(item))
                return

            probe= probe.next()
            index-=1

        temp = probe.next()
        probe.set_next(Node(item))
        probe.next().set_next(temp)

    def __delitem__(self, index):
        """ Eliminar Index """
        if index > len(self)-1 or not self._head: return

        if index == 0:
            self._head = self._head.next()
            return

        probe = self._head
        while index>1:
            probe = probe.next()
            index-=1
        probe.set_next(probe.next().next())

    def __iter__(self):
        probe = self._head
        while probe:
            yield probe
            probe = probe.next()
        return

    def remove(self, item):
        if not self._head: return

        probe = self._head
        while probe:
            if probe.next().get_data() == item:
                probe.set_next(probe.next().next())
                return True
            probe = probe.next()

        return False

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
        llist = LinkedList()
        llist.append("UNO")
        print llist
        llist.append("dos")
        print llist
        llist.append("tres")
        print llist


        llist.remove("dos")
        print llist

        del llist[0]
        print "deleted 0", llist

        llist.append("QUaTRO")

        for node in llist:
            print node.get_data(),