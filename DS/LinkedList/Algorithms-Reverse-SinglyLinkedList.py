from SingleLinkedList import SingleLinkedList
from Node import Node

# 输入一个单向链表，输出逆序反转后的链表;


def reverseByLoop(node: Node):
    if node == None or node.next == None:
        return node

    current = node
    pre = None
    while current is not None:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre


def reverseByRecursion(node: Node, linked_list: SingleLinkedList):
    # 停止条件
    if node is None or node.next == None:
        linked_list.set_head(node)
        return node

    temp = reverseByRecursion(node.next, linked_list)
    temp.next = node

    print(id(temp))

    return temp.next


def reverse_by_recursion(head: Node):
    if head is None or head.next == None:
        return head

    new_head = reverse_by_recursion(head.next)
    head.next.next = head
    head.next = None

    return new_head


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


def print_list(link_list):
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')

    print('\n')


if __name__ == '__main__':
    link_list = SingleLinkedList()
    # 向链表尾部添加数据
    for i in range(6):
        link_list.append(i)
    # 向头部添加数据
    link_list.add(7)

    # 链表数据插入数据
    link_list.insert(3, 9)

    # reverse(link_list)
    print_list(link_list)

    new_head = reverse_by_recursion(link_list.head())
    link_list.set_head(new_head)

    print_list(link_list)
