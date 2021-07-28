# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#        1
#       / \
#      0   1
#         / \
#        0   1
#       / \
#      0   0

import binary_tree

# TESTS
def print_btree(btree):

    print(btree.root.data)
root1 = Node(0)
root1.right = 1
root2.left = 0
