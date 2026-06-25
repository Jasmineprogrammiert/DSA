# Problem 42.4 - Counting Paths
# Given the adjacency list of an unweighted DAG, graph, and a node, start,
# return an array of length V with the number of different paths from start
# to every node.
#
# Example:
# graph = [
#   [1],        # Neighbors of node 0
#   [],         # Neighbors of node 1
#   [1],        # Neighbors of node 2
#   [4],        # Neighbors of node 3
#   [1, 2, 5],  # Neighbors of node 4
#   [2]         # Neighbors of node 5
# ]
# start = 4
# Output: [0, 3, 2, 0, 1, 1]
#
# Constraints:
# - Number of nodes <= 10^5
# - Number of edges <= 10^6
# - Each node is labeled from 0 to V-1