from SingleLinkedList import SingleLinkedList
from Node import Node

# 输入一个单向链表，输出该链表中倒数第k个节点，链表的倒数第0个节点为链表的尾指针

# 考虑对称性，切忌先遍历


def print_list(link_list):
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')

    print('\n')


def getKthNodeBackforward(list: SingleLinkedList, k: int):
    p1 = p2 = list.head()
    i = 0

    while i < k and p2 is not None:
        p2 = p2.next
        i += 1

    if p2 is None:
        return None
    else:
        while p2.next is not None:
            p1 = p1.next
            p2 = p2. next

        return p1


if __name__ == "__main__":
    link_list = SingleLinkedList()
    for i in range(6):
        link_list.add(i)

    print_list(link_list)
    result = getKthNodeBackforward(link_list, 5)

    if result is not None:
        print(result.value)
    else:
        print("None")
