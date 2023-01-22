# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# leetcode - 24

class Solution:
    # tc: O(n)
    # sc: O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None

        dummy = ListNode(-1, head)
        pre = dummy

        while pre.next and pre.next.next:
            slow = pre.next
            fast = pre.next.next
            n = fast.next

            slow.next = n
            fast.next = slow
            pre.next = fast

            pre = slow

        return dummy.next