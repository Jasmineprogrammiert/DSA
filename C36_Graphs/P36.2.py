from collections import deque

# Graph Path - return a simple path from node1 to node2 (3 approaches)
# V: number of nodes
# E: number of edges


# Approach 1: DFS, build the path on the way back (recursive)
# Recurse from node2 toward node1; each call returns the path found so far.
# Root at node2 so base case node1 lands first -> builds in order, no reverse.
# + stops the moment node1 is found (early exit, often less work)
# + one pass, self-contained
# - returns ANY path, not the shortest
# - recursion depth up to O(V)
# T: O(V + E)
# S: O(V) - visited set + call stack

def graph_path(graph, node1, node2):
    visited = set()

    def visit(node):
        if node == node1:
            return [node]
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                path = visit(nbr)
                if path:
                    path.append(node)
                    return path
        return []

    return visit(node2)


# Approach 2: DFS + predecessor map (search, then trace back)
# Record who discovered each node, then follow breadcrumbs node1 -> node2.
# The predecessors dict doubles as the visited set.
# + reusable predecessor map; clean two-phase structure
# - explores node2's whole component, no early exit
# - returns ANY path, not the shortest
# T: O(V + E)
# S: O(V) - predecessors map + call stack

def path_dfs(graph, node1, node2):
    predecessors = {node2: None}

    def visit(node):
        for nbr in graph[node]:
            if nbr not in predecessors:
                predecessors[nbr] = node
                visit(nbr)

    visit(node2)
    if node1 not in predecessors:
        return []
    path = [node1]
    while path[-1] != node2:
        path.append(predecessors[path[-1]])
    return path


# Approach 3: BFS + predecessor map (shortest path)
# Same as Approach 2 but a queue explores ring by ring from node2.
# First time a node is reached is via the fewest steps -> shortest path.
# + returns the SHORTEST path (fewest edges)
# + no recursion, no stack-depth limit
# - explores node2's whole component, no early exit
# T: O(V + E)
# S: O(V) - predecessors map + queue

def path_bfs(graph, node1, node2):
    queue = deque()
    queue.append(node2)
    predecessors = {node2: None}
    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in predecessors:
                predecessors[nbr] = node
                queue.append(nbr)
    if node1 not in predecessors:
        return []
    path = [node1]
    while path[-1] != node2:
        path.append(predecessors[path[-1]])
    return path



# # Graph Path

# Given the adjacency list of an undirected graph, `graph`, and two distinct nodes, `node1` and `node2`, return a simple path from `node1` to `node2`.

# A _simple path_ does not repeat any nodes. Return an empty array if there is no path from `node1` to `node2`.

# Example 1:
# graph = [
#   [1],
#   [0, 2, 5, 4],
#   [1, 4, 5],
#   [],
#   [5, 2, 1],
#   [1, 2, 4]
# ]
# node1 = 0
# node2 = 4

# Output: [0, 1, 4]
# There are other valid answers, like [0, 1, 2, 5, 4].

# Example 2:
# graph = [
#   [1],
#   [0, 2, 5, 4],
#   [1, 4, 5],
#   [],
#   [5, 2, 1],
#   [1, 2, 4]
# ]
# node1 = 0
# node2 = 3

# Output: []
# There is no path to node 3.

# Example 3:
# graph = [
#   [1],
#   [0, 2],
#   [1]
# ]
# node1 = 0
# node2 = 2

# Output: [0, 1, 2]
# A simple path through all nodes.

# Here is a drawing of the graph from Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/graph-path-1.png

# Constraints:

# - `graph.length ≤ 1000`
# - `graph[i].length < 1000`
# - `0 ≤ graph[i][j] < graph.length`
# - `0 ≤ node1, node2 < graph.length`
# - `node1 != node2`
# - The adjacency list is properly formatted, with no parallel edges or self-loops