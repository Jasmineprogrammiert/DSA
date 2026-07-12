# Count the ways to chop s into palindrome pieces. Two framings below (DP first,
# then topological sort). Both need every palindrome's (l, r) index pair up front,
# so they share one preprocessing helper.
#
# find_palindromes: expand around each center — odd length centers on one char,
# even length on a char pair — recording (l, r) while s[l] == s[r].
#
# n: length of s. Worst case (all letters equal) every substring is a palindrome,
# so there are O(n^2) palindromes -> O(n^2) time and space for both solutions.

def find_palindromes(s):
    n = len(s)
    palindromes = []
    for i in range(n):
        l, r = i, i        # odd length: center on one char
        while l >= 0 and r < n and s[l] == s[r]:
            palindromes.append((l, r))
            l -= 1
            r += 1
        l, r = i, i + 1    # even length: center on the pair (i, i+1)
        while l >= 0 and r < n and s[l] == s[r]:
            palindromes.append((l, r))
            l -= 1
            r += 1
    return palindromes

# ===== DP solution =====
# Logic: count_splits(i) = number of palindromic splits of the suffix s[i:]. Pick
# the first piece — any palindrome s[i:j+1] — and the rest is the subproblem
# count_splits(j+1). Since we're counting, sum over every valid first piece.
#   - base: count_splits(n) = 1 (whole string consumed = one complete split)
#   - answer: count_splits(0); memoize on i, as the result depends only on i
# T: O(n^2) — n subproblems, each scans up to n end positions; set lookups are O(1)
# S: O(n^2) — the palindrome set holds up to O(n^2) pairs (memo/recursion add O(n))

def count_palindromic_splits_dp(s):
    n = len(s)
    if n == 0:
        return 0

    palindrome_set = set(find_palindromes(s))
    memo = {}

    def count_splits(i):
        if i == n:                      # suffix fully consumed -> one complete split
            return 1
        if i in memo:
            return memo[i]

        total = 0
        for j in range(i, n):           # first piece is s[i:j+1] when it's a palindrome
            if (i, j) in palindrome_set:
                total += count_splits(j + 1)

        memo[i] = total
        return total

    return count_splits(0)

# ===== Topological sort solution =====
# Logic: same computation seen as a graph. Positions 0..n are nodes; each
# palindrome s[i:j+1] is an edge i -> j+1; node n is the goal. Every edge points
# left -> right, so the graph is a DAG, and counting splits = counting paths from
# 0 to n. Apply Template 2 (DAG DP) with a += relaxation: counts[0] = 1, then in
# topological order push each node's count forward (counts[nbr] += counts[node]).
# The topo order is trivially 0..n, so Kahn's peel-off is optional — kept for the recipe.
# T: O(n^2) — up to O(n^2) edges; graph build, topo sort, and relaxation are each O(V + E)
# S: O(n^2) — the adjacency list stores up to O(n^2) edges

def topological_sort(graph):
    V = len(graph)
    in_degrees = [0] * V
    for node in range(V):
        for nbr in graph[node]:
            in_degrees[nbr] += 1

    degree_zero = [node for node in range(V) if in_degrees[node] == 0]

    topo_order = []
    while degree_zero:
        node = degree_zero.pop()
        topo_order.append(node)
        for nbr in graph[node]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                degree_zero.append(nbr)
    return topo_order

def count_palindromic_splits(s):
    n = len(s)
    if n == 0:
        return 0

    # Nodes 0..n; edge i -> j+1 means s[i:j+1] is a palindrome. Node n is the goal.
    graph = [[] for _ in range(n + 1)]
    for l, r in find_palindromes(s):
        graph[l].append(r + 1)

    topo_order = topological_sort(graph)   # Recipe 1

    counts = [0] * (n + 1)
    counts[0] = 1
    for node in topo_order:
        for nbr in graph[node]:
            counts[nbr] += counts[node]
    return counts[n]


# # Number Of Palindromic Splits

# A palindrome is a string that reads the same forward and backward, like `"abba"`.

# A _palindromic split_ of a string is a way of dividing a string into substrings where every substring is a palindrome.

# Given a string, `s`, return the number of palindromic splits.

# Example 1:
# s = "abbaab"

# Output: 6
# The palindromic splits are:
# - `a|b|b|a|a|b`
# - `a|bb|a|a|b`
# - `a|b|b|aa|b`
# - `a|bb|aa|b`
# - `abba|a|b`
# - `a|b|baab`

# Example 2:
# s = "aabaa"

# Output: 6
# The palindromic splits are:
# - `a|a|b|a|a`
# - `aa|b|a|a`
# - `a|a|b|aa`
# - `aa|b|aa`
# - `a|aba|a`
# - `aabaa`

# Example 3:
# s = "aaaaa"

# Output: 16

# Example 4:
# s = ""

# Output: 0

# Constraints:

# - The length of the string is at most `10^4`
# - Each character in the string is a lowercase English letter