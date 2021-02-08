from DataStructure.Linear import Node


class OneWayLinkedList:
    def __init__(self):
        self.head = Node(None)

    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node
