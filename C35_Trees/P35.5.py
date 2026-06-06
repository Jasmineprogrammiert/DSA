# Tree DFS — 3 info flows:
#   Down   (param):  parent tells child   → e.g. depth, path sum
#   Up     (return): child tells parent   → e.g. subtree size, height
#   Global (state):  across branches      → e.g. max seen, result list
#
#   def visit(node, down_info):
#       if not node:
#           return up_info
#       left  = visit(node.left,  down_info)
#       right = visit(node.right, down_info)
#       global_state = ...          # side effect (across branches)
#       return up_info              # to parent

# For each node as apex, triangles = min(left spine, right spine)
#   Down:   none
#   Up:     (left_spine_len, right_spine_len)
#   Global: res += min(left_spine, right_spine)
#
#   visit(node) -> (left_spine_len, right_spine_len)
#     unpack left child's left spine, right child's right spine
#     res += min(left_spine, right_spine)
#     return (left_spine + 1, right_spine + 1) up to parent
#
# n: number of nodes, h: height of tree
# T: O(n) - each node visited once, spine lengths reused from children
# S: O(h) - recursion

def triangle_count(root):
    res = 0

    def visit(node):
        nonlocal res
        if not node:
            return 0, 0
        left_spine, _ = visit(node.left)
        _, right_spine = visit(node.right)
        res += min(left_spine, right_spine)
        return left_spine + 1, right_spine + 1

    visit(root)
    return res


# # Triangle Count

# Given the root of a binary tree, return the number of _triangles_.
# A triangle is a set of three distinct nodes, `a`, `b`, and `c`, where:

# 1. `a` is the _lowest common ancestor_ of `b` and `c`.
# 2. `b` and `c` have the same depth.
# 3. the path from `a` to `b` only consists of left children (the nodes in the path can have right children).
# 4. the path from `a` to `c` only consists of right children (the nodes in the path can have left children).

# Example 1:
#          0
#      /       \
#     1         2
#      \       / \
#       3     4   5
#      / \   /     \
#     6   7 8       9

# Output: 4.
# The triangles are: (0, 1, 2), (3, 6, 7), (2, 4, 5), (2, 8, 9).

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig12.png

# Example 2:
#       0
#    /      \
#   1        4
#  /  \       \
# 2    3       5
# Output: 3.
# The triangles are: (0, 1, 4), (1, 2, 3), (0, 2, 5).

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The value at each node doesn't matter.