# even: left -> right
# odd: right -> left

# n: number of nodes
# T: O(n) - each node is enqueued and dequeued once; the reverses sum to n across all rows
# S: O(n) - res is the output; auxiliary is the queue, one level at a time, up to n / 2

from collections import deque

def zig_zag_order(root):
    res = []
    queue = deque([root]) if root else deque()
    depth = 0
    while queue:
        level_size = len(queue)
        row = []
        for _ in range(level_size):
            node = queue.popleft()
            row.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.extend(reversed(row) if depth % 2 == 1 else row)
        depth += 1
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