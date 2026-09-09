# Trigger:
#     COUNT subarrays by their SUM, negatives allowed
#     -> negatives kill sliding window (sum not monotonic); flip to hashmap lookup
#
# Identity:  sum(l..r) = k  <=>  running[r] - running[l-1] = k
#                           <=>  running[l-1] = running[r] - k
# -> sweep r once; at each r ask "how many EARLIER running totals == running - k?"
#    each one is a prefix to subtract = one subarray ending at r
#
# seen = {running total: times seen so far}
# seen = {0: 1}            -> the empty prefix before index 0 has total 0,
#                             so subarrays starting at index 0 get counted
#
# three moves per element:
#     running += x
#     count += seen[running - k]     -> look up BEFORE recording, else k = 0 matches itself
#     record running

# n: length of arr
# T: O(n) — one sweep, O(1) hashmap lookup/insert per element
# S: O(n) — frequency map holds up to n + 1 distinct prefix values

def count_subarray(arr, k):
    seen = {0: 1}
    running = 0
    count = 0
    for elem in arr:
        running += elem
        count += seen.get(running - k, 0)
        seen[running] = seen.get(running, 0) + 1
    return count


# # Count Subarrays With Sum K

# Given an array of integers, `arr`, and an integer `k`, return the number of subarrays in `arr` with sum `k`.

# Example 1:
# arr = [1, 2, 3, 2, 1], k = 3

# Output: 3
# The subarrays with sum 3 are [1, 2], [3], and [2, 1].

# Example 2:
# arr = [-1, -2, -3, 2, 1], k = -3

# Output: 4
# The subarrays with sum -3 are
#     [-1, -2]
#     [-3]
#     [-2, -3, 2]
#     [-1, -2, -3, 2, 1]

# Constraints:

# - The length of `arr` is at most `10^5`
# - Each element in `arr` is an integer between `-10^4` and `10^4`