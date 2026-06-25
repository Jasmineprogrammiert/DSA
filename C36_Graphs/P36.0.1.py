# # Adjacency List Basics

# Given the adjacency list of an undirected graph, `graph`, where `graph[i]` is the
# list of neighbors of node `i`, code the following:

# 1. Return the number of nodes in the graph.
# 2. Return the number of edges in the graph.
# 3. Return the degree of a given node (its number of neighbors).
# 4. Print each neighbor of a given node, one per line.


# adjacency list, graph, undirected graph
# V = number of nodes, E = number of edges


def num_nodes(graph):  # T: O(1), S: O(1)
    return len(graph)

def num_edges(graph):  # undirected — T: O(V), S: O(1)
    count = 0
    for node in range(len(graph)):
        count += len(graph[node])
    return count // 2  # each edge from both endpoints/ Don't half for directed graph

def degree(graph, node):  # T: O(1), S: O(1)
    return len(graph[node])

def print_neighbors(graph, node):  # T: O(degree(node)), S: O(1)
    for nbr in graph[node]:
        print(nbr)