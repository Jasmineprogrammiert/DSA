import sys
sys.setrecursionlimit(10**5)  # V can reach 10^4; a long chain recurses that deep


# ---- The Best: Union-Find / Disjoint Set Union ----
# Add cables in order; union(node1, node2) each step. Keep a running component
# count (starts at V, drops by 1 on each successful union). Return the index the moment the count hits 1; -1 if it never does.
# Reference: https://start.interviewing.io/beyond-ctci/part-viii-online-chapters/union-find#chapter
#
# T: O(E * a(V)) ~ O(E) - one near-constant union per cable (a = inverse Ackermann)
# S: O(V) - parent + rank arrays

# ---- Better: Binary Search ----
# transition_point_recipe()
#   define is_before(val) to return whether val is 'before'
#   initialize l and r to the first and last values in the range
#   handle edge cases:
#     - the range is empty
#     - l is 'after'  (the whole range is 'after')
#     - r is 'before' (the whole range is 'before')

#   while l and r are not next to each other (r - l > 1)
#     mid = (l + r) // 2
#     if is_before(mid)
#       l = mid
#     else
#       r = mid

#   return l (the last 'before'), r (the first 'after'), or something else, depending on the problem
#
# V: number of nodes
# E: number of cables
# T: O((V + E) log E) - log E probes, each rebuilds the graph + one O(V + E) DFS
# S: O(V + E) - adjacency list + seen set + recursion stack

def all_connected(V, cables):
    def visit(graph, seen, node):
        seen.add(node)
        for nbr in graph[node]:
            if nbr not in seen:
                visit(graph, seen, nbr)

    def is_before(cable_index):
        graph = [[] for _ in range(V)]
        for i in range(cable_index + 1):
            node1, node2 = cables[i]
            graph[node1].append(node2)
            graph[node2].append(node1)
        seen = set()
        visit(graph, seen, 0)
        return len(seen) < V

    l, r = 0, len(cables) - 1
    if is_before(r):
        return -1
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    return r


# ---- Brute force: DFS re-check connectivity after every cable ----
# build an empty undirected adjacency list for V nodes
# for each cable [node1, node2] in order, with index i:
#     add node2 to node1's neighbors and node1 to node2's neighbors
#     DFS from node 0, collecting reachable nodes in `seen`
#     if len(seen) == V: return i
# return -1
#
# T: O(E * (V + E)) - E cables, each triggers a full O(V + E) traversal
# S: O(V + E) - adjacency list + seen set + recursion stack (reused each check)

def all_connected_bruteforce(V, cables):
    graph = [[] for _ in range(V)]

    def is_connected():
        seen = set()
        def visit(node):
            seen.add(node)
            for nbr in graph[node]:
                if nbr not in seen:
                    visit(nbr)
        visit(0)
        return len(seen) == V

    for i, (node1, node2) in enumerate(cables):
        graph[node1].append(node2)
        graph[node2].append(node1)
        if is_connected():
            return i

    return -1


# # First Time All Connected

# We are given `V >= 2`, the number of computers in a data center. The computers are identified with indices from `0` to `V - 1`.

# We are also given a list, `cables`, of length `E` where each element is a pair `[x, y]`, with `0 ≤ x, y < V` and `x != y`, indicating that we should connect the computers with indices `x` and `y` with a cable.

# If we add the cables in the order of the list, at what point will all the computers be connected (meaning that there is a path of cables between every pair of computers)?

# Return the index of the cable in cables after which all the computers are connected or `-1` if that never happens.

# For example, in this figure, if we add the cables in order, the computers become all connected after adding cables `0`, `1`, and `2`.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/graphs_fig12.png

# Example 1:
# V = 4
# cables = [
#   [0, 2],
#   [1, 3],
#   [0, 1],
#   [1, 2]
# ]

# Output: 2
# See image above

# Example 2:
# V = 3
# cables = [[0, 1]]

# Output: -1
# It's impossible to connect 3 computers with only one cable

# Example 3
# V = 4
# cables = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 0]]

# Output: 3
# Redundant cables don't affect the result

# Constraints:

# - `2 <= V <= 10^4`
# - `0 <= E <= 10^5`
# - `0 <= cables[i][0], cables[i][1] < V`
# - `cables[i][0] != cables[i][1]`
# - all the cables are unique