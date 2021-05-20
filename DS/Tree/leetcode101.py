from Node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = True

    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        
        self.test1(queue)

        return self.result
        
    def test1(self, items: list):
        if all(x is None for x in items):
            return

        queue = []

        for item in items:
            l = item.left if item else None
            r = item.right if item else None
            
            queue.append(l)
            queue.append(r)  
        
        test = []
        
        for i in range(0,len(queue)):
            test.append(queue[i].val if queue[i] else 0)
        
        for i in range(0, len(test)):
            if test[i] != test[len(test)-1-i]:
                self.result = False
                break
            
        if self.result:
            self.test1(queue)
        
        
        
    
node_3 = TreeNode(3, None, None)
node_33 = TreeNode(3, None, None)
node_4 = TreeNode(4, None, None)
node_44 = TreeNode(4, None, None)

node_2 = TreeNode(2, node_3, node_4)
node_22 = TreeNode(2, node_44, node_33)
node_1 = TreeNode(1, node_2, node_22)

test = Solution()

a = [None] * 10

print(a is None)


