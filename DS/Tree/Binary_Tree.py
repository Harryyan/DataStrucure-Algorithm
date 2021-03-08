from Node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

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