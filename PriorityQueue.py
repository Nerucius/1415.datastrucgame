from Queue import *


class PriorityQueue(Queue):
    """Cola de prioridad, hereda de una cola pero inserta los elementos en orden,
    por defecto ascendiente"""

    def __init__(self):
        super(PriorityQueue, self).__init__()

    def enqueue(self, el):
        if self.isEmpty():
            self.insert(0, el)

        elif el <= self.get(0):
            self.insert(0, el)

        else:
            inserted, i = False, 0
            while i < (len(self) - 1) and not (inserted):
                if self.get(i) < el and el <= self.get(i + 1):
                    self.insert(i + 1, el)
                    inserted = True
                i = i + 1
            if not (inserted): self.insert(len(self), el)