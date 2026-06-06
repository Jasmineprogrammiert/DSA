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