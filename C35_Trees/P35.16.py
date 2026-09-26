# n: number of nodes; h: height of the tree
# T: O(n) worst case - each node is visited at most once
# S: O(h) - the recursion stack follows one root-to-leaf path

def bst_kth(node, k):
    count = 0
    res = None

    def inorder(node):
        nonlocal count, res
        if not node or res is not None:
            return

        inorder(node.left)
        if count == k:
            res = node.val
        count += 1
        inorder(node.right)

    inorder(node)
    return res


# # BST Kth Element

# A binary search tree (BST) is a binary tree where, for _every_ node:

# - All the values on its **left** subtree are _less than or equal_ to the node's value.
# - All the values on its **right** subtree are _greater than or equal_ to the node's value.

# Given the root of a binary search tree with `n` nodes, find the `k`-th smallest element (0-indexed), where `0 ≤ k ≤ n-1`.

# Example 1:
#               5
#             /    \
#            2      9
#             \    / \
#              4  9   11
# k = 4
# Output: 9.

# Example 2:
# Same tree, k = 0
# Output: 2.

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The value at each node is between `0` and `10^9`
# - `0 ≤ k ≤ n-1`