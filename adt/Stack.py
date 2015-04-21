class Stack(object):
    """Implementacio d'una estructura Stack"""

    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return self.__items == []

    def get(self, index):
        return self.__data[index]

    def push(self, obj):
        self.__items.append(obj)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        if len(self) > 0:
            return self.__items[-1]
        else:
            return None

    # Overloaded Methods

    def __str__(self):
        return ''.join(str(elem) + ', ' for elem in self.__items)

    def __len__(self):
        return len(self.__items)