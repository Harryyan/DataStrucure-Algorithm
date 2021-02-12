from Node import Node


class DoubleLinkedList:
    def __init__(self):
        self._head = None

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def is_empty(self):
        return self._head is None

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            node.prev = cur
            cur.next = node

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.value
            cur = cur.next
