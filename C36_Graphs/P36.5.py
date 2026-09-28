# Return a boolean array of length `k` where the `i`-th element indicates if the nodes in `queries[i]` are in the same node_to_cc

# node_to_cc: a max set of nodes that are all reachable from each other

# 0 1 2 3 4 5       IDX
# 0 1 2 3 4 5       NODE
# 0 0 0 1 0 0       GROUP_ID

# V: number of nodes; E: number of edges; Q: number of queries
# T: O(V + E + Q) - DFS visits all nodes and scans all edges; each query takes O(1)
# S: O(V + Q) - labels and call stack use O(V); the output list uses O(Q)

def reachability_queries(graph, queries):
    seen = {}

    def visit(node, group_id):
        seen[node] = group_id
        for nbr in graph[node]:
            if nbr not in seen:
                visit(nbr, group_id)

    group_id = 0
    for node in range(len(graph)):
        if node not in seen:
            visit(node, group_id)
            group_id += 1

    res = []
    for a, b in queries:
        res.append(seen[a] == seen[b])
    return res


# # Reachability Queries

# You are given the adjacency list of an undirected graph, `graph`, as well as an array, `queries`, of length `k`, where `queries[i]` is a pair of node indices.
# Return a boolean array of length `k` where the `i`-th element indicates if the nodes in `queries[i]` are in the same connected component.

# A _connected component_ is a maximal set of nodes that are all reachable from each other.

# Example 1
# graph = [
#   [1],           # Node 0
#   [0, 2, 5, 4],  # Node 1
#   [1, 4, 5],     # Node 2
#   [],            # Node 3
#   [5, 2, 1],     # Node 4
#   [1, 2, 4]      # Node 5
# ]
# queries = [[0, 4], [0, 3]]

# Output: [True, False]
# The True corresponds to query [0, 4] and the False to query [0, 3].

# Example 2:
# graph = [
#   [1],           # Node 0
#   [0, 2],        # Node 1
#   [1]            # Node 2
# ]
# queries = [[0, 2], [0, 1]]

# Output: [True, True]
# All nodes are in the same connected component.

# Example 3:
# graph = [
#   [1],           # Node 0
#   [0],           # Node 1
#   [3],           # Node 2
#   [2]            # Node 3
# ]
# queries = [[0, 1], [0, 2], [2, 3]]

# Output: [True, False, True]
# The graph has two connected components: {0, 1} and {2, 3}.

# Graph from Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/reachability-queries-1.png

# Constraints:

# - `graph.length ≤ 1000`
# - `graph[i].length < 1000`
# - `0 ≤ graph[i][j] < graph.length`
# - The adjacency list is properly formatted, with no parallel edges or self-loops
# - `queries.length ≤ 1000`
# - `0 ≤ queries[i][0], queries[i][1] < graph.length`
# - `queries[i][0] != queries[i][1]`