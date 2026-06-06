# # Unrooted Tree Diameter

# Given the number of nodes `n > 0` and the edge list `edges` of an undirected graph that forms a tree (meaning it is connected and has no cycles), find the tree's diameter. The diameter is the maximum distance between any two nodes.

# Example: n = 8
# edges = [[0, 3], [2, 3], [1, 3], [4, 1], [1, 5], [1, 7], [7, 6]]
# Output: 4. Nodes 2 and 6 are at distance 4 (and so are 0 and 6).

# Constraints:

# - `1 <= n <= 10^4` (number of nodes)
# - `edges.length == n - 1` (tree has exactly n-1 edges)
# - `0 <= edges[i][0], edges[i][1] < n` (valid node indices)
# - The edges form a connected tree (no cycles)