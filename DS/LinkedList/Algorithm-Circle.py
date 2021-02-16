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


if __name__ == "__main__":
    result = isCircleLinkedList()

    print(result)
