# # Pattern — Prefix Sum + Hashmap (subarray sum = k)   [NEW — high value]
#
# Trigger:
#     COUNT/FIND subarrays by their SUM, negatives allowed
#     -> negatives kill sliding window (sum not monotonic); flip to hashmap lookup.
#
# Core identity:  sum(l..r) = k  <=>  prefix[r] - prefix[l-1] = k
#                                <=>  prefix[l-1] = prefix[r] - k
# -> sweep r once; at each r ask "how many EARLIER prefixes == running - k?"
#   -> seen = {prefix_value: times it occurred}, a HOW-MANY map (tally)
#      key = a running-total value the sweep has visited
#      val = how many past moments sat at that total; each one = a distinct
#            subarray ending at r (starts right after that moment)
#
# seen = {0: 1}            -> empty prefix occurred once, before index 0,
#                             so subarrays starting at index 0 get counted
# running = count = 0
# for x in arr:
#     running += x         -> running == prefix[r]
#     count += ...         -> occurrences of (running - k) seen so far
#     ...                  -> record running; count BEFORE record, else k = 0 matches itself
#
# n: length of arr
# T: O(n) — one sweep, O(1) hashmap lookup/insert per element
# S: O(n) — frequency map holds up to n + 1 distinct prefix values

def count_subarrays_with_sum_k(arr, k):
    seen = {0: 1}
    running = 0
    count = 0
    for x in arr:
        running += x
        count += seen.get(running - k, 0)  # earlier prefixes k below me -> subarrays ending here
        seen[running] = seen.get(running, 0) + 1  # record self for future r's
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