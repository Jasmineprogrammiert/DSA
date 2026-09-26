# return the HIGHEST protection level of any node. MIN of any:
    # 1. The number of ancestors
    # 2. The length of the longest chain of descendants
    # 3. The number of nodes on the same level to its left
    # 4. The number of nodes on the same level to its right

# 1. ancestor_count -> BFS  (depth, free)
# 2. longest_chain  -> DFS postorder, carried over in a dict
# 3. left_count     -> BFS  (i)
# 4. right_count    -> BFS  (level_size - 1 - i)

# min_of = min(ancestor_count, chain_below, left_count, right_count)
# best = max(best, min_of)

# n: number of nodes
# T: O(n) - DFS and BFS each visit every node once; dict lookups are O(1) on average
# S: O(n) - heights stores n entries; the queue and DFS call stack use at most O(n) more

from collections import deque

def most_protected_node(root):
    heights = {}

    def height(node):
        if not node:
            return -1
        chain = max(height(node.left), height(node.right)) + 1
        heights[node] = chain
        return chain

    height(root)

    best = 0
    queue = deque([root])
    depth = 0
    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            ancestor_count = depth
            longest_chain = heights[node]
            left_count = i
            right_count = level_size - i - 1
            best = max(best, min(ancestor_count, longest_chain, left_count, right_count))

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    return best


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