# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

from binary_tree import Node


def count_univals(root):

    count = 0
    if root.left and root.right:
        if root.left.data == root.right.data:
            count += 1
        count += count_univals(root.left)
        count += count_univals(root.right)
    else:
        if root.right is not None:
            count += count_univals(root.right)
        elif root.left is not None:
            count += count_univals(root.left)
        else:
            count += 1

    return count

# TESTS
                        #   Unival subtrees are marked with []

root = Node(0)          #                   0
root.insert(0)          #                 /   \
root.insert(1)          #               0       1
root.insert(0)          #             /  \     /  \
root.insert(0)          #           [0    0]  1    3
root.insert(3)          #          / /   /|   |\    \ \
root.insert(1)          #        [N N] [N N] [N N]  [N N]

print(count_univals(root))       # Should give 5


root = Node(0)  #                           1
root.insert(1)  #                         /   \
root.insert(1)  #                      [1       1]
root.insert(-2) #                     /  \     /  \
root.insert(1)  #                   -2    1  [1     1]
root.insert(1)  #                  / /   /|   |\    \ \
root.insert(1)  #                [N N] [N N] [N N]  [N N]

print(count_univals(root))      # Should give 6
