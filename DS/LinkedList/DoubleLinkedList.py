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
            # 新结点指针指向原头部结点
            node.next = self._head
            # 原头部 prev 指向 新结点
            self._head.prev = node
            # head 指向新结点
            self._head = node
