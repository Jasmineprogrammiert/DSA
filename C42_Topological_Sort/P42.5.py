# A variant of the longest-path problem (P42.3) with 4 tweaks:
# 1. imports is an adjacency list of INCOMING edges -> build the forward (outgoing) list to run the topo sort
# 2. start nodes = nodes with no incoming edges (empty imports)
# 3. weights live on the nodes (seconds), not the edges
# 4. answer is the max finish time across all nodes
# 
# E: number of edges (dependencies)
# V: number of nodes/vertices (packages, n)
# T: O(V + E) — building the forward graph, the topo sort, and the finish-time relaxation each touch every node/edge once
# S: O(V + E) — the O(E) is ENTIRELY the forward `graph` we build from `imports`: one neighbor entry per dependency, so E entries across V lists. Every other structure (in_degrees, degree_zero, topo_order, finish) is a flat O(V) array

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

    if len(topo_order) < V:
        return []
    return topo_order

def min_compile_time(seconds, imports):
    # Tweak 1: build outgoing graph from incoming 'imports'
    n = len(seconds)
    graph = [[] for _ in range(n)]
    for pkg in range(n):
        for dep in imports[pkg]:
            graph[dep].append(pkg)

    # Tweak 2: start nodes = packages with no imports (in-degree 0)
    topo_order = topological_sort(graph)

    # Tweak 3: weights on nodes — each package starts at its own compile time
    finish = seconds.copy()
    for node in topo_order:
        for nbr in graph[node]:
            finish[nbr] = max(finish[nbr], finish[node] + seconds[nbr])

    return max(finish)  # Tweak 4: whole program done at the last finish time


# # Parallel Compilation

# A compiler needs to compile a program consisting of `n` packages, numbered from `0` to `n - 1`. We are given an array of `n` positive integers, `seconds`, where `seconds[i]` indicates the time it takes to compile package `i`, in seconds. An additional array, `imports`, of length `n`, specifies the package dependencies, where `imports[i]` is the list of packages that package `i` depends on.

# Constraints:

# 1. There are no circular dependencies (no cycles in the dependency graph).
# 2. We cannot start compiling a package until all the packages it depends on have finished compiling.
# 3. There is no limit to how many packages can be compiled **in parallel**, provided they don't depend on each other.
# 4. The program is considered fully compiled when all packages are compiled.

# Determine the minimum time required to compile the entire program.

# Example 1:
# seconds = [10, 20, 30],
# imports = [
#   [],
#   [],
#   [0, 1]
# ]

# Output: 50
# Packages 0 and 1 can be compiled in parallel.
# Package 2 takes 30s and cannot start until packages 0 and 1 finish, which takes 20s.

# Example 2:
# seconds = [10, 20, 30],
# imports = [
#   [],
#   [],
#   []
# ]

# Output: 30
# We can compile all packages in parallel.