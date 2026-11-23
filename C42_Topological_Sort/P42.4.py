# Given an unweighted DAG and a start node, return the path count to each node.
# graph = [[1], [], [1], [4], [1, 2, 5], [2]]
# start = 4 -> [0, 3, 2, 0, 1, 1]

# TOPO ORDER    [0, 3, 4, 5, 2, 1]
# NODE ID       0 1 2 3 4 5
# PATHS         0 3 2 0 1 1

# V: number of nodes
# E: number of directed edges
# T: O(V + E) - a fixed number of passes over the nodes and edges
# S: O(V) - indegree, ready, topo_order and paths each hold at most V entries

from collections import deque

def counting_paths(graph, start):
    def topological_sort(graph):
        V = len(graph)
        indegree = [0] * V
        for node in range(V):
            for nbr in graph[node]:
                indegree[nbr] += 1

        ready = deque()
        for node in range(V):
            if indegree[node] == 0:
                ready.append(node)

        topo_order = []
        while ready:
            node = ready.popleft()
            topo_order.append(node)
            for nbr in graph[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    ready.append(nbr)

        return topo_order

    topo_order = topological_sort(graph)
    paths = [0] * len(graph)
    paths[start] = 1

    for node in topo_order:
        for nbr in graph[node]:
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