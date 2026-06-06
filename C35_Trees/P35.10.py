# Zig-zag order = level-order, but flip every odd level left-to-right -> right-to-left
# 1. BFS one full level at a time (for _ in range(len(queue))), so each while pass = one level
# 2. Collect that level's values into `level`
# 3. Keep a `flipped` flag; reverse `level` before extending res on flipped levels, then toggle it
# 4. Return res
#
# n: number of nodes
# T: O(n) — each node is enqueued/dequeued once; reversing each level sums to O(n) overall
# S: O(n) — the queue holds up to a full level (~n/2 nodes)

# Level-by-level (BFS) recipe:
# from collections import deque
# def level_order(root):
#     queue = deque()
#     queue.append((root, 0))
#     while queue:
#         level_size = len(queue)     # queue == exactly one level
#         for _ in range(level_size): # peel off that whole level
#             node, depth = queue.popleft()
#             # Do something with node and depth
#             if node.left:
#                 queue.append((node.left, depth + 1))
#             if node.right:
#                 queue.append((node.right, depth + 1))
#         # Do something with the WHOLE level (size = level_size)

from collections import deque


def zig_zag_order(root):
    if not root:
        return []
    queue = deque()
    queue.append(root)
    res = []
    flipped = False
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.extend(reversed(level) if flipped else level)
        flipped = not flipped
    return res


# # Zig-Zag Order

# Given a binary tree, return the values of all its nodes in _zig-zag order_. This is similar to a level-order traversal but alternating the direction of the nodes at each level. Nodes at even depth are ordered left to right, and nodes at odd depth are ordered right to left.

# Example:

# Input:
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6

# Output: [1, 3, 2, 4, 5, 6]

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig19.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The values at each node are between `0` and `10^9`