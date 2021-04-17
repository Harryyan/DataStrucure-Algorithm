from Node import Node
import random


class SkipList:
    _MAX_LEVEL = 8

    def __init__(self):
        # 当前索引总层数
        self.levelCount = 1

        # 带头结点
        self.head = Node()
        self.head._forwards = [None] * self._MAX_LEVEL

    def insert(self, value):
        level = self._random_level()
        if self._level_count < level:
            self._level_count = level

        new_node = Node(value, [None] * level)
        update = [self.head] * level

        p = self.head
        for i in range(level - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            if p._forwards[i] and p._forwards[i]._data == value:
                # 说明已经存储该节点，不需要再插入
                return False
            update[i] = p  # 找到插入的位置

        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]  # new_node.next = prev.next
            update[i]._forwards[i] = new_node  # prev.next = new_node

        return True

    # 确保Node添加到每层索引的概率是1 / 2
    def _random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < self._MAX_LEVEL:
            level += 1
        return level