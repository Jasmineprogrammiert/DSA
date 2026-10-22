# 0 1 2 3 4     IDX
# 1 2 3 2 1     ARR
# 1 3 6 8 9     RUNNING
#     i

# remove = running - k = 3
# sum_idx = {0: -1, 1: 0, 3: 1 ...}
# longest = 2

# return the length of the longest subarray in `arr` with sum `k`, or `-1` if there is no such subarray.

# n: length of arr
# T: O(n) average - one pass, O(1) average dictionary lookup/insert per element
# S: O(n) - the dictionary stores at most n + 1 distinct prefix sums

def longest_subarray_sum_k(arr, k):
    longest = -1
    running = 0
    sum_idx = {0: -1}

    for idx, elem in enumerate(arr):
        running += elem
        remove = running - k
        if remove in sum_idx:
            longest = max(longest, idx - sum_idx[remove])
        if running not in sum_idx:
            sum_idx[running] = idx
    return longest


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