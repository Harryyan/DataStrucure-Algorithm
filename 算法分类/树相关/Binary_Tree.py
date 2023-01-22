from Node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def breadth_iterate(self):
        '''广度遍历'''
        if self.root == None:
            return

        queue = [self.root]

        while queue:
            node = queue.pop(0)

            print(node.element, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def preorder_traversal(self, node):
        '''深度-先序遍历'''
        if node is None:
            return

        print(node.element, end=" ")

        left = self.preorder_traversal(node.left)
        right = self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        '''深度-中序遍历'''
        if node is None:
            return

        left = self.inorder_traversal(node.left)
        print(node.element, end=" ")
        right = self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        '''深度-后序遍历'''
        if node is None:
            return
        left = self.postorder_traversal(node.left)
        right = self.postorder_traversal(node.right)

        print(node.element, end=" ")

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]

        while queue:
            current_node = queue.pop(0)

            # left node
            if current_node.left is not None:
                queue.append(current_node.left)
            else:
                current_node.left = node
                break

            # right node
            if current_node.right is not None:
                queue.append(current_node.right)
            else:
                current_node.right = node
                break


tree = BinaryTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)

# tree.breadth_iterate()
tree.depth_iteration_post(tree.root)
