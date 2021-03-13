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

            print(node.element)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def depth_iteration_pre(self, node):
        '''深度-先序遍历'''
        if node is None:
            return

        print(node.element)

        left = self.depth_iteration_pre(node.left)
        right = self.depth_iteration_pre(node.right)

    def depth_iteration_middle(self, node):
        '''深度-中序遍历'''
        if node is None:
            return
        if node.left is None and node.right is None:
            return node

        left = self.depth_iteration_middle(node.left)
        if left is not None:
            print(left.element)

        print(node.element)

        right = self.depth_iteration_middle(node.right)

        if right is not None:
            print(right.element)

    def depth_iteration_post(self, node):
        '''深度-后序遍历'''
        if node is None:
            return
        if node.left is None and node.right is None:
            return node

        left = self.depth_iteration_post(node.left)
        right = self.depth_iteration_post(node.right)

        if left is not None:
            print(left.element)

        if right is not None:
            print(right.element)

        print(node.element)

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
tree.depth_iteration_pre(tree.root)
