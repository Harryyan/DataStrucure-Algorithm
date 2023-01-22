# Definition for singly-linked list.

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# leetcode - 19

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # tc: O(n)
    # sc: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        s = 0
        slow = head
        fast = head
        pre = head

        while s < n:
            fast = fast.next
            s += 1

        while fast:
            pre = slow
            fast = fast.next
            slow = slow.next

        pre.next = slow.next

        return head
        
