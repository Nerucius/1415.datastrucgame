from adt.LinkedQueue import *

class LinkedPriorityQueue(LinkedQueue):
    """
        Linked implementation of PriorityQueue, same code exactly as PriorityQueue
        but extends the Linked version of queue this time.

        Extracts elements smallest first.
    """

    def __init__(self):
        LinkedQueue.__init__(self)
        # super(PriorityQueue, self).__init__()

    def enqueue(self, el):
        if self.is_empty():
            self.insert(0, el)

        elif el <= self.get(0):
            self.insert(0, el)

        else:
            inserted, i = False, 0
            while i < len(self) - 1 and not inserted:
                if self.get(i) < el <= self.get(i + 1):
                    self.insert(i + 1, el)
                    inserted = True
                i += 1
            if not inserted:
                self.insert(len(self), el)

    @staticmethod
    def test():
        queue = LinkedPriorityQueue()

        queue.enqueue(2)
        queue.enqueue(5)
        queue.enqueue(1)
        queue.enqueue(3)
        print queue

        queue.dequeue()
        print queue

        queue.dequeue()
        print queue

        queue.dequeue()
        print queue

if __name__ == "__main__":
    LinkedPriorityQueue.test()