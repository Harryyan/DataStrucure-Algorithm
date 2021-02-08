from Node import Node


class OneWayLinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # 向链表头部添加元素
    def add(self, value):
        node = Node(value)
        node.next = self._head
        self._head = node

    # 向链表尾部添加元素
    def append(self, value):
        node = Node(value)

        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, value):
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(value)
        # 指定位置超过尾部，在尾部插入
        elif index > (self.length() - 1):
            self.append(value)
        else:
            # 创建元素结点
            node = Node(value)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, value):
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.value == value:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next

                cur = None
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    # 生成器
    def items(self):
        # 获取head指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            yield cur.value
            # 指针下移
            cur = cur.next

    def find(self, value):
        return value in self.items()

    def length(self):
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None 表示到达尾部
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        return count


if __name__ == '__main__':
    link_list = OneWayLinkedList()
    # 向链表尾部添加数据
    for i in range(5):
        link_list.append(i)
    # 向头部添加数据
    link_list.add(6)
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')
    # 链表数据插入数据
    link_list.insert(3, 9)
    print('\n', list(link_list.items()))
    # 删除链表数据
    link_list.remove(0)
    # 查找链表数据
    print(link_list.find(40))
