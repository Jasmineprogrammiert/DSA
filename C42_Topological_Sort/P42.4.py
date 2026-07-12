# Transferable lesson so far — same skeleton, the update line is the whole
# personality of the problem:
#   shortest     ->  if new < old: paths[v] = new
#   longest      ->  if new > old: paths[v] = new
#   count paths  ->  paths[v] += paths[u]
# 
# E: number of edges    
# V: number of nodes/vertices
# T: O(V + E) — topo sort and the counting pass each touch every node/edge once
# S: O(V) — in_degrees, degree_zero, topo_order, paths are each O(V) (input adjacency list not counted)

from collections import deque


def topological_sort(graph):
    V = len(graph)
    in_degrees = [0] * V
    for node in range(V):
        for nbr in graph[node]:
            in_degrees[nbr] += 1

    degree_zero = deque(node for node in range(V) if in_degrees[node] == 0)

    topo_order = []
    while degree_zero:
        node = degree_zero.popleft()
        topo_order.append(node)
        for nbr in graph[node]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                degree_zero.append(nbr)

    return topo_order

def path_count(graph, start):
    V = len(graph)
    topo_order = topological_sort(graph)

    paths = [0] * V
    paths[start] = 1
    for node in topo_order:
        for nbr in graph[node]:  # each path reaching node extends one step to nbr, so nbr gains node's count
            paths[nbr] += paths[node]

    return paths


# # Counting Paths

# Given the adjacency list of an **unweighted** DAG, `graph`, and a node, `start`, return an array of length `V` (the number of nodes) with the number of different paths from `start` to every node.

# Example:
# graph = [
#   [1],        # Neighbors of node 0
#   [],         # Neighbors of node 1
#   [1],        # Neighbors of node 2
#   [4],        # Neighbors of node 3
#   [1, 2, 5],  # Neighbors of node 4
#   [2]         # Neighbors of node 5
# ]
# start = 4

# Output: [0, 3, 2, 0, 1, 1]
# Nodes 0 and 3 are unreachable from node 4.
# There is a single path from 4 to itself, the empty path.
# There are 3 paths from node 4 to node 1:
#     4 -> 1,
#     4 -> 2 -> 1,
#     4 -> 5 -> 2 -> 1

# Here is the DAG from the example:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/topological-sort-8.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The number of edges is at most `10^6`
# - Each node is labeled from `0` to `V-1`