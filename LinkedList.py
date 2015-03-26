from Node import *


class LinkedList():

    def __init__(self):
        self.__head = None

    def __len__(self):
        pass

    def get (self, index):
        pass

    def isEmpty(self):
        return self.__head ==None

    def insert(self,index,item):
        pass

    def remove(self,item):
        pass

    def enqueue (self, item):
        new_node= Node()
        new_node.set_data(item)

        if self.__head == None:
            self.__head = Node(item)
        else:
            probe = self.__head
            while (probe.next() != None):
                probe = probe.next()

            probe.set_next(new_node)

    def dequeue (self):
        if len(self)==1:
            return self.__head
            self.__head = None
        else:
            pass

    def __str__(self):
        probe = self.__head
        str = "["

        while probe != None:
            str += probe.get_data() + ", "
            probe = probe.next()

        return str + "]"

    def __len__(self):
        pass

    @staticmethod
    def test():
        llist = LinkedList()
        llist.enqueue("UNO")
        llist.enqueue("dos")
        llist.enqueue("tres")

        print llist

LinkedList.test()