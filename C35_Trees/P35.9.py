# Prolificness of a level = total children / number of nodes on that level
# 1. Empty tree -> return -1
# 2. BFS level by level; per level count its nodes and their children
# 3. prolificness = children / level_size; if it beats the best, record this level
# 4. Return the best level
#
# n: number of nodes
# T: O(n) - each node enqueued/dequeued once
# S: O(n) - queue holds at most one full level (up to ~n/2 nodes)

# Level-by-level (BFS) recipe:
# def level_order(root):
#     queue = deque()
#     queue.append((root, 0))
#     while queue:
#         level_size = len(queue)
#         for _ in range(level_size):
#             node, depth = queue.popleft()
#             # Do something with node and depth
#             if node.left:
#                 queue.append((node.left, depth + 1))
#             if node.right:
#                 queue.append((node.right, depth + 1))
#         # Do something with the whole level (size = level_size)

from collections import deque


def most_prolific_level(root):
    if not root:
        return -1
    queue = deque()
    queue.append((root, 0))
    max_prolificness = -1
    res = 0
    while queue:
        level_size = len(queue)
        children = 0
        for _ in range(level_size):
            node, depth = queue.popleft()
            if node.left:
                children += 1
                queue.append((node.left, depth + 1))
            if node.right:
                children += 1
                queue.append((node.right, depth + 1))
        prolificness = children / level_size
        if prolificness > max_prolificness:
            max_prolificness = prolificness
            res = depth
    return res


# # Most Prolific Level

# Given the root of a binary tree, return the most prolific level. The _prolificness_ of a level is the average number of children over all the nodes in that level.

# Return `-1` if the tree is empty. In case of a tie, return any of the most prolific levels.

# Example:

# Input:
#       O
#      /
#     O
#    / \
#   O   O
#  / \   \
# O   O   O

# Output: 1
# - Level 0 has prolificness 1
# - Level 1 has prolificness 2
# - Level 2 has prolificness 1.5
# - Level 3 has prolificness 0
# The most prolific level is 1, with a prolificness of 2.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig18.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The value at each node doesn't matter.