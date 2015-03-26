


class LinkedList():

    def __init__(self):
        self.__head = None

    def __len__(self):
        pass

    def get (self, index):
        pass

    def isEmpty(self):
        return self.__head==None

    def insert(self,index,item):
        pass

    def remove(self,item):
        pass

    def enqueue (self, item):
        new_node= Node()
        new_node.set_data(item)

        if self.__head == None:
            self.__head = item
        else :
            probe = self.__head.next()
            while (probe != None):
                probe = probe.next()

            probe.set_next(new_node)

    def dequeue (self):
        if len(self)==1:
            return self.__head
            self.__head = None
        else:
            pass

    def len (self):
        pass

    @staticmethod
    def test():
        list = LinkedList()
        list.enqueue("UNO")
        list.enqueue("dos")
        list.enqueue("tres")
