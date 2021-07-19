from Node import Node


class DoubleLinkedList:
    def __init__(self):
        self._head = None

    def head(self):
        return self._head

    def add(self, item):
        node = Node(item)

        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.pre = node
            self._head = node

    def is_empty(self):
        return self._head is None

    def get_node(self, index):
        i = 0
        cur = self._head

        while cur != None and i < index:
            cur = cur.next
            i += 1

        return cur

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            node.pre = cur
            cur.next = node

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.value
            cur = cur.next
