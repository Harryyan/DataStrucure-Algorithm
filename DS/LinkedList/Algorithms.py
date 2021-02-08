from LinkedList import SingleLinkedList
from Node import Node

# 输入一个单向链表，输出逆序反转后的链表;


def reverseByRecursion(node: Node, linked_list: SingleLinkedList):
    # 停止条件
    if node is None or node.next == None:
        linked_list.set_head(node)
        return node

    temp = reverseByRecursion(node.next, linked_list)
    temp.next = node

    print(id(temp))

    return temp.next


def reverse(linked_list: SingleLinkedList):
    head = link_list.head()

    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')

    print("\n")
    result = reverseByRecursion(head, link_list)
    result.next = None

    print(id(result))

    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')


if __name__ == '__main__':
    link_list = SingleLinkedList()
    # 向链表尾部添加数据
    for i in range(6):
        link_list.append(i)
    # 向头部添加数据
    link_list.add(7)

    # 链表数据插入数据
    link_list.insert(3, 9)
    print('\n')

    reverse(link_list)
