# Goal: does the BST contain any duplicate values?
#   in-order traversal visits a BST's values in sorted order, so duplicates are adjacent
#   - track `prev`, the previous value seen in-order (global state)
#   - node.val == prev -> duplicate, return True
#   - otherwise update prev and keep walking
#
# n: number of nodes, h: height of tree
# T: O(n) - each node is visited exactly once
# S: O(h) - recursion stack

def bst_duplicate(node):
    prev = None

    def visit(node):
        nonlocal prev
        if not node:
            return False
        if visit(node.left):
            return True
        if node.val == prev:
            return True
        prev = node.val
        return visit(node.right)

    return visit(node)


# # BST Duplicate Detection

# A binary search tree (BST) is a binary tree where, for _every_ node:

# - All the values on its **left** subtree are _less than or equal_ to the node's value.
# - All the values on its **right** subtree are _greater than or equal_ to the node's value.

# Given the root of a binary search tree, determine if it contains any duplicate values.

# Example:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
#                  \
#                   9
# Output: True

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The value at each node is between `0` and `10^9`