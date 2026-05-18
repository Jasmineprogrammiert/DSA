# Problem 36.12 - Days Until All Infected
# Given an undirected connected graph and an array of initially infected nodes,
# the virus spreads to all direct neighbors each day. Return how many days
# until all nodes are infected.
#
# Example 1:
# graph = [[1,2],[0,2],[0,1,3],[2]], infected = [0] -> 2
#
# Example 2:
# graph = [[1],[0,2],[1,3],[2,4],[3]], infected = [0,4] -> 2
#
# Example 3:
# graph = [[1,2],[0,3],[0,3],[1,2]], infected = [0,3] -> 1
#
# Constraints:
# - 1 <= graph.length <= 10^4
# - 1 <= infected.length <= graph.length
# - No duplicates in infected
# - Graph is connected