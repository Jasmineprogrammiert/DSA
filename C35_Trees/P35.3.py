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

# Diameter pattern: longest path of aligned nodes (can bend at any node)
#   Down:   depth
#   Up:     longest aligned chain downward (0 if not aligned)
#   Global: res = max(res, left + 1 + right) — path bending here
#
#   visit(node, depth) -> chain_length
#     if aligned: update res with left + 1 + right (bend), return max(left, right) + 1 (chain)
#     else: return 0 (broken)
#
# n: number of nodes, h: height of tree
# T: O(n) - each node visited once
# S: O(h) - recursion

def aligned_path(root):
    res = 0

    def visit(node, depth):
        nonlocal res
        if node is None:
            return 0
        left = visit(node.left, depth + 1)
        right = visit(node.right, depth + 1)
        if node.val == depth:
            res = max(res, left + 1 + right)
            return max(left, right) + 1
        return 0

    visit(root, 0)
    return res

# Alt: mutable list instead of nonlocal
def aligned_path_v2(root):
    res = [0]

    def visit(node, depth):
        if node is None:
            return 0
        left = visit(node.left, depth + 1)
        right = visit(node.right, depth + 1)
        if node.val == depth:
            res[0] = max(res[0], left + 1 + right)
            return max(left, right) + 1
        return 0

    visit(root, 0)
    return res[0]


# # Aligned Path

# Given a binary tree, we say a node is _aligned_ if its value is equal to its depth (distance from root).
# Return the length of the longest path of aligned nodes.
# A path can start and end at any node.

# Example:
#                 7
#                / \
#               1   4
#              / \   \
#             2   8   2
#            / \     / \
#           4   3   3   3

# Output: 3
# The aligned nodes are the circled ones:
# Depth
#   0             7
#                / \
#   1          (1)   4
#              / \   \
#   2        (2)  8  (2)
#            / \     / \
#   3       4  (3) (3) (3)

# There are two paths of aligned nodes with maximum length: 1 -> 2 -> 3 on the left subtree, and 3 -> 2 -> 3 on the right subtree.

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - Each node has a value between `0` and `10^9`