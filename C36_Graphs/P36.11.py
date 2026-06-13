# Every node is a possible meeting spot
# Cost of meeting at node v = (edges node1 walks to v) + (edges node2 walks to v) + (edges node3 walks to v)
# Pick the cheapest spot
#
# 1. BFS from each of node1, node2, node3 -> three distance maps
#    (dist1[v] = number of edges from node1 to node v; same for dist2, dist3)
# 2. For each candidate node v: total = dist1[v] + dist2[v] + dist3[v]
# 3. Return the smallest total over all v
#
# V: number of nodes
# E: number of edges
# T: O(V + E) - 3 BFS runs each walk every node and edge once, then an O(V) sweep
# S: O(V) - three distance maps and the queue each hold at most one entry per node

from collections import deque


def min_edges(graph, node1, node2, node3):
    def dist(node):
        distance = {node: 0}
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr not in distance:
                    queue.append(nbr)
                    distance[nbr] = distance[node] + 1
        return distance

    shortest = float('inf')
    dist1, dist2, dist3 = dist(node1), dist(node2), dist(node3)
    for v in range(len(graph)):
        shortest = min(shortest, dist1[v] + dist2[v] + dist3[v])
    return shortest


# # Graph Hangout

# Three friends want to meet. They live in nodes in a connected, undirected graph.

# You are given the adjacency list, `graph`, and the nodes where they start, `node1`, `node2`, and `node3`.

# Return the minimum number of edges they need to traverse in total between the three to meet at _any_ node in the graph.

# For example, for this graph:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/graph-hangout-1.png

# If the three friends start at the nodes labeled `1`, `2` and `3`, they can each get to the middle node by traversing `3` edges. The next closest meeting point is at one of the starting nodes, where the other two friends have to traverse `5` edges each. Thus, the answer is `9`.

# Example 1:
# graph = [
#     [1, 4],   # Node 0
#     [0, 2],   # Node 1
#     [1, 3],   # Node 2
#     [2, 4],   # Node 3
#     [0, 3]    # Node 4
# ]
# node1 = 0
# node2 = 2
# node3 = 4

# Output: 3
# They can meet at node 0 or 4 in combined 3 steps

# Example 2:
# graph = [
#     [1, 2, 3],  # Node 0
#     [0, 2, 3],  # Node 1
#     [0, 1, 3],  # Node 2
#     [0, 1, 2]   # Node 3
# ]
# node1 = 0
# node2 = 1
# node3 = 2

# Output: 2
# In a complete graph, they can meet at any node

# Constraints:

# - `graph.length <= 10^4`
# - `graph[i].length < 10^4`
# - `0 <= graph[i][j] < graph.length`
# - `0 <= node1, node2, node3 < graph.length`
# - The graph is well-formed, with no parallel edges or self-loops