# Shortest path on a DAG = 3 reusable ideas (don't trace, just trust the invariants):
# 1. Topo order  -> a safe schedule: process a node only after everything pointing into it is done
# 2. Relax (improve) -> "can I reach nbr cheaper via node?" if so, update dist[nbr] AND parent[nbr] = node
# 3. Reconstruct -> walk parent pointers backward from goal, then reverse (parent[start] = -1 stops it)
# 
# E: number of edges    
# V: number of nodes/vertices
# T: O(V + E) — topo sort and relaxation each touch every node/edge once; reconstruction walks <= V parents
# S: O(V) — in_degrees, degree_zero, topo_order, dist, parent, path are each O(V) (input adjacency list not counted)

from collections import deque


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

def _build_path(parent, goal):
    path = []
    node = goal
    while node != -1:
        path.append(node)
        node = parent[node] # take one step backward
    path.reverse()
    return path

def dag_shortest_path(graph, start, goal):
    V = len(graph)
    topo_order = topological_sort(graph)

    INF = float("inf")
    dist = [INF] * V
    parent = [-1] * V
    dist[start] = 0
    for node in topo_order:
        if node == goal:
            break
        if dist[node] == INF:
            continue
        for nbr, w in graph[node]:
            if dist[node] + w < dist[nbr]:
                dist[nbr] = dist[node] + w
                parent[nbr] = node

    if dist[goal] == INF:
        return []
    return _build_path(parent, goal)


# # DAG Path Reconstruction

# Given the adjacency list of a DAG with edge weights, `graph`, and a pair of nodes, `start` and `goal`, return the shortest path from `start` to `goal`, or an empty array if `goal` cannot be reached from `start`. The edge weights can be negative.

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
# goal = 1

# Output: [4, 5, 2, 1]
# The shortest path from node 4 to node 1 is 4 -> 5 -> 2 -> 1.

# Here is the DAG from the example:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/dag-distances-1.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The number of edges is at most `10^6`
# - Each node is labeled from `0` to `V-1`
# - The edge weights are integers between `-10^4` and `10^4`