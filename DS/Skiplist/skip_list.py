from Node import Node
import random

class SkipList:
    MAX_LEVEL = 16

    def __init__(self):
        self.levelCount = 1

        # 带头结点
        head = Node()

    def random_level(self):
        return 0