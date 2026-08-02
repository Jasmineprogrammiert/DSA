# the path can turn at ANY node, not just the root
#
# down(None)  = -1,  down(x) = 1 + max(down(l), down(r))
# through(x)  = down(l) + down(r) + 2
# diameter(x) = max(through(x), diameter(l), diameter(r))
#
# precompute down in ONE post-order pass

# n: nodes
# T: O(n) — down precomputed once, then O(1) per node
# S: O(n) — the down table; call stack is O(h), O(n) when skewed


# # Tree Diameter

# Given the root `root` of a binary tree, find the diameter of the tree. The diameter is the maximum distance between any two nodes.

# Assume that the tree is given as a struct with `val`, `left`, and `right` fields.

# Example 1:

#      a
#     / \
#    b   c
#   /   /
#  d   e
#     / \
#    g   h

# Output: 5. Nodes d and g are at distance 5 (and so are d and h).

# Example 2:

#        a
#      /   \
#     b     c
#   /   \
#  d     e
# /     / \
# f    g   h
#  \   \
#   i   j

# Output: 6. Nodes i and j are the farthest apart.

# Here is a visualization of the examples:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/boosters-fig11.png

# Constraints:

# - `0 <= number of nodes <= 10^4`
# - Node values are unique strings of lowercase English letters of length at most `10`.
# - The tree is a valid binary tree