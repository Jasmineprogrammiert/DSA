# w e l l                   S2
# freq_map = {w: 1, e: 1, l: 2}
# shortest = float('inf')

# 0 1 2 3 4 5 6 7 8 9       INDEX
# h e l l o w o r l d       S1
#     l
#                     r
# --------------------------------------------
# missing = len(freq_map)

# while r < len(s1):
# if letter in freq_map:
#       freq_map[letter] -= 1
#       if freq_map[letter] == 0:
#           missing -= 1
# r += 1

# while missing == 0:
#       shortest = min(shortest, r - l)
#       if letter in freq_map:
#           freq_map[letter] += 1
#           if freq_map[letter] > 0:
#               missing += 1
#       l += 1

# return shortest if shortest != float('inf'), else -1
# --------------------------------------------
# shortest = 5
# missing = 1
# freq_map = {w: 0, e: 1, l: -1}

# n: length of s1
# m: length of s2
# T: O(n) - each elem in s1 is visited at most twice; building the dict takes O(m), since m < n, O(2n + m) -> O(n)
# S: O(m) - the dictionary holds at most m distinct characters

from collections import defaultdict

def shortest_period(s1, s2):
    l, r = 0, 0
    freq_map = defaultdict(int)
    shortest = float('inf')

    for char in s2:
        freq_map[char] += 1
    missing = len(freq_map)

    while r < len(s1):
        char = s1[r]
        if char in freq_map:
            freq_map[char] -= 1
            if freq_map[char] == 0:
                missing -= 1
        r += 1

        while missing == 0:
            shortest = min(shortest, r - l)
            if s1[l] in freq_map:
                freq_map[s1[l]] += 1
                if freq_map[s1[l]] > 0:
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