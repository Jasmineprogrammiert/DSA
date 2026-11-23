# Example: 0 (10s) and 1 (20s) -> 2 (30s)
# Package 2 waits for both: max(10, 20) + 30 = 50s.

# Build prereq -> dependent edges.
# Toposort, then finish = duration + max(prereq finishes, default 0).
# Return max(finish).

# Example 1 trace
# PACKAGE      0    1     2
# SECONDS     10   20    30
# IMPORTS     []   []    [0, 1]
# GRAPH       [2]  [2]   []       0 -> 2, 1 -> 2
#
# After seeding   INDEGREE [0, 0, 2]   READY deque([0, 1])   TOPO_ORDER []
# After pop 0     INDEGREE [0, 0, 1]   READY deque([1])      TOPO_ORDER [0]
# After pop 1     INDEGREE [0, 0, 0]   READY deque([2])      TOPO_ORDER [0, 1]
# After pop 2     INDEGREE [0, 0, 0]   READY deque([])       TOPO_ORDER [0, 1, 2]
#
# FINISH  [10, 20, 30] -> [10, 20, 40] -> [10, 20, 50]
#                         via 0 -> 2     via 1 -> 2

# V: number of packages
# E: number of dependencies
# T: O(V + E) - each pass does constant work per package and dependency.
# S: O(V + E) - graph stores V lists and E entries. Other structures use O(V).

from collections import deque

def parallel_compilation(seconds, imports):
    V = len(imports)
    graph = [[] for _ in range(V)]
    for pkg in range(V):
        for dep in imports[pkg]:
            graph[dep].append(pkg)

    topo_order = topological_sort(graph)
    finish = seconds.copy()
    for pkg in topo_order:
        for nbr in graph[pkg]:
            finish[nbr] = max(finish[nbr], finish[pkg] + seconds[nbr])

    return max(finish)


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