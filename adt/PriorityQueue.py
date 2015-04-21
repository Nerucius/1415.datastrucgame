from adt.Queue import *


class PriorityQueue(Queue):
    """Cola de prioridad, hereda de una cola pero inserta los elementos en orden,
    por defecto ascendiente"""

    def __init__(self):
        Queue.__init__(self)

    def enqueue(self, el):
        if self.is_empty():
            self.insert(0, el)

        elif el <= self.get(0):
            self.insert(0, el)

        else:
            inserted, i = False, 0
            while i < (len(self) - 1) and not (inserted):
                if self.get(i) < el <= self.get(i + 1):
                    self.insert(i + 1, el)
                    inserted = True
                i += 1
            if not inserted:
                self.insert(len(self), el)

    @staticmethod
    def test():
        queue = PriorityQueue()

        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(1)
        print queue

        queue.dequeue()
        print queue

        queue.dequeue()
        print queue

        queue.dequeue()
        print queue

if __name__ == "__main__":
    PriorityQueue.test()