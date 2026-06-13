# Connected components + per-component average (DFS)
# build adjacency list from weighted edge triplets (undirected)
# visited = set of visited nodes
# best = 0.0
# for each node not in visited:
#     DFS its whole component, accumulating:
#         total_gain += gain per neighbor encounter
#         edge_count += 1 per neighbor encounter
#     (each edge counted twice, so 2*sum / 2*count = sum/count)
#     best = max(best, total_gain / edge_count) if edge_count > 0
# return best
#
# V: number of nodes
# E: number of edges
# T: O(V + E) - each node visited once; each edge scanned twice
# S: O(V + E) - adjacency list + visited set + recursion stack

def highest_ave_elevation_gain(V, edges):
    # 1. build the graph
    graph = [[] for _ in range(V)]
    for node1, node2, gain in edges:
        graph[node1].append((node2, gain))
        graph[node2].append((node1, gain))

    # 2. flood-fill a component, accumulating its totals
    visited = set()

    def visit(node):
        nonlocal total_gain, edge_count
        visited.add(node)
        for nbr, gain in graph[node]:
            total_gain += gain
            edge_count += 1
            if nbr not in visited:
                visit(nbr)

    # 3. for each component, compute its average, keep the best
    best = 0.0
    for node in range(V):
        if node not in visited:
            total_gain = 0
            edge_count = 0
            visit(node)
            if edge_count > 0:
                best = max(best, total_gain / edge_count)

    return best


# # Highest Average Elevation Gain

# You are given `V > 0`, the number of nodes in a graph, and an array, `edges`, where `edges[i]` is a triplet `[node1, node2, elevation_gain]` representing an edge and an associated elevation gain.

# Find the connected component with the highest average edge elevation gain and return that average as a floating-point number.

# Example 1:
# V = 4,
# edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 0, 2]]

# Output: 2.0
# The graph is a single connected component
# Its average elevation gain is (3 + 2 + 1 + 2) / 4 = 2.0

# Example 2:
# V = 2
# edges = [[0, 1, 5]]

# Output: 5.0
# There is a single edge

# Example 3:
# V = 6
# edges = [[0, 1, 1], [1, 2, 2], [3, 4, 3], [4, 5, 5]]

# Output: 4.0
# The graph has 2 connected components:
# - {0, 1, 2} with average gain (1 + 2)/2 = 1.5
# - {3, 4, 5} with average gain (3 + 5)/2 = 4.0

# Constraints:

# - `1 ≤ V ≤ 1000`
# - `edges.length ≤ 10^6`
# - `0 ≤ edges[i][0], edges[i][1] < V`
# - `edges[i][0] != edges[i][1]`
# - `0 ≤ edges[i][2] ≤ 10^9`
# - `edges[i][2]` is an integer
# - The graph is well-formed, with no parallel edges or self-loops
# - The output should be within 6 decimal places of precision