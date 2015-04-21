class Node():
    def __init__(self, item=None, nxt=None, prev=None):
        self.__data = item
        self.__next = nxt
        self.__prev = prev

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def next(self):
        return self.__next

    def prev(self):
        return self.__prev

    def set_next(self, nxt):
        self.__next = nxt

    def set_prev(self, prev):
        self.__prev = prev
