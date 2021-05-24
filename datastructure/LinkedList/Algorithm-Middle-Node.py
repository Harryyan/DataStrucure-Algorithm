from SingleLinkedList import SingleLinkedList
from Node import Node


# 求链表的中间节点，如果链表的长度为偶数，返回中间两个节点的任意一个，若为奇数，则返回中间节点
# 类似变体: 求1/3, 1/4处的节点

def getMiddleNode(list: SingleLinkedList):
    if list is None:
        return None

    p1 = p2 = list.head()

    while p2 is not None and p2.next is not None:
        p2 = p2.next.next
        p1 = p1.next

    return p1


def print_list(link_list):
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')

    print('\n')


if __name__ == "__main__":
    link_list = SingleLinkedList()
    for i in range(1):
        link_list.add(i)

    print_list(link_list)

    result = getMiddleNode(link_list)

    if result is not None:
        print(result.value)
    else:
        print(None)
