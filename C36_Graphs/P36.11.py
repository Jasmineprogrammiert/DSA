# Problem 36.11 - Graph Hangout
# Three friends live at nodes in a connected undirected graph. Return the
# minimum total edges they need to traverse to meet at any single node.
#
# Example 1:
# graph = [[1,4],[0,2],[1,3],[2,4],[0,3]]
# node1 = 0, node2 = 2, node3 = 4 -> 3
#
# Example 2:
# graph = [[1,2,3],[0,2,3],[0,1,3],[0,1,2]]
# node1 = 0, node2 = 1, node3 = 2 -> 2
#
# Constraints:
# - graph.length <= 10^4
# - No parallel edges or self-loops