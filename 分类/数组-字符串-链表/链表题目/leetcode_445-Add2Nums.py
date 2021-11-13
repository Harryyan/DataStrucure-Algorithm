# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# leetcode 445
# 使用栈实现不翻转原链表 - follow up
class Solution:
    # tc: O(n) 
    # sc: O(n)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_l1 = self.stack(l1)
        stack_l2 = self.stack(l2)

        # dummy head
        new_head = ListNode(-1)
        # 进位
        carry = 0

        while not stack_l1 or not stack_l2 or carry != 0:
            x = stack_l1.pop() if stack_l1 else 0
            y = stack_l2.pop() if stack_l2 else 0

            sum = x + y + carry

            node = ListNode(sum % 10)
            node.next = new_head.next
            new_head.next = node

            # 取整
            carry = sum // 10

        return new_head.next

    def stack(self, node: ListNode) -> List:
        stack = []
        n = node

        while not n:
            stack.append(n.val)
            n = n.next

        return stack