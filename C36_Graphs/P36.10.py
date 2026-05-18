# Problem 36.10 - Shortest-Path Queries
# Given an undirected graph, a start node, and an array of query nodes,
# return an array where each element is the shortest path from start to
# that query node. Return [] if no path exists.
#
# Example 1:
# graph = [[1],[0,2,5,4],[1,4,5],[],[5,2,1],[1,2,4]]
# start = 0, queries = [1,0,3,4]
# Output: [[0,1],[0],[],[0,1,4]]
#
# Example 2:
# graph = [[1],[0,2],[1]], start = 0, queries = [1,2]
# Output: [[0,1],[0,1,2]]
#
# Example 3:
# graph = [[1],[0],[3],[2]], start = 0, queries = [1,2,3]
# Output: [[0,1],[],[]]
#
# Constraints:
# - graph.length <= 10^4
# - queries.length <= 10^3
# - No parallel edges or self-loops