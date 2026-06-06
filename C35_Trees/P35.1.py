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

# Aligned = node.val == depth. Find longest descendant chain of aligned nodes.
#   Down:   depth
#   Up:     aligned chain length extending down from this node (0 if not aligned)
#   Global: res = max(res, chain length)
#
#   visit(node, depth) -> chain_length
#     if aligned: chain = 1 + max(left, right), update res
#     else: chain = 0 (broken)
#     return chain up to parent
#
# n: number of nodes, h: height of tree
# T: O(n) - each node visited once
# S: O(h) - recursion

def aligned_chain(root):
    res = 0

    def visit(node, depth):
        nonlocal res
        if not node:
            return 0
        left = visit(node.left, depth + 1)
        right = visit(node.right, depth + 1)
        if node.val == depth:
            chain = 1 + max(left, right)
            res = max(res, chain)
            return chain
        return 0

    visit(root, 0)
    return res

# Alt: streak passed down, max flows up (no nonlocal)
# T: O(n)  S: O(h)
def aligned_chain_v2(node, depth=0, streak=0):
    if node is None:
        return 0
    streak = streak + 1 if node.val == depth else 0
    left = aligned_chain_v2(node.left, depth + 1, streak)
    right = aligned_chain_v2(node.right, depth + 1, streak)
    return max(streak, left, right)


# # Aligned Chain

# Given a binary tree, we say a node is _aligned_ if its value is equal to its depth (distance from root).
# A _descendant chain_ is a sequence of nodes where each node is the parent of the next node.
# Return the length of the longest descendant chain of aligned nodes. The chain does not need to start at the root.

# Example:
#                 7
#                / \
#               1   3
#              / \   \
#             2   8   2
#            / \     / \
#           4   3   3   3

# Output: 3
# The aligned nodes are the circled ones:
# Depth
#   0             7
#                / \
#   1          (1)   3
#              / \   \
#   2        (2)  8  (2)
#            / \     / \
#   3       4  (3) (3) (3)

# The longest descendant chain of aligned nodes is 1 -> 2 -> 3 on the left subtree.

# Here is a drawing of the same example:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig9.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - Each node has a value between `0` and `10^9`