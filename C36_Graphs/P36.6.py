# Problem 36.6 - Strongly Connected Graph
# Given the adjacency list of a non-empty directed graph, return whether
# it is strongly connected (every node can reach every other node).
#
# Example 1:
# graph = [[1,3],[2],[0],[2]] -> True
#
# Example 2:
# graph = [[1,2,3],[2],[],[2]] -> False (node 2 can't reach node 0)
#
# Example 3:
# graph = [[1],[0],[3],[2]] -> False (node 0 can't reach node 3)
#
# Constraints:
# - 1 <= graph.length <= 1000
# - graph[i].length < 1000
# - No parallel edges or self-loops
# - Directed graph