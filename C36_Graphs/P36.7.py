# Problem 36.7 - Hilliest Connected Component
# Given an undirected graph and an array of heights (floats) per node,
# find the hilliest connected component and return its hilliness.
# Elevation gain of an edge = abs difference of endpoint heights.
# Hilliness = average elevation gain of edges in the component (0 if single node).
#
# Example 1:
# graph = [[1,3],[0,2],[1,3],[0,2]], heights = [4.0,1.0,3.0,2.0] -> 2.0
#
# Example 2:
# graph = [[]], heights = [5.0] -> 0.0
#
# Example 3:
# graph = [[1],[0],[3],[2]], heights = [1.5,5.5,0.0,5.0] -> 5.0
#
# Example 4:
# graph = [[1,2],[0,2],[0,1]], heights = [3.0,3.0,3.0] -> 0.0
#
# Constraints:
# - 1 <= graph.length <= 1000
# - heights.length = graph.length
# - 0 <= heights[i] < 10^9