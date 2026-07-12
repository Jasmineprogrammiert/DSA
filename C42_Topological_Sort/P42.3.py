# Flipping shortest → longest takes two linked changes:
#
# 1. The sentinel flips sign: float("inf") → float("-inf")
#   - This touches the init: dist = [NEG_INF] * V
#   - …and the unreachable guard: if dist[node] == NEG_INF
# 2. min → max in the relaxation:
#   dist[nbr] = max(dist[nbr], dist[node] + w)
# Same skeleton as P42.1 (all-nodes distance); only min/inf flips to max/-inf for longest instead of shortest
# 
# E: number of edges    
# V: number of nodes/vertices
# T: O(V + E) — topo sort and relaxation each touch every node/edge once
# S: O(V) — in_degrees, degree_zero, topo_order, dist are each O(V) (input adjacency list not counted)

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

def dag_longest_path(graph, start):
    V = len(graph)
    topo_order = topological_sort(graph)

    NEG_INF = float("-inf")
    dist = [NEG_INF] * V
    dist[start] = 0
    for node in topo_order:
        if dist[node] == NEG_INF:
            continue
        for nbr, w in graph[node]:
            dist[nbr] = max(dist[nbr], dist[node] + w)

    return dist


# # DAG Longest Path

# Given the adjacency list of a DAG with edge weights, `graph`, and a node, `start`, return an array of length `V` (the number of nodes) with the length of the longest path from `start` to every other node (or `-infinity` if the node is unreachable). The edge weights can be negative.

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

# Output: [-infinity, 31, 21, -infinity, 0, 14]
# Nodes 0 and 3 are unreachable from node 4.
# The longest path from node 4 to node 1 is 4 -> 2 -> 1.

# Here is the DAG from the example:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/dag-distances-1.png

# Constraints:

# - The number of nodes is at most `10^5`
# - The number of edges is at most `10^6`
# - Each node is labeled from `0` to `V-1`
# - The edge weights are integers between `-10^4` and `10^4`