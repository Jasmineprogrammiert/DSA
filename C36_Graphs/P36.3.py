# Check if the tree is acyclic AND connected. One DFS from node 0.
# predecessors: keys = visited nodes, values = the parent arrived from
#   for each node:
#       for each neighbor:
#           if unvisited:
#               record parent, recurse
#           else if neighbor is not its parent:
#               -> cycle
#   connected when DFS reached every node: len(predecessors) == V
#
# V: number of nodes
# E: number of edges
# T: O(V + E) - each node visited once, each edge seen twice
# S: O(V) - predecessors dict + recursion stack

def tree_check(graph):
    predecessors = {0: None}
    has_cycle = False

    def visit(node):
        nonlocal has_cycle
        for nbr in graph[node]:
            if nbr not in predecessors:
                predecessors[nbr] = node
                visit(nbr)
            elif nbr != predecessors[node]:
                has_cycle = True

    visit(0)
    connected = len(predecessors) == len(graph)
    return not has_cycle and connected


# # Tree Check

# Given a non-empty adjacency list of an undirected graph, `graph`, return whether it is a _tree_. A graph is a tree if it is _acyclic_ and _connected_.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/tree-check-1.png

# Example 1:
# graph = [
#   [2],           # Node 0
#   [2, 5],        # Node 1
#   [0, 1, 3, 4],  # Node 2
#   [2],           # Node 3
#   [2],           # Node 4
#   [1]            # Node 5
# ]
# Output: True
# See left graph in the picture above

# Example 2:
# graph = [
#   [2],           # Node 0
#   [5],           # Node 1
#   [0, 3],        # Node 2
#   [2],           # Node 3
#   [],            # Node 4
#   [1]            # Node 5
# ]
# Output: False
# This graph is not connected
# See center graph in the picture above

# Example 3:
# graph = [
#   [1],           # Node 0
#   [0, 2, 5],     # Node 1
#   [1, 3, 4],     # Node 2
#   [2],           # Node 3
#   [2, 5],        # Node 4
#   [1, 4]         # Node 5
# ]
# Output: False
# This graph is not acyclic
# See right graph in the picture above

# Constraints:

# - `1 ≤ graph.length ≤ 1000`
# - `graph[i].length < 1000`
# - `0 ≤ graph[i][j] < graph.length`
# - The adjacency list is properly formatted, with no parallel edges or self-loops