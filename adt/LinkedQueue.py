from adt.LinkedList import *


class LinkedQueue(LinkedList):
    """
        Linked Queue implementation, objects are added to
        the end of the Queue and are taken from the beginning.
    """

    def __init__(self):
        LinkedList.__init__(self)

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        item = self.get(0)
        self.remove(item)
        return item

    @staticmethod
    def test():
        queue = LinkedQueue()

        queue.enqueue("Uno")
        queue.enqueue("Dos")
        queue.enqueue("Tres")
        print queue

        queue.dequeue()
        print queue

        queue.dequeue()
        print queue

        queue.dequeue()
        print queue


if __name__ == "__main__":
    LinkedQueue.test()



