# === Approach 1: solution reconstruction — length DP + backtrack (optimal) ===
# m: len(s1)
# n: len(s2)
# Subproblems: m*n — one per (i, j)
# Non-recursive work: O(1) — memo stores an int (LCS length), not a string
# T: O(m*n) — m*n subproblems * O(1); reconstruction walk O(m+n), dominated
# S: O(m*n) — memo up to m*n int entries (result string O(min(m,n)), dominated)

def lcs(s1, s2):
    memo = {}

    def lcs_rec(i, j):
        if i == len(s1) or j == len(s2):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if s1[i] == s2[j]:
            memo[(i, j)] = 1 + lcs_rec(i + 1, j + 1)
        else:
            memo[(i, j)] = max(lcs_rec(i + 1, j), lcs_rec(i, j + 1))
        return memo[(i, j)]

    i, j = 0, 0
    res = []
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            res.append(s1[i])
            i += 1
            j += 1
        elif lcs_rec(i + 1, j) >= lcs_rec(i, j + 1):
            i += 1
        else:
            j += 1
    return ''.join(res)


# === Approach 2: carry the LCS string in the memo (heavier) ===
# Same recurrence as Approach 1, but stores the LCS STRING instead of its length:
#   base -> ""  |  match -> s1[i] + child  |  mismatch -> longer of the two skips (key=len)
# No backtrack needed (answer is already built), but strings cost O(k) to copy/store.
#
# m: len(s1)
# n: len(s2)
# k = min(m, n): max LCS length -> cost to build/store one result string
# Subproblems: m*n — one per (i, j)
# Non-recursive work: O(k) — match concatenates a string up to k long (O(k) copy); mismatch's max is O(1)
# T: O(m*n*k) — m*n subproblems * O(k) work
# S: O(m*n*k) — memo up to m*n entries, each a string up to k long (recursion stack O(m+n), dominated)

def lcs(s1, s2):
    memo = {}

    def lcs_rec(i, j):
        if i == len(s1) or j == len(s2):
            return ""
        if (i, j) in memo:
            return memo[(i, j)]
        if s1[i] == s2[j]:
            memo[(i, j)] = s1[i] + lcs_rec(i + 1, j + 1)
        else:
            memo[(i, j)] = max(lcs_rec(i + 1, j), lcs_rec(i, j + 1), key=len)
        return memo[(i, j)]

    return lcs_rec(0, 0)


# # Reconstruct Longest Common Subsequence

# Given two strings, `s1` and `s2`, return the longest subsequence that is common to both `s1` and `s2`. A _subsequence_ of a string `s` is a sequence of characters that appears in `s` in the same relative order but not necessarily consecutively. In case of a tie, return any common subsequence of maximum length. The two strings consist of uppercase English letters only.

# Example 1:
# s1 = "HAHAH"
# s2 = "AAAAHH"
# Output: "AAH". The other valid output is "AHH".

# Example 2:
# s1 = ""
# s2 = "AA"
# Output: ""

# Example 3:
# s1 = "ABCD"
# s2 = "ACBAD"
# Output: "ACD". The other valid output is "ABD".

# Constraints:

# - The length of each string is at most `1000`.
# - The two strings consist of uppercase English letters only.