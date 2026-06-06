# Goal: does the BST contain `target`?
#   - target == node.val -> found, return True
#   - target <  node.val -> go left  (smaller values live left)
#   - target >  node.val -> go right (larger values live right)
#   - fell off the tree (node is None) -> return False
#
# n: number of nodes, h: height of tree
# T: O(h) - one root-to-leaf path. O(log n) if balanced, O(n) if skewed
# S: O(h) - recursion stack (O(1) if iterative)

def bst_search(node, target):
    if not node:
        return False
    if target == node.val:
        return True
    if target < node.val:
        return bst_search(node.left, target)
    return bst_search(node.right, target)


# # BST Search

# A binary search tree (BST) is a binary tree if, for _every_ node:

# - All the values on its **left** subtree are _less than or equal_ to the node's value.
# - All the values on its **right** subtree are _greater than or equal_ to the node's value.

# Given the root of a binary search tree and a value, `target`, return `true` if the tree contains the target value, and `false` otherwise.

# Example 1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
#                  \
#                   9
# target = 4
# Output: true

# Example 2:
# Same tree, target = 3
# Output: false
# The value 3 does not exist in the tree.

# Constraints:

# - The number of nodes is at most `10^5`
# - The value at each node is between `0` and `10^9`