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

# Count max nodes at same (r, c). left: r+1, right: c+1
#   Down:   r, c (grid position)
#   Up:     none
#   Global: counts[(r, c)] += 1
#
#   visit(node, r, c):
#     increment counts[(r, c)]
#     recurse left with r+1, right with c+1
#
# n: number of nodes, h: height of tree
# T: O(n) - every node visited once
# S: O(n) - counts stores up to n entries + O(h) recursion

def max_stacked(root):
    counts = {}

    def visit(node, r, c):
        if node is None:
            return
        counts[(r, c)] = counts.get((r, c), 0) + 1
        visit(node.left, r + 1, c)
        visit(node.right, r, c + 1)

    visit(root, 0, 0)
    return max(counts.values())

# Alt: BFS level-by-level. r + c = depth, so c alone determines position per level
#   - process one level at a time, discard counts before next level
#
# T: O(n)
# S: O(w) - only store counts for one level at a time

from collections import deque


def max_stacked_v2(root):
    max_count = 1
    queue = deque([(root, 0)])

    while queue:
        level_counts = {}
        for _ in range(len(queue)):
            node, c = queue.popleft()
            level_counts[c] = level_counts.get(c, 0) + 1
            if node.left:
                queue.append((node.left, c))
            if node.right:
                queue.append((node.right, c + 1))
        max_count = max(max_count, max(level_counts.values()))

    return max_count


# # Tree Layout

# You are given the root of a non-empty binary tree. We lay out the tree on a grid as follows:

# 1. We put the root at `(r, c) = (0, 0)`
# 2. We recursively lay out the left subtree one unit below the root (increasing `r` by one)
# 3. We recursively lay out the right subtree one unit to the root's right (increasing `c` by one)

# For instance, the left child of the root goes on `(1, 0)` and the right child goes on `(0, 1)`.

# Two nodes are _stacked_ if they are laid on the same `(r, c)` coordinates. For instance, `root.left.right` and `root.right.left` would overlap at `(1, 1)`.

# Return the maximum number of nodes stacked on the same coordinate.

# Example:

# Input:
#          1
#        /   \
#      2       3
#    /  \     /
#   4    5   6
#    \      / \
#     7    8   9

# Output: 2
# The layout looks like this:

# 1 -- 3
# |    |
# 2 - 5,6 - 9
# |    |
# 4 - 7,8

# The most stacked nodes are 5,6 or 7,8.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig11.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The value at each node doesn't matter.