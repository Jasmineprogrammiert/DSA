# Problem 36.1 - Adjacency List Validation
# Given an adjacency list, return whether it is a valid undirected graph:
# - Every node is between 0 and V-1
# - No self-loops
# - No parallel edges
# - If node1 in graph[node2], then node2 in graph[node1]
#
# Example 1: graph = [[1], [0]] -> True
# Example 2: graph = [[2], [0]] -> False (node 2 invalid, only 2 nodes)
# Example 3: graph = [[0], []] -> False (self-loop)
# Example 4: graph = [[1, 1], [0, 0]] -> False (parallel edges)
# Example 5: graph = [[1], []] -> False (asymmetric)
#
# Constraints:
# - graph.length <= 1000
# - graph[i].length <= 1000