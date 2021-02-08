class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_pre(self):
        return self.pre

    def set_pre(self, new_pre):
        self.pre = new_pre
