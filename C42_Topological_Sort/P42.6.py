# Key trick: "increasing degree" gives every edge a natural direction. Orient
# each edge low-degree -> high-degree, and equal-degree edges vanish (they can't 
# extend a strictly-increasing path) -> the result is a DAG. 
# Then it's the familiar longest-path-in-a-DAG, counting nodes instead of edge weights (+1 per hop) since path length here is the node count.
# 
# E: number of edges
# V: number of nodes/vertices
# T: O(V + E) — degrees, orientation, topo sort, and the +1 relaxation each pass once over nodes/edges
# S: O(V + E) — the O(E) is ENTIRELY the oriented `adj` we build: one neighbor entry per edge, ties dropped, so <= E entries across V lists. Every other structure (degrees, in_degrees, degree_zero, topo_order, dist) is a flat O(V) array

from collections import deque


def topological_sort(adj):
    V = len(adj)
    in_degrees = [0] * V
    for node in range(V):
        for nbr in adj[node]:
            in_degrees[nbr] += 1

    degree_zero = deque(node for node in range(V) if in_degrees[node] == 0)

    topo_order = []
    while degree_zero:
        node = degree_zero.popleft()
        topo_order.append(node)
        for nbr in adj[node]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                degree_zero.append(nbr)

    return topo_order

def longest_increasing_degree_path(V, edges):
    # 1. Undirected degree of every node
    degrees = [0] * V
    for node_a, node_b in edges:
        degrees[node_a] += 1
        degrees[node_b] += 1

    # 2. Orient each edge low-degree -> high-degree (ties dropped) -> DAG
    adj = [[] for _ in range(V)]
    for node_a, node_b in edges:
        if degrees[node_a] < degrees[node_b]:
            adj[node_a].append(node_b)
        elif degrees[node_a] > degrees[node_b]:
            adj[node_b].append(node_a)

    # 3. Topological order (Kahn's peel-off) -- Recipe 1
    topo_order = topological_sort(adj)

    # 4. Longest path: each node is its own length-1 path, relax with +1
    dist = [1] * V
    for node in topo_order:
        for nbr in adj[node]:
            dist[nbr] = max(dist[nbr], dist[node] + 1)

    return max(dist)


# # Longest Path Of Increasing Degrees

# Given the number of nodes and the edge list of an **unweighted, undirected** graph, `V` and `edges`, find the longest path where every node has a higher degree than the previous one and return its length.

# Example:
# V = 8
# edges = [
#   [0, 1], [1, 2], [2, 3], [0, 2], [0, 4], [2, 6],
#   [3, 7], [2, 7], [4, 5], [5, 6], [6, 7]
# ]

# Output: 3
# One of the longest paths with increasing degrees is 5 -> 6 -> 2 (degrees 2, 3, and 5). Other longest paths include 1 -> 0 -> 2.

# Here is the graph from the example:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/longest-path-of-increasing-degrees-1.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The number of edges is at most `10^6`
# - Each node is labeled from `0` to `V-1`
# - `edges[i].length == 2`