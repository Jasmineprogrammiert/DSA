# Approach: label every node with its node_to_cc-component id, then compare labels
#   one DFS pass over the graph -> stamp each node with a component id
#   each query [a, b] -> True iff label[a] == label[b]
#
# V: number of nodes
# E: number of edges
# k: number of queries
# T: O(V + E + k) - one DFS pass visits each node and scans each edge once, then O(1) per query
# S: O(V) - label map plus recursion stack depth
#
# Trace (Example 1) - two components: {0,1,2,4,5}=0 and {3}=1
#   node :  0   1   2   3   4   5
#   label:  0   0   0   1   0   0
#   [0, 4] -> 0 == 0 -> True
#   [0, 3] -> 0 == 1 -> False

def reachability(graph, queries):
    node_to_cc = {}

    def visit(node, cc_id):
        node_to_cc[node] = cc_id
        for nbr in graph[node]:
            if nbr not in node_to_cc:
                visit(nbr, cc_id)

    cc_id = 0
    for node in range(len(graph)):
        if node not in node_to_cc:
            visit(node, cc_id)
            cc_id += 1

    return [node_to_cc[a] == node_to_cc[b] for a, b in queries]


# # Reachability Queries

# You are given the adjacency list of an undirected graph, `graph`, as well as an array, `queries`, of length `k`, where `queries[i]` is a pair of node indices.
# Return a boolean array of length `k` where the `i`-th element indicates if the nodes in `queries[i]` are in the same node_to_cc component.

# A _node_to_cc component_ is a maximal set of nodes that are all reachable from each other.

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
# All nodes are in the same node_to_cc component.

# Example 3:
# graph = [
#   [1],           # Node 0
#   [0],           # Node 1
#   [3],           # Node 2
#   [2]            # Node 3
# ]
# queries = [[0, 1], [0, 2], [2, 3]]

# Output: [True, False, True]
# The graph has two node_to_cc components: {0, 1} and {2, 3}.

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