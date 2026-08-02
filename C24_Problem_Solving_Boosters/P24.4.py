# freq_map = count(s1) - count(window), del 0 -> empty freq_map == permutation
# 
# INIT freq_map from s1, found = set(), l = r = 0
# while r < len(s2):
#     GROW     freq_map[s2[r]] -= 1, del 0, r += 1
#     if r - l == len(s1):
#         MATCH    not freq_map -> found.add(s2[l:r])
#         SHRINK   freq_map[s2[l]] += 1, del 0, l += 1
# return len(found)

# n1: len(s1), n2: len(s2)
# T: O(n1 * n2) - freq_map takes O(n1) and while loop O(n2), O(n1 * n2) for found.add()
# S: O(n1 * n2) - the set of matched substrings, freq_map is O(1), max 26 letters

# 0 1 2 3 4 5 6 7 8
# t a b b a t h a t
# l
#       r               {} -> hit
#   l
#         r             abb -> {t: 1, b: -1}

from collections import defaultdict

def sub_permutations(s1, s2):
    freq_map = defaultdict(int)
    for char in s1:
        freq_map[char] += 1

    l, r = 0, 0
    found = set()
    while r < len(s2):
        char = s2[r]
        freq_map[char] -= 1
        if freq_map[char] == 0:
            del freq_map[char]
        r += 1

        if r - l == len(s1):
            if not freq_map:
                found.add(s2[l:r])

            char = s2[l]
            freq_map[char] += 1
            if freq_map[char] == 0:
                del freq_map[char]
            l += 1

    return len(found)


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