import ListNode

# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        current = head
        pre = None

        while current is not None:
            next = current.next
            current.next = pre
            pre = current
            current = next
            
        return pre