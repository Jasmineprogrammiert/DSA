# Pure traversal + in-place swap at each node. No info flows needed
#
# n: number of nodes, h: height of tree
# T: O(n) - every node visited once
# S: O(h) - recursion

def invert_binary_tree(node):
    if not node:
        return node
    node.left, node.right = node.right, node.left
    invert_binary_tree(node.left)
    invert_binary_tree(node.right)
    return node


# # Invert a Binary Tree

# Given a binary tree, invert it by modifying the `left` and `right` pointers (do not modify the values in the nodes or create new nodes).

# The left subtree of the root should become the right subtree inverted, and the right subtree of the root should become the left subtree inverted.

# Return the root of the tree after modifying it.

# Example:
#      1
#    /   \
#   6     7
#  / \   /
# 4  11 2
#  \     \
#   5     9

# Output:
#      1
#    /   \
#   7     6
#    \   / \
#     2 11  4
#    /     /
#   9     5

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig13.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - Each node has a value between `0` and `10^9`