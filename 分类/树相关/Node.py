class Node:
    def __init__(self, item):
        self.element = item
        self.left = None
        self.right = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next