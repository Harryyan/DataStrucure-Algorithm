from Node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymetric(self, root):
        if not root: return False
        if not root.left and not root.right: return True
        if not root.left or not root.right: return False
        if root.left.val != root.right.val: return False
        
        self.recursive(root.left, root.right)
        
        
    def recursive(self, left, right) -> bool:
        if not left and not right: return True
        if not left or not right: return False
        if left.val != right.val: return False
        
        self.recursive(left.left, right.right) and self.recursive(left.right, right.left)
    
    def isSymmetric_loop(self, root):
        ret = True
        
        if not root.left and not root.right:
            return ret
        
        if not root.left or not root.right:
            return False

        if root.left.val != root.right.val:
            return False
        
        queue = [root.left, root.right]
        while queue:
            a = queue.pop(0)
            b = queue.pop(0)
            
            if not a and not b:
                continue
            
            if not a or not b:
                ret = False
                break
            
            l1 = a.left
            r1 = b.right
            l2 = b.left
            r2 = a.right
            
            if l1 and r1 and l1.val == r1.val:
                queue.append(l1)
                queue.append(r1)
            elif not l1 and not r1: pass
            else:
                ret = False
                break
            
            if l2 and r2 and l2.val == r2.val:
                queue.append(l2)
                queue.append(r2)
            elif not l2 and not r2: pass
            else:
                ret = False
                break

        return ret