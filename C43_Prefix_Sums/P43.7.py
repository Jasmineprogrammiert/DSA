# # Pattern — Prefix Sum + Hashmap, LONGEST variant (see P43.6)
#
# Same identity as P43.6:  sum(l..r) = k  <=>  prefix[l-1] = prefix[r] - k
# New question per hit: not HOW MANY earlier prefixes match, but HOW FAR back
#   -> first = {prefix_value: earliest index}, a WHERE map instead of a tally
#   -> hit at i has length i - first[running - k]; keep the max
#
# Three knobs, all forced by "longest":
#   seed {0: -1}        -> empty prefix sits one slot before index 0 (0-based),
#                          so a whole-prefix hit at i = i - (-1) = i + 1, no special case
#   never overwrite     -> smallest stored index maximizes i - index; later dupes can't win
#   lookup, THEN record -> k = 0 would otherwise self-match as a length-0 subarray
#
# first = {0: -1}
# running = 0; best = -1
# for i, x in enumerate(arr):
#     running += x
#     if (running - k) in first:  ...   -> best = max(best, i - first[running - k])
#     ...                               -> record i for running only if unseen
#
# n: length of arr
# T: O(n) — one sweep, O(1) dict lookup/insert per element
# S: O(n) — first holds up to n + 1 distinct prefix values

def longest_subarray_with_sum_k(arr, k):
    first = {0: -1}
    running = 0
    best = -1
    for i, x in enumerate(arr):
        running += x
        if running - k in first:
            best = max(best, i - first[running - k])
        if running not in first:  # keep earliest index -> longest span later
            first[running] = i
    return best


# # Longest Subarray With Sum K

# Given an array of integers, `arr`, and an integer `k`, return the length of the longest subarray in `arr` with sum `k`, or `-1` if there is no such subarray.

# Example 1:
# arr = [1, 2, 3, 2, 1], k = 3

# Output: 2
# The longest subarrays with sum 3 are [1, 2] and [2, 1].

# Example 2:
# arr = [-1, -2, -3, 2, 1], k = -3

# Output: 5
# The longest subarray with sum -3 is [-1, -2, -3, 2, 1].

# Constraints:

# - The length of `arr` is at most `10^5`
# - Each element in `arr` is an integer between `-10^4` and `10^4`