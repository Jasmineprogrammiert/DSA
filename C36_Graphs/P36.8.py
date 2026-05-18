# Problem 36.8 - Highest Average Elevation Gain
# Given V > 0 nodes and an array of edges [node1, node2, elevation_gain],
# find the connected component with highest average edge elevation gain.
#
# Example 1: V = 4, edges = [[0,1,3],[1,2,2],[2,3,1],[3,0,2]] -> 2.0
# Example 2: V = 2, edges = [[0,1,5]] -> 5.0
# Example 3: V = 6, edges = [[0,1,1],[1,2,2],[3,4,3],[4,5,5]] -> 4.0
#
# Constraints:
# - 1 <= V <= 1000
# - edges.length <= 10^6
# - No parallel edges or self-loops
# - Output within 6 decimal places of precision