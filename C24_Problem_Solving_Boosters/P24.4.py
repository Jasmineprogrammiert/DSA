# # Sub Permutations

# Given two strings, `s1` and `s2`, count how many permutations of `s1` are substrings in `s2`. A permutation of a string `s` is a string with the same letters of `s`, in any order. Assume that `n1 <= n2`, where `n1` is the length of `s1` and `n2` is the length of `s2`.

# Example 1: s1 = "bat", s2 = "tabbathat"
# Output: 2. The permutations are "tab" and "bat".

# Example 2: s1 = "a", s2 = "aa"
# Output: 1. Permutation "a" is counted once even though it appears multiple times.

# Constraints:

# - `1 <= s1.length <= 100`
# - `s1.length <= s2.length <= 10^5`
# - `s1` and `s2` consist of lowercase English letters only