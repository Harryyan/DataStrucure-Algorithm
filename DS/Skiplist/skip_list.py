from Node import Node
import random


class SkipList:
    _MAX_LEVEL = 8

    def __init__(self):
        # 当前索引总层数
        self.levelCount = 1

        # 带头结点
        self.head = Node(None, SkipList._MAX_LEVEL)

    def insert(self, value):
        level = self._random_level()
        if self.levelCount < level:
            self.levelCount = level

        new_node = Node(value, level)
        update = [self.head] * level

        p = self.head
        for i in range(level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].value < value:
                p = p.forwards[i]
            if p.forwards[i] and p.forwards[i].value == value:
                # 说明已经存储该节点，不需要再插入
                return False
            update[i] = p  # 找到插入的位置

        for i in range(level):
            new_node.forwards[i] = update[i].forwards[i]  # new_node.next = prev.next
            update[i].forwards[i] = new_node  # prev.next = new_node

        return True

    def delete(self, value):
        update = [None] * self.levelCount
        p = self.head
        for i in range(self.levelCount - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].value < value:
                p = p.forwards[i]
            update[i] = p

        if p.forwards[0] and p.forwards[0].value == value:
            for i in range(self.levelCount - 1, -1, -1):
                if update[i].forwards[i] and update[i].forwards[i].value == value:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]
                    # Similar to prev.next = prev.next.next
            return True
        else:
            return False

    def find(self, value):
        p = self.head

        for i in range(self.levelCount - 1, -1, -1):  # Move down a level
            while p.forwards[i] and p.forwards[i].value < value:
                p = p.forwards[i]  # Move along level
            if p.forwards[i] and p.forwards[i].value == value:
                return p.forwards[i]
        # 到这一步，说明没有找到
        return None

    def find_range(self, begin_value, end_value):
        p = self.head
        begin = None
        for i in range(self.levelCount - 1, -1, -1):  # Move down a level
            while p.forwards[i] and p.forwards[i].value < begin_value:
                p = p.forwards[i]  # Move along level
            if p.forwards[i] and p.forwards[i].value >= begin_value:
                begin = p.forwards[i]

        if begin is None:
            return None  # 没有找到
        else:
            result = []
            while begin and begin.value <= end_value:
                result.append(begin)
                begin = begin.forwards[0]
            return result

    def pprint(self):
        """
        打印跳表
        """
        skiplist_str = ""
        i = self.levelCount - 1
        while i >= 0:
            p = self.head
            skiplist_str = f"head {i}: "
            while p:
                if p.value:
                    skiplist_str += "->" + str(p.value)
                p = p.forwards[i]
            print(skiplist_str)
            i -= 1

    # 确保Node添加到每层索引的概率是1 / 2
    def _random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < self._MAX_LEVEL:
            level += 1
        return level


if __name__ == "__main__":
    l = SkipList()

    for i in range(0, 40, 3):
        l.insert(i)
    l.pprint()
    if l.delete(15):
        print("delete 15 success.")
    l.pprint()
    if not l.delete(16):
        print("delete 16 fail.")
    l.pprint()
    print("find 9 : ", l.find(9).value)
    print("find data between 4 and 10:")
    for d in l.find_range(4, 10):
        print(d.value, end="->")
