


class Node():

    def __init__(self, item=None):
        self.__data = item
        self.__next = None
        self.__prev = None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data= data

    def next(self):
        return self.__next

    def set_next(self,next):
        self.__next= next

    def prev(self):
        return self.__prev

    def set_prev(self, prev):
        self.__prev= prev
