#   at node:
#       if this node is closer to target than `closest`:   # (tie -> keep smaller)
#           closest = node.val
#       if target == node.val: return node.val   # distance 0, can't beat it
#       move left or right by BST rule
#
# n: number of nodes, h: height of tree
# T: O(h) - one root-to-leaf path. O(log n) if balanced, O(n) if skewed
# S: O(h) - recursion stack (O(1) if iterative)

def bst_nearest(node, target):
    closest = node.val
    while node:
        if target == node.val:
            return node.val
        node_dist = abs(node.val - target)
        closest_dist = abs(closest - target)
        if node_dist < closest_dist:
            closest = node.val
        elif node_dist == closest_dist:
            closest = min(closest, node.val)
        node = node.left if target < node.val else node.right
    return closest


# # BST Nearest Value

# A binary search tree (BST) is a binary tree if, for _every_ node:

# - All the values on its **left** subtree are _less than or equal_ to the node's value.
# - All the values on its **right** subtree are _greater than or equal_ to the node's value.

# Given the root of a non-empty binary search tree and a value, `target`, find the closest value to `target` in the tree. In case of a tie, return the smaller value.

# Example 1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
#                  \
#                   9
# target = 4
# Output: 4

# Example 2:
# Same tree, target = 3
# Output: 2

# Constraints:

# - `1 <= number of nodes <= 10^4`
# - `-10^9 <= node.val <= 10^9`
# - `-10^9 <= target <= 10^9`
# - The tree is a valid binary search tree