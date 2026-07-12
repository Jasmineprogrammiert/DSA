# TEMPLATE 1 PEEL-OFF ALGO
from collections import deque

# def topological_sort(graph):
#     # I. Build the in-degree array
#     V = len(graph)
#     in_degrees = [0] * V
#     for node in range(V):
#         for nbr in graph[node]:  # For weighted graphs, unpack edges: nbr, _
#             in_degrees[nbr] += 1

#     # II. Seed the queue with the "ready" nodes
#     degree_zero = deque(node for node in range(V) if in_degrees[node] == 0)

#     # III. The peel-off loop
#     # 1. Take a ready node and commit it to the output
#     # 2. 'Remove' it from the graph - since it's now done, each neighbor loses one prerequisite, so decrement in_degrees[nbr]
#     # 3. Promote any neighbor whose count just hit 0 - it has no remaining prerequisites, so it's now ready. Add it to the queue
#     topo_order = []
#     while degree_zero:
#         node = degree_zero.popleft()
#         topo_order.append(node)
#         for nbr in graph[node]:  # For weighted graphs, unpack edges: nbr, _
#             in_degrees[nbr] -= 1
#             if in_degrees[nbr] == 0:
#                 degree_zero.append(nbr)

#     # IV. Cycle detection
#     if len(topo_order) < V:
#         return []
#     return topo_order
#     # DAG → every node reaches in-degree 0, so topo_order holds all V. A cycle's nodes keep each other's counts above 0 forever, so they're never queued or output. That shortfall (len(topo_order) < V) signals the cycle → return []

# TEMPLATE 2 DAG ALGO
# # compute a topological ordering (Khan's peel-off algorithm)
# for node in topological ordering
#   for each edge node -> nbr
#     update some information about nbr


# E: number of edges
# V: number of nodes/vertices
# T: O(V + E) — topological_sort visits each node and edge once; the relaxation pass does the same → O(V + E)
# S: O(V) — in_degrees, degree_zero, topo_order (in the helper) and dist are each O(V) (input adjacency list not counted)

def topological_sort(graph):
    V = len(graph)
    in_degrees = [0] * V
    for node in range(V):
        for nbr, _ in graph[node]:
            in_degrees[nbr] += 1

    degree_zero = deque(node for node in range(V) if in_degrees[node] == 0)

    topo_order = []
    while degree_zero:
        node = degree_zero.popleft()
        topo_order.append(node)
        for nbr, _ in graph[node]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                degree_zero.append(nbr)

    if len(topo_order) < V:
        return []
    return topo_order

def dag_distances(graph, start):
    V = len(graph)
    topo_order = topological_sort(graph)

    INF = float("inf")
    dist = [INF] * V
    dist[start] = 0
    for node in topo_order:
        if dist[node] == INF:
            continue
        for nbr, w in graph[node]:
            dist[nbr] = min(dist[nbr], dist[node] + w)

    return dist


# # DAG Distances

# Given the adjacency list of a DAG (Directed Acyclic Graph) with edge weights, `graph`, and a node, `start`, return the distances from `start` to every other node in an array of length `V` (the number of nodes). Element `i` should be the distance from `start` to node `i`. If `i` cannot be reached from `start`, that element should be `infinity`. The edge weights can be negative.

# Example:
# graph = [
#   [[1, 10]],                    # Neighbors of node 0
#   [],                           # Neighbors of node 1
#   [[1, 10]],                    # Neighbors of node 2
#   [[4, 12]],                    # Neighbors of node 3
#   [[1, 11], [2, 21], [5, 14]],  # Neighbors of node 4
#   [[2, -30]]                    # Neighbors of node 5
# ]
# start = 4

# Output: [infinity, -6, -16, infinity, 0, 14]
# Nodes 0 and 3 are unreachable from node 4.
# Node 4 is at distance 0 from itself.
# The shortest path from node 4 to node 1 is 4 -> 5 -> 2 -> 1.

# Here is the DAG from the example:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/dag-distances-1.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The number of edges is at most `10^6`
# - Each node is labeled from `0` to `V-1`
# - The edge weights are integers between `-10^4` and `10^4`