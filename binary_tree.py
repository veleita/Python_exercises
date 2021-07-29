class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_data(self):
        print(self.data)

    def print_tree(self):               # left -> self -> right
        if self.left:
            self.left.print_tree()
        self.print_data()
        if self.right:
            self.right.print_tree()

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def inorder_traversal(self, root: Node):      # [left -> root -> right]

        data = []
        if root:
            data = self.inorder_traversal(root.left)
            data.append(root.data)
            data += self.inorder_traversal(root.right)

        return data

    def preorder_traversal(self, root: Node):      # [root -> left -> right]

        data = []
        if root:
            data.append(root.data)
            data += self.inorder_traversal(root.left)
            data += self.inorder_traversal(root.right)

        return data

    def postorder_traversal(self, root:Node):      # [left -> right -> root]

        data = []
        if root:
            data = self.inorder_traversal(root.left)
            data += self.inorder_traversal(root.right)
            data.append(root.data)

        return data

    def find_value(self, value, node=None):

        if not node:
            node = self.root

        if value < node.data:
            if node.left:
                return self.find_value(value, node.left)
            else:
                return str(value) + " not found"
        elif value > node.data:
            if node.right:
                return self.find_value(value, node.right)
            else:
                return str(value) + " not found"
        else:
            return str(value) + " found"

# TESTS
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.print_tree()
#
# tree = BinaryTree(root)
# print(tree.inorder_traversal(tree.root))
# print(tree.preorder_traversal(tree.root))
# print(tree.postorder_traversal(tree.root))

# print(tree.find_value(13))

