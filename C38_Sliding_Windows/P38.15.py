# def shortest_period(s1, s2):
#     l, r = 0, 0
#     shortest = float("inf")
#     freq_map = letters still needed
#     missing = distinct letters not yet covered
#     while True:
#         if missing > 0:  # invalid -> grow
#             if r == len(s1):  # can't grow -> stop
#                 break
#             if s1[r] needed:
#                 freq_map[s1[r]] -= 1  # one copy supplied
#                 if freq_map[s1[r]] == 0:
#                     missing -= 1  # letter now covered
#             r += 1
#         else:  # valid -> record, then shrink
#             shortest = min(shortest, r - l)  # r exclusive -> window len
#             if s1[l] needed:
#                 freq_map[s1[l]] += 1  # give the copy back
#                 if freq_map[s1[l]] == 1:
#                     missing += 1  # letter now short again
#             l += 1
#     return shortest

# n: length of s1
# T: O(n) — l and r each only move forward, at most n steps total
# S: O(1) — freq_map holds at most 26 distinct letters

from collections import defaultdict


def shortest_period(s1, s2):
    l, r = 0, 0
    shortest = float('inf')
    freq_map = defaultdict(int)
    for char in s2:
        freq_map[char] += 1
    missing = len(freq_map)

    while True:
        if missing > 0:
            if r == len(s1):
                break
            char = s1[r]
            if char in freq_map:
                freq_map[char] -= 1
                if freq_map[char] == 0:
                    missing -= 1
            r += 1
        else:
            shortest = min(shortest, r - l)
            char = s1[l]
            if char in freq_map:
                freq_map[char] += 1
                if freq_map[char] == 1:
                    missing += 1
            l += 1
    return shortest if shortest != float('inf') else -1


# # Shortest With All Letters

# Given a string, `s1`, and a shorter but non-empty string, `s2`, return the length of the shortest substring of `s1` that has every letter in `s2` at least as many times as they appear in `s2`. If there is no such substring, return `-1`.

# Example 1: s1 = "helloworld", s2 = "well"
# Output: 5. The substring "ellow" in s1 has all the letters in s2.

# Example 2: s1 = "helloworld", s2 = "weelll"
# Output: -1. s1 does not have 2 e's.

# Constraints:

# - `1 <= len(s2) < len(s1) <= 10^5`
# - All characters are lowercase English letters