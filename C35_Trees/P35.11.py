# Level-by-level Recipe for Level-Order Traversal (BFS)
#   def level_order(root):
#       queue = deque()
#       queue.append((root, 0))
#       while queue:
#           level_size = len(queue)     # queue == exactly one level
#           for _ in range(level_size): # peel off that whole level
#               node, depth = queue.popleft()
#               # Do something with node and depth
#               if node.left:
#                   queue.append((node.left, depth + 1))
#               if node.right:
#                   queue.append((node.right, depth + 1))
#           # Do something with the WHOLE level (size = level_size)

# input: root
# return: max(protection_level) of any node.
# protection_level = min of:
#   1. number of ancestors       = depth             -> down info
#   2. longest descendant chain  = max(left,right)+1 -> up info
#   3. nodes to left (same level)                    -> BFS
#   4. nodes to right (same level)                   -> BFS
#
# n: number of nodes
# T: O(n) -- DFS visits each node once, BFS visits each node once, lookups O(1)
# S: O(n) -- heights dict holds all n nodes; queue holds up to one full level (~n/2)

from collections import deque


def most_protected_node(root):
    # Pass 1 -- DFS (post-order): record each node's longest descendant chain
    heights = {}

    def height(node):
        if not node:
            return -1
        chain = max(height(node.left), height(node.right)) + 1
        heights[node] = chain
        return chain

    height(root)

    # Pass 2 -- BFS (level by level): combine the four values, keep the best
    queue = deque([(root, 0)])
    max_prot = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node, depth = queue.popleft()

            ancestors = depth
            desc_chain = heights[node]
            l_nodes = i
            r_nodes = level_size - 1 - i
            prot = min(ancestors, desc_chain, l_nodes, r_nodes)
            max_prot = max(max_prot, prot)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    return max_prot


# # Most Protected Node

# Given the root of a non-empty binary tree, return the highest protection level of any node. The _protection level_ of a node is the minimum of four values:

# 1. The number of ancestors
# 2. The length of the longest chain of descendants
# 3. The number of nodes on the same level to its left
# 4. The number of nodes on the same level to its right

# Example:
#             O
#          /     \
#         O       O
#        / \     / \
#       O   O   O   O
#      / \   \   \   \
#     O   O   O   O   O
#    / \   \   \   \   \
#   O   O   O   O   O   O
#  /   / \     / \   \   \
# O   O   O   O   O   O   O

# Output: 2.
# The protection level of each node is:
#             0
#          /     \
#         0       0
#        / \     / \
#       0   1   1   0
#      / \   \   \   \
#     0   1   2   1   0
#    / \   \   \   \   \
#   0   1   0   1   1   0
#  /   / \     / \   \   \
# 0   0   0   0   0   0   0

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/trees_fig20.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The height of the tree is at most `500`
# - The value at each node doesn't matter.