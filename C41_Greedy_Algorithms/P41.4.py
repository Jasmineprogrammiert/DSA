# Greedy: sort, then the biggest m elements are wasted as triplet highs.
#   -> pair the rest as (low, median): each median needs a smaller low
#   -> so medians land on the odd indices 1, 3, 5, ... of the sorted array
#   -> sum arr[1], arr[3], ..., arr[2m-1] where m = len // 3
#
# n: number of elements in arr
# T: O(n log n) — sort dominates, single pass after
# S: O(n) — Python's sort needs extra space

def min_triplet_medians(arr):
    arr.sort()
    median_sum = 0
    for i in range(len(arr) // 3):
        median_sum += arr[2 * i + 1]
    return median_sum


# # Minimum Triplet Medians

# You are given a non-empty list of distinct integers, `arr`, where the length of `arr` is guaranteed to be a multiple of three. Your task is to group the numbers into triplets such that the sum of the medians of each triplet (the middle value in sorted order) is minimized. Return the sum of the medians.

# Example 1:
# arr = [6, 5, 8, 2, 1, 9]

# Output: 8
# One optimal grouping is [1, 2, 8], [5, 6, 9]
# The sum of the medians is 2 + 6 = 8
# Another optimal grouping is [1, 2, 9], [5, 6, 8]

# Example 2:
# arr = [6, 5, 8, 2, 1, 9, 12, 15, 14]

# Output: 17
# One optimal grouping is [5, 6, 14], [1, 2, 12], [8, 9, 15]
# The sum of the medians is 6 + 2 + 9 = 17

# Constraints:

# - The length of `arr` is a multiple of three.
# - `3 <= arr.length < 10^5`
# - `1 <= arr[i] <= 10^9`
# - All elements in `arr` are distinct.