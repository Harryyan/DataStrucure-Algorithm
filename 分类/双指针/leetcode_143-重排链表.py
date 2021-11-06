# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#  L0 → L1 → … → Ln-1 → Ln 
# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    # 时间复杂度: O(n)
    # 空间复杂度: O(1)
    def reorderList(self, head: ListNode) -> None:
        ##翻转函数
        def reverseList(node: ListNode):
            pre = None
            cur = node
            while cur:
                temp = cur.next   
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        
        #快慢指针找中点
        slow=head
        fast=head

        while fast.next and fast.next.next:
            slow,fast=slow.next,fast.next.next
        
        #右半部分right逆序，左半部分left不动
        reverse_node=slow.next
        right=reverseList(reverse_node)
        slow.next=None
        left=head
        
        #左右两部分逐个拼接
        while right:
            left=left.next
            head.next=right
            head=head.next
            right=right.next
            head.next=left
            head=head.next