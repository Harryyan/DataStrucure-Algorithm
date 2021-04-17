from typing import List


class Node:

    
    def __init__(self, value, maxlevel):
        self.value = value
            # 当前索引总层数。
            # 索引从 0 开始计数，到 maxLevel-1 为止。
            # 第 0 层为原始链表，从下往上依次建立索引，最上层为第 maxLevel-1 层索引。

        self.maxLevel = 0
        self.forwards = [None] * maxlevel
