# Model: each letter is a node; each adjacent pair a -> b is an ordering
# constraint (a must appear before b)
#
# Key insight: a single no-repeat supersequence exists iff these constraints
# admit a total order — i.e. the constraint graph is a DAG. So build the graph
# and topo-sort; a cycle (e.g. "ab" + "ba") means no valid ordering exists
#
# Notes:
#   - store neighbors in a set so parallel edges dedupe automatically
#     (repeats can't inflate in-degrees)
#   - factor the cycle check out as a reusable has_cycle
# 
# N: total chars across all strings
# T: O(N) — scan every char to build the graph; the ≤26-node graph makes the sort O(1)
# S: O(1) — sets dedupe edges, so the graph holds ≤26 nodes (O(N) if you keep raw pairs)
#
# P.S. "iff" above is math shorthand for "if and only if" (both directions), not a typo

from collections import deque


def has_cycle(graph):
    # Kahn's peel-off: a graph is a DAG iff every node can be peeled
    in_degrees = {node: 0 for node in graph}
    for node in graph:
        for nbr in graph[node]:
            in_degrees[nbr] += 1

    degree_zero = deque(node for node in graph if in_degrees[node] == 0)

    peeled = 0
    while degree_zero:
        node = degree_zero.popleft()
        peeled += 1
        for nbr in graph[node]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                degree_zero.append(nbr)

    return peeled != len(graph)  # unpeeled nodes => a cycle remains

def can_form_supersequence(arr):
    # Build the constraint graph: every letter a node, each consecutive pair
    # prev -> curr an edge. Neighbor sets dedupe parallel edges automatically
    graph = {}
    for word in arr:
        for char in word:
            # setdefault(k, d): return graph[k], or insert k->d first if k is missing
            graph.setdefault(char, set())
        # zip(word, word[1:]): pair each char with the next -> "abc" gives (a,b),(b,c)
        for prev, curr in zip(word, word[1:]):
            graph[prev].add(curr)

    # A single no-repeat supersequence exists iff the constraints form a DAG.
    return not has_cycle(graph)


# # Supersequence

# A _supersequence_ of a string `s` is another string that contains all the same letters of `s` in the same relative order. For instance, `"aabbcc"` is a supersequence of `"abc"`, but not of `"bca"`.

# Given a non-empty array of strings, `arr`, where each string consists only of lowercase English letters, determine if it is possible to construct a _single_ supersequence of all the strings in `arr` such that no letter appears more than once. Return `true` if such a supersequence exists and `false` otherwise.

# Example 1. arr = ["abc", "bde", "df", "cfe"]
# Output: True. "abcdfe" is a supersequence.

# Example 2. arr = ["ab", "ba"]
# Output: False. Any supersequence would have to
# - include 'a' twice (like "aba") or
# - include 'b' twice (like "bab").

# Example 3. arr = ["aa"]
# Output: False.

# Constraints:

# - The length of each string is at most `100`
# - Each string consists of lowercase English letters