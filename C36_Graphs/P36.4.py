# Traverse from node 0; give each node one parent = where it was first seen
# Skip already-seen nodes (those edges would close a cycle)
# Each non-root node => one edge [parent, node] => V - 1 edges, no cycle
#
# V: number of nodes
# E: number of edges
# T: O(V + E) - visit each node once; sum of all degree = 2E across all neighbor scans
# S: O(V) - predecessors (one parent/node) + recursion depth + V-1 edges

def spanning_tree(graph):
    predecessors = {0: None}

    def visit(node):
        for nbr in graph[node]:
            if nbr not in predecessors:
                predecessors[nbr] = node
                visit(nbr)

    visit(0)
    return [[parent, node] for node, parent in predecessors.items()
            if parent is not None]


# # Spanning Tree

# Given the adjacency list of an undirected, **connected** graph, `graph`, return a set of edges forming a _spanning tree_.

# A spanning tree is a subset of edges that connects (i.e., "spans") every node and has no cycles.

# Example 1:
# graph = [
#   [1],
#   [0, 2, 5],
#   [1, 3, 4],
#   [2],
#   [2, 5],
#   [1, 4]
# ]
# Output: [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5]]
# There are other valid answers

# Example 2:
# graph = [[1], [0]]
# Output: [[0, 1]]
# A single edge is a valid spanning tree for two nodes.

# Example 3:
# graph = [
#   [1, 2],
#   [0, 2],
#   [0, 1]
# ]
# Output: [[0, 1], [0, 2]]
# There are other valid answers, like [[0, 1], [1, 2]].

# Example 4:
# graph = [[]]
# Output: []
# This graph has a single node and no edges.

# Constraints:

# - `1 ≤ graph.length ≤ 1000`
# - `graph[i].length < 1000`
# - `0 ≤ graph[i][j] < graph.length`
# - The adjacency list is properly formatted, with no parallel edges or self-loops
# - The graph is connected