# Connected components + per-component average (DFS/BFS)
# seen = set of visited nodes
# best = 0.0
# for each node not in seen:
#     DFS/BFS its whole component, accumulating:
#         total_gain += |height[u] - height[v]| per neighbor encounter
#         edge_count += 1 per neighbor encounter
#     hilliness_C = total_gain / edge_count if edge_count > 0 else 0.0
#     best = max(best, hilliness_C)
# return best
#
# V: number of nodes
# E: number of edges
# T: O(V + E) - each node visited once; each edge scanned twice
# S: O(V) - seen set + recursion/stack

def hilliest(graph, heights):
    V = len(graph)
    seen = set()
    total_gain = 0
    edge_count = 0

    def visit(node):
        nonlocal total_gain, edge_count
        seen.add(node)
        for nbr in graph[node]:
            total_gain += abs(heights[node] - heights[nbr])
            edge_count += 1
            if nbr not in seen:
                visit(nbr)

    best = 0.0
    for node in range(V):
        if node not in seen:
            total_gain = 0
            edge_count = 0
            visit(node)
            hilliness_C = total_gain / edge_count if edge_count > 0 else 0.0
            best = max(best, hilliness_C)

    return best


# # Hilliest Connected Component

# We're given the adjacency list, `graph`, of a non-empty, undirected graph with `V` nodes and an array, `heights`, of length `V`, where `heights[i]` is a floating-point number representing the _height_ of node `i`.

# A _connected component_ is a maximal set of nodes such that there is a path between any two nodes in the set.

# The _elevation gain_ of an edge is the absolute difference of the heights of its endpoints. The _hilliness_ of a connected component is the average elevation gain of the edges in it, or `0` if it has a single node. The _hilliest_ connected component is the one with maximum hilliness.

# Find the hilliest connected component and return its hilliness.

# Example 1:
# graph = [
#    [1, 3],       # Node 0
#    [0, 2],       # Node 1
#    [1, 3],       # Node 2
#    [0, 2]        # Node 3
# ]
# heights = [4.0, 1.0, 3.0, 2.0]

# Output: 2.0
# The graph has a single connected component
# The edge elevation gains are:
# - |4 - 1| = 3 for [0, 1]
# - |1 - 3| = 2 for [1, 2]
# - |3 - 2| = 1 for [2, 3]
# - |2 - 4| = 2 for [3, 0]
# The average is 2

# Example 2:
# graph = [
#    []           # Node 0
# ]
# heights = [5.0]

# Output: 0.0
# A single-node connected component has hilliness 0

# Example 3:
# graph = [
#    [1],          # Node 0
#    [0],          # Node 1
#    [3],          # Node 2
#    [2]           # Node 3
# ]
# heights = [1.5, 5.5, 0.0, 5.0]

# Output: 5.0
# The graph has two components:
# - {0, 1}, with a single edge with elevation gain 4.0
# - {2, 3}, with a single edge with elevation gain 5.0

# Example 4:
# graph = [
#    [1, 2],       # Node 0
#    [0, 2],       # Node 1
#    [0, 1]        # Node 2
# ]
# heights = [3.0, 3.0, 3.0]
# Output: 0.0
# When all nodes have the same height, the elevation gain is 0 for all edges

# Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/hilliest-connected-component-1.png

# Constraints:

# - `1 ≤ graph.length ≤ 1000`
# - `graph[i].length < 1000`
# - `0 ≤ graph[i][j] < graph.length`
# - The adjacency list is properly formatted, with no parallel edges or self-loops
# - `heights.length = graph.length`
# - `0 ≤ heights[i] < 10^9`
# - `heights[i]` is a floating-point number