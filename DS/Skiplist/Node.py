from typing import List

class Node:
    def __init__(self, value, level):
        self._value = value
        # 当前节点在每个索引层的下一个节点
        self._forwards = [None] * level
