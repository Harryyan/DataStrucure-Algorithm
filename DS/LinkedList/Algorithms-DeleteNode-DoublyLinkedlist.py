from DoubleLinkedList import DoubleLinkedList
from Node import Node


def deleteNode(node: Node):
    print("")


def print_list(link_list):
    for i in link_list.items():
        print(i, end='\t')

    print('\n')


if __name__ == '__main__':
    link_list = DoubleLinkedList()
    for i in range(6):
        link_list.add(i)

    print_list(link_list)
