import ListNode
from typing import List

class Solution:
    #反转区间[a,b)中的链表元素
    def reverse(self,a,b):
        #pre作为头节点a前的null
        pre,cur = None,a
        while cur != b:           
            nxt = cur.next
            # 逐个结点反转
            cur.next = pre
            #更新指针位置
            pre = cur
            cur =nxt
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:return 
        a,b = head,head
        #区间 [a, b) 包含 k 个待反转元素
        for i in range(k):
            #不足 k 个，不需要反转，递归的base case
            if not b:
                return head
            b = b.next
        #反转前k个元素
        newhead = self.reverse(a,b)
        #递归反转后续链表，并拼接起来
        a.next = self.reverseKGroup(b,k)
        return newhead
