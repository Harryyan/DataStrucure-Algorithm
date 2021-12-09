# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

class Node:
    pass

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return 
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pre = root
        while pre:
            cur = pre
            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.right and cur.next: cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root
