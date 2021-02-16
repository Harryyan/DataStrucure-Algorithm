from SingleLinkedList import SingleLinkedList
from Node import Node

# 题目1:
# 输入一个单向链表，判断链表是否有环？

# 看是否能相遇; walker 和 runner 类型


def isCircleLinkedList(list: SingleLinkedList):
    walker = runner = list.head()
    result = False

    while walker is not None and runner.next is not None:
        walker = walker.next
        runner = runner.next.next

        if walker == runner:
            result = True
            break

    return result

# 题目2:
# 输入一个单向链表，判断链表是否有环。如果链表存在环，如何找到环的入口点？

# 还是 walker 和 runner 的解决思路, runner每次走2步，walker一步，意味着
# 他们相遇时，一个走了2n步，一个走了n步；那么，walker再走n步就能返回原来的相遇
# 点，也意味着，runner返回头结点后(1 by 1)再走n步也能到原来的相遇点；由于环的入口到相遇
# 点的距离都是一样的，也就意味着他们能在入口处相遇


def findEntryNodeOfCircleList(list: SingleLinkedList):
    walker = runner = list.head()

    while walker is not None and runner.next is not None:
        walker = walker.next
        runner = runner.next.next

        if walker == runner:
            break

    runner = list.head()

    while runner != walker:
        runner = runner.next
        walker = walker.next

    return walker


# 题目3:
# 输入2个单向有环链表头指针，如何判断相交.
# 环上的点总是在两个链表中的, 只要找到一条
# 链表上环上的一点，再判断该点是否在另一条
# 上即可；

def isTwoCircleListIntercept(h1: Node, h2: Node):
    walker = runner = h1
    result = False

    while walker is not None and runner.next is not None:
        walker = walker.next
        runner = runner.next.next

        if walker == runner:
            break

    while h2 is not None:
        h2 = h2.next

        if h2 == walker:
            result = True
            break

    return result


# 题目4:
# 两个无环单链表相交，怎么求出他们相交的第一个节点呢？
# 链表长度相减，长的那个先向后移动差值个node，然后
# 两个链表同时向后一步一步移动

def findFirstInterceptNode(list1: SingleLinkedList, list2: SingleLinkedList):
    l1 = list1.length()
    l2 = list2.length()

    p1 = list1.head()
    p2 = list2.head()

    i = 0

    if l2 > l1:
        while i < l2 - l1 and p2 is not None:
            p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
    else:
        while i < l1 - l2 and p1 is not None:
            p1 = p1.next

        while p1 != p2 and p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p1


if __name__ == "__main__":
    result = isCircleLinkedList()

    print(result)
