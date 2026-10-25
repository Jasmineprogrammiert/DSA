# subsequence: in the same relative order (not necessarily consecutively)
# return:
#       tie: any common subsequence of maximum length
#       the longest common subsequence


# dp[i][j]: LCS length of s1[i:] and s2[j:]
# match: 1 + diagonal; otherwise: max(below, right)


# IDX       0 1 2 3 4 5 6
# s1        H A H A H 
#                     i
# s2        A A A A H H
#                     j

# dp[i][j]: best matching length from i and j onward
#                s2 →
#                A A A A H H empty
#                0 1 2 3 4 5 6       j
# s1       i
# H        0     3 3 3 2 2 1 0
# A        1     3 3 3 2 2 1 0
# H        2     2 2 2 2 2 1 0
# A        3     2 2 2 2 1 1 0
# H        4     1 1 1 1 1 1 0
# empty    5     0 0 0 0 0 0 0

# res = AAH


# m: length of s1, n: length of s2
# T: O(m * n) - fill the table; reconstruction takes O(m + n)
# S: O(m * n) - the dp table; res holds at most min(m, n) letters
# These bounds assume both strings are non-empty.

def reconstruct_lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    i = j = 0
    res = []
    while i < m and j < n:
        if s1[i] == s2[j]:
            res.append(s1[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return ''.join(res)


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