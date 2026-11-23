# Each adjacent pair gives a before -> after edge.
# Process zero-indegree letters with Kahn's algorithm.
# A valid supersequence exists if every letter is processed.

# Example 2: ["ab", "ba"] -> a -> b -> a
# GRAPH       {"a": {"b"}, "b": {"a"}}
# INDEGREE    {"a": 1, "b": 1}
# READY       deque([])
# PROCESSED   0 of 2 -> False

# N: total characters, W: number of words
# T: O(W + N) - scan the words and their adjacent pairs.
# S: O(1) - at most 26 letters, with bounded edges and word slices.

from collections import deque

def can_form_supersequence(arr):
    graph = {}
    for word in arr:
        for char in word:
            graph.setdefault(char, set())
        for prev, curr in zip(word, word[1:]):
            graph[prev].add(curr)

    return not has_cycle(graph)


def has_cycle(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for nbr in graph[node]:
            indegree[nbr] += 1

    ready = deque()
    for node in graph:
        if indegree[node] == 0:
            ready.append(node)

    processed = 0
    while ready:
        node = ready.popleft()
        processed += 1
        for nbr in graph[node]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                ready.append(nbr)

    return processed != len(graph)


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