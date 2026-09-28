# infected = [0]
# graph = [
#   [1, 2],       # Node 0
#   [0, 2],       # Node 1
#   [0, 1, 3],    # Node 2
#   [2]           # Node 3
# ]

# days = 0
# queue = [0]
# dist = {0: 0}

# V: number of nodes; E: number of edges
# T: O(V + E) - each node is processed once and all edges are scanned
# S: O(V) - the queue and infection-day map each hold at most V entries

from collections import deque

def all_infected(graph, infected):
    days = 0
    queue = deque(infected)
    dist = {node: 0 for node in infected}

    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in dist:
                dist[nbr] = dist[node] + 1
                days = max(days, dist[nbr])
                queue.append(nbr)
    return days


# # Days Until All Infected

# Some computers in a network have been infected by a virus. We are given the adjacency list of an undirected, **connected** graph, `graph`, representing the computer network, and an array, `infected`, with the indices of the infected nodes.

# Every day, the virus spreads to all computers directly connected to an infected neighbor computer.

# How many days will it take to infect all computers?

# For example, for this graph:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/days-until-all-infected-1.png

# It takes 3 days for the virus to infect all computers.

# Example 1:
# graph = [
#   [1, 2],       # Node 0
#   [0, 2],       # Node 1
#   [0, 1, 3],    # Node 2
#   [2]           # Node 3
# ]
# infected = [0]

# Output: 2
# On day 1, nodes 1 and 2 get infected
# On day 2, node 3 gets infected

# Example 2:
# graph = [
#   [1],          # Node 0
#   [0, 2],       # Node 1
#   [1, 3],       # Node 2
#   [2, 4],       # Node 3
#   [3],          # Node 4
# ]
# infected = [0, 4]

# Output: 2
# The virus spreads through the line graph from both ends.

# Example 3:
# graph = [
#   [1, 2],       # Node 0
#   [0, 3],       # Node 1
#   [0, 3],       # Node 2
#   [1, 2],       # Node 3
# ]
# infected = [0, 3]

# Output: 1. With two initial infected nodes, all other nodes are infected after one day.

# Constraints:

# - `1 <= graph.length <= 10^4`
# - `graph[i].length < 10^4`
# - `0 <= graph[i][j] < graph.length`
# - `1 <= infected.length <= graph.length`
# - `0 <= infected[i] < graph.length`
# - `infected` does not contain duplicates
# - The graph is well-formed, with no parallel edges or self-loops
# - The graph is connected