class Queue(object):
    """Implementacion de la estructura Cola"""

    def __init__(self):
        self.__data = []

    def get(self, index):
        return self.__data[index]

    def insert(self, index, item):
        self.__data.insert(index, item)

    def remove(self, item):
        self.__data.remove(item)

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        return self.__data.pop(0)

    def isEmpty(self):
        return self.__data == []

    # Overloaded methods

    def __str__(self):
        return ''.join(str(elem) + ', ' for elem in self.__data)

    def __getitem__(self, i):
        return self.__data[i]

    def __len__(self):
        return len(self.__data)