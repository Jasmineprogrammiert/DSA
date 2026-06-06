# Left view = first node at each depth, in BFS (level-order) traversal
# BFS visits depths in order, left-to-right, so the first node popped at a new depth is that depth's answer
# Detector: depth == len(res) — true only for the first node of a new depth
#
# n: number of nodes
# T: O(n) — each node is enqueued and dequeued once
# S: O(n) — the queue can hold up to a full level (~n/2 nodes)

# Level-order (BFS) recipe:
# def level_order(root):
#     Q = Queue()
#     Q.add((root, 0))
#     while not Q.empty():
#         node, depth = Q.pop()
#         if not node:
#             continue
#         # Do something with node and depth
#         Q.add((node.left, depth + 1))
#         Q.add((node.right, depth + 1))

from collections import deque


def left_view(root):
    queue = deque()
    queue.append((root, 0))
    res = []
    while queue:
        node, depth = queue.popleft()
        if not node:
            continue
        if depth == len(res):
            res.append(node.val)
        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))
    return res


# # Left View

# Given the root of a binary tree, return its _left view_. The left view is an array with the value of the first node on each layer, ordered from top to bottom.

# Example:

# Input:
#     1
#    / \
#   2   3
#    \   \
#     5   6
#          \
#           7

# Output: [1, 2, 5, 7]

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig17.png

# Constraints:

# - The number of nodes is at most `10^5`
# - Each node has a value between `0` and `10^9`