# Given the head of a singly linked list, group all the nodes with odd indices together followed by the 
# nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # tc: O(n)
    # sc: O(1)
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:return head
        odd = head
        even_head = even = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd,even = odd.next,even.next
        odd.next = even_head

        return head