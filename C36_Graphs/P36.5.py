# Problem 36.5 - Reachability Queries
# Given an undirected graph and an array of queries (pairs of node indices),
# return a boolean array where each element indicates if the two nodes are
# in the same connected component.
#
# Example 1:
# graph = [[1],[0,2,5,4],[1,4,5],[],[5,2,1],[1,2,4]]
# queries = [[0,4],[0,3]] -> [True, False]
#
# Example 2:
# graph = [[1],[0,2],[1]]
# queries = [[0,2],[0,1]] -> [True, True]
#
# Example 3:
# graph = [[1],[0],[3],[2]]
# queries = [[0,1],[0,2],[2,3]] -> [True, False, True]
#
# Constraints:
# - graph.length <= 1000
# - queries.length <= 1000
# - No parallel edges or self-loops