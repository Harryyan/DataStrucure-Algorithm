from queue import Queue
from typing import Deque, List

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
# 这种方法空间复杂度不是O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q=Deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(q)>1:
                for j in range(len(q)):#这里是层次遍历的结果，每一个都创造一个next指针指向下一个节点
                    q[j].next=q[j+1]
                    
        return root
    
# 常量级空间复杂度
# 重点在于 双层循环，cur指针比那里parent层，pre指针遍历children层;
class Solution2:
    def connect(self, root):
        if not root:
            return None
        cur = root
        while cur:
            dummyHead = Node(-1)    #为下一行的之前的节点，相当于下一行所有节点链表的头结点；
            pre = dummyHead
            while cur:
                if cur.left:        #链接下一行的节点
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dummyHead.next    #此处为换行操作，更新到下一行
        return root