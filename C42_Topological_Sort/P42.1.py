# Problem 42.1 - DAG Distances
# Given the adjacency list of a DAG with edge weights, graph, and a node,
# start, return the distances from start to every other node in an array of
# length V. Element i should be the distance from start to node i. If i
# cannot be reached from start, that element should be infinity. The edge
# weights can be negative.
#
# Example:
# graph = [
#   [[1, 10]],                    # Neighbors of node 0
#   [],                           # Neighbors of node 1
#   [[1, 10]],                    # Neighbors of node 2
#   [[4, 12]],                    # Neighbors of node 3
#   [[1, 11], [2, 21], [5, 14]],  # Neighbors of node 4
#   [[2, -30]]                    # Neighbors of node 5
# ]
# start = 4
# Output: [infinity, -6, -16, infinity, 0, 14]
#
# Constraints:
# - Number of nodes <= 10^5
# - Number of edges <= 10^6
# - Each node is labeled from 0 to V-1
# - Edge weights are integers between -10^4 and 10^4