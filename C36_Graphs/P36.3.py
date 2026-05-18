# Problem 36.3 - Tree Check
# Given a non-empty adjacency list of an undirected graph, return whether
# it is a tree (acyclic and connected).
#
# Example 1:
# graph = [[2],[2,5],[0,1,3,4],[2],[2],[1]] -> True
#
# Example 2:
# graph = [[2],[5],[0,3],[2],[],[1]] -> False (not connected)
#
# Example 3:
# graph = [[1],[0,2,5],[1,3,4],[2],[2,5],[1,4]] -> False (has cycle)
#
# Constraints:
# - 1 <= graph.length <= 1000
# - graph[i].length < 1000
# - No parallel edges or self-loops