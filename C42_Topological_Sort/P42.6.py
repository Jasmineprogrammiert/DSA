# Problem 42.6 - Longest Path of Increasing Degrees
# Given the number of nodes and the edge list of an unweighted, undirected
# graph, V and edges, find the longest path where every node has a higher
# degree than the previous one and return its length.
#
# Example:
# V = 8
# edges = [
#   [0, 1], [1, 2], [2, 3], [0, 2], [0, 4], [2, 6],
#   [3, 7], [2, 7], [4, 5], [5, 6], [6, 7]
# ]
# Output: 3
# One longest path with increasing degrees is 5 -> 6 -> 2
# (degrees 2, 3, and 5).
#
# Constraints:
# - Number of nodes <= 10^5
# - Number of edges <= 10^6
# - Each node is labeled from 0 to V-1
# - edges[i].length == 2
