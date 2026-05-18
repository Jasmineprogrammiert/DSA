# Problem 36.4 - Spanning Tree
# Given the adjacency list of an undirected, connected graph, return a set
# of edges forming a spanning tree (connects all nodes, no cycles).
#
# Example 1:
# graph = [[1],[0,2,5],[1,3,4],[2],[2,5],[1,4]]
# Output: [[0,1],[1,2],[2,3],[2,4],[4,5]] (other valid answers exist)
#
# Example 2: graph = [[1],[0]] -> [[0,1]]
# Example 3: graph = [[1,2],[0,2],[0,1]] -> [[0,1],[0,2]]
# Example 4: graph = [[]] -> []
#
# Constraints:
# - 1 <= graph.length <= 1000
# - No parallel edges or self-loops
# - Graph is connected