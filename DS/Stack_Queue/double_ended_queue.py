class DoubleEndedQueue:

    def __init__(self):
        self.__content = []

    def add_front(self, value):
        self.__content.insert(0, value)

    def add_rear(self, value):
        self.__content.append(value)

    def remove_front(self):
        if not self.is_empty():
            self.__content.pop(0)
        else:
            return None

    def remove_rear(self):
        if not self.is_empty():
            self.__content.pop()
        else:
            return None

    def size(self):
        return len(self.__content)

    def is_empty(self):
        return not self.__content
