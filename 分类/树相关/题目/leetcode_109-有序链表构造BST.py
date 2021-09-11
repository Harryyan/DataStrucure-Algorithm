from Node import TreeNode, ListNode

# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。



# 解题思路：
# 通过快慢指针寻找有序链表中位数的前一个
# 再从中位数切断链表
# 递归
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        preMidNode = self.findPreMid(head)
        midNode = preMidNode.next
        preMidNode.next = None
        
        node = TreeNode(midNode.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(midNode.next)

        return node
    
    
    def findPreMid(self,node: ListNode) -> ListNode:
        pre = s = f = node
        
        while f and f.next:
            pre = s
            s = s.next
            f = f.next.next
        
        return pre        