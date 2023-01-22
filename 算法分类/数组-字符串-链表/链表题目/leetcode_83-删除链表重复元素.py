import ListNode

# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素只出现一次.      
# 返回同样按升序排列的结果链表。

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)
        cur = dummy
        
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    if cur.next.next and cur.next.next.val == x:
                        cur.next = cur.next.next
                    else:
                        break
            else:
                cur = cur.next

        return dummy.next