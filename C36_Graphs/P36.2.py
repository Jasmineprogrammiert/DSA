# Problem 36.2 - Graph Path
# Given the adjacency list of an undirected graph and two distinct nodes,
# return a simple path from node1 to node2. Return [] if no path exists.
#
# Example 1:
# graph = [[1],[0,2,5,4],[1,4,5],[],[5,2,1],[1,2,4]]
# node1 = 0, node2 = 4 -> [0, 1, 4]
#
# Example 2: same graph, node1 = 0, node2 = 3 -> []
#
# Example 3:
# graph = [[1],[0,2],[1]], node1 = 0, node2 = 2 -> [0, 1, 2]
#
# Constraints:
# - graph.length <= 1000
# - graph[i].length < 1000
# - No parallel edges or self-loops