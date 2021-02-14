from DoubleLinkedList import DoubleLinkedList
from Node import Node


def deleteNode(node: Node, head: Node):
    # head
    if node.pre == None:
        temp = head
        head = node.next
        head.pre = None
        temp = None
    elif node.next == None:
        node.pre.next = None
        node.pre = None
        node = None
    else:
        node.pre.next = node.next
        node.next.pre = node.pre
        node = None


def print_list(link_list):
    for i in link_list.items():
        print(i, end='\t')

    print('\n')


if __name__ == '__main__':
    link_list = DoubleLinkedList()
    for i in range(6):
        link_list.add(i)

    print_list(link_list)

    # 2nd node
    head = link_list.head()
    node = link_list.get_node(2)
    print(head.next.pre)
    deleteNode(node, head)

    print_list(link_list)
