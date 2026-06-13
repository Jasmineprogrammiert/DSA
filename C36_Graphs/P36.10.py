# 1. BFS from start -> build the parent map (single traversal serves all queries)
# 2. For each query, reconstruct the path by walking parent pointers back to start
# 3. Unreachable target -> not in parent -> []

# n: nodes (V)
# m: edges (E)
# q: queries, path length up to V
# T: O(V + E + q * V) - BFS once, then reconstruct up to V nodes per query
# S: O(q * V) - parent/queue O(V), output O(q * V)

from collections import deque


def shortest_path_queries(graph, start, queries):
    parent = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in parent:
                parent[nbr] = node
                queue.append(nbr)

    def build_path(target):
        if target not in parent:
            return []
        path = []
        while target is not None:
            path.append(target)
            target = parent[target]
        return path[::-1]

    return [build_path(query) for query in queries]


# # Shortest Path Queries

# You are given the adjacency list of an undirected graph, `graph`, a node index, `start`, and an array, `queries`, where each element is a node index.

# Return an array with the same length as `queries`, where the `i`-th element is an array with the shortest path from `start` to `queries[i]`.

# If there is no path from `start` to `queries[i]`, return an empty array for the `i`-th element.

# Example 1:
# graph = [
#    [1],           # Node 0
#    [0, 2, 5, 4],  # Node 1
#    [1, 4, 5],     # Node 2
#    [],            # Node 3
#    [5, 2, 1],     # Node 4
#    [1, 2, 4]      # Node 5
# ]
# start = 0
# queries = [1, 0, 3, 4]

# Output: [[0, 1], [0], [], [0, 1, 4]]
# Node 3 cannot be reached from node 0

# Example 2:
# graph = [
#    [1],           # Node 0
#    [0, 2],        # Node 1
#    [1]            # Node 2
# ]
# start = 0
# queries = [1, 2]

# Output: [[0, 1], [0, 1, 2]]

# Example 3:
# graph = [
#    [1],           # Node 0
#    [0],           # Node 1
#    [3],           # Node 2
#    [2]            # Node 3
# ]
# start = 0
# queries = [1, 2, 3]

# Output: [[0, 1], [], []]
# Can only reach node 1 from node 0

# Graph from example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/shortest-path-queries-1.png

# Constraints:

# - `graph.length <= 10^4`
# - `graph[i].length < 10^4`
# - `0 <= graph[i][j] < graph.length`
# - `0 <= start < graph.length`
# - `queries.length <= 10^3`
# - `0 <= queries[i] < graph.length`
# - The graph is well-formed, with no parallel edges or self-loops
