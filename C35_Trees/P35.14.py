# - All the values on its **left** subtree <= node.val
# - All the values on its **right** subtree >= node.val

# n: number of nodes; h: height of the tree
# T: O(n) worst case - each node is checked at most once
# S: O(h) - maximum recursion depth; O(n) for a chain

def bst_validation(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True

    if node.val < low or node.val > high:
        return False

    return (bst_validation(node.left, low, node.val) and
            bst_validation(node.right, node.val, high))


# # BST Validation

# A binary search tree (BST) is a binary tree if, for _every_ node:

# - All the values on its **left** subtree are _less than or equal_ to the node's value.
# - All the values on its **right** subtree are _greater than or equal_ to the node's value.

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# Example 1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
#                  \
#                   9
# Output: true

# Example 2:
#               5
#             /    \
#            2      12
#             \    / \
#              4  10  13
#                  \
#                   9
# Output: false

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The value at each node is between `0` and `10^9`