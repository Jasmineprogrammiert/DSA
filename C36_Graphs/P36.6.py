# Goal: is the directed graph strongly connected (every node reaches every other)?
# directed -> reachability is one-way, so check both directions
#
# Brute force: forward BFS/DFS from each node
#   - any start can't reach all V nodes -> False
# V: number of nodes
# E: number of edges
# T: O(V * (V + E)) - one traversal per node
# S: O(V) - visited set
#
# Trick: 2 traversals from one hub (node 0)
#   - forward from 0 on graph          -> reaches all? (0 reaches everyone)
#   - forward from 0 on reversed graph -> reaches all? (everyone reaches 0)
#   - reversing edges turns "who reaches 0" into "who does 0 reach" - one forward pass
#   - both reach all V -> True (any A -> 0 -> B); either misses -> False
# T: O(V + E) - two traversals + build reversed adjacency
# S: O(V + E) - reversed adjacency + visited

def strongly_connected(graph):
    V = len(graph)

    # chunk 1: DFS from node 0 - does it reach all V nodes?
    def reach(adj):
        seen = set()

        def dfs(node):
            seen.add(node)
            for nbr in adj[node]:
                if nbr not in seen:
                    dfs(nbr)
        dfs(0)
        return len(seen) == V

    # chunk 2: reverse every edge node -> nbr into nbr -> node
    rev = [[] for _ in range(V)]
    for node in range(V):
        for nbr in graph[node]:
            rev[nbr].append(node)

    # chunk 3: 0 reaches everyone AND everyone reaches 0
    return reach(graph) and reach(rev)


# # Strongly Connected Graph

# Given the adjacency list of a non-empty **directed** graph, `graph`, return whether it is _strongly connected_.

# A directed graph is strongly connected if every node can reach every other node (in a directed graph, it is possible that `node1` can reach `node2` but not the other way around).

# Below is an image of strongly connected, weakly connected, and disconnected directed graphs. A directed graph is weakly connected if it would be connected if edges didn't have directions.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/strongly-connected-graph-1.png

# Example 1:
# graph = [
#   [1, 3],    # Node 0
#   [2],       # Node 1
#   [0],       # Node 2
#   [2]        # Node 3
# ]

# Output: True
# Left graph in the image above

# Example 2:
# graph = [
#   [1, 2, 3], # Node 0
#   [2],       # Node 1
#   [],        # Node 2
#   [2]        # Node 3
# ]

# Output: False
# Middle graph in the image above
# Node 2 cannot reach node 0, among others

# Example 3:
# graph = [
#   [1],       # Node 0
#   [0],       # Node 1
#   [3],       # Node 2
#   [2]        # Node 3
# ]

# Output: False
# Right graph in the image above
# Node 0 cannot reach node 3, among others

# Constraints:

# - `1 ≤ graph.length ≤ 1000`
# - `graph[i].length < 1000`
# - `0 ≤ graph[i][j] < graph.length`
# - The adjacency list is properly formatted, with no parallel edges or self-loops
# - The graph is directed