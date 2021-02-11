from Node import Node


class DoubleLinkedList:
    def __init__(self):
        self._head = None

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            # 头部结点指针修改为新结点
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
