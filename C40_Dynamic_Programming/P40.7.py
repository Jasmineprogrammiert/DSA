# Signature: lcs_rec(i, j) — i = current index into s1, j = current index into s2
# Description: length of the LCS of s1[i:] and s2[j:]
# Base case: i == len(s1) or j == len(s2) -> 0  (a string is exhausted, nothing left in common)
# General case:
#   choices: compare s1[i] vs s2[j] — match or mismatch
#   subproblems: match -> lcs_rec(i+1, j+1); mismatch -> lcs_rec(i+1, j) or lcs_rec(i, j+1)
#   recurse: match counts the paired char (+1); mismatch skips one side
#   aggregate: match -> 1 + child; mismatch -> max of the two skips (maximization problem)
# Original: answer = lcs_rec(0, 0) — LCS of the whole s1 and s2
# DP: overlapping subproblems (e.g. lcs_rec(1,1) reached via two paths) -> memoize on (i, j)
# 
# m: len(s1)
# n: len(s2)
# Subproblems: m*n — one per (i, j)
# Non-recursive work: O(1) — char compare + max of 2
# T: O(m*n) — m*n subproblems * O(1) work
# S: O(m*n) — memo up to m*n entries (recursion stack O(m+n), dominated)

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
            memo[(i, j)] = max(lcs_rec(i+1, j), lcs_rec(i, j+1))
        return memo[(i, j)]
    return lcs_rec(0, 0)

    
# # Longest Common Subsequence

# Given two strings, `s1` and `s2`, return the length of the longest common subsequence that is common to `s1` and `s2`. A _subsequence_ of a string `s` is a sequence of characters that appears in `s` in the same relative order but not necessarily consecutively. The two strings consist of uppercase English letters only.

# Example 1:
# s1 = "HAHAH"
# s2 = "AAAAHH"
# Output: 3.
# There are two common subsequences of length 3: "AAH" and "AHH".

# Example 2:
# s1 = ""
# s2 = "AA"
# Output: 0.

# Example 3:
# s1 = "ABC"
# s2 = "BCA"
# Output: 2.
# The longest common subsequence is "BC".

# Constraints:

# - The length of each string is at least `0` and at most `1000`.
# - The two strings consist of uppercase English letters only.