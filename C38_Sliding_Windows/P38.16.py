# sort the arr
# reframe: find the window with at least k elements, minimizing the difference between its min and max

# n: length of arr
# T: O(n log n) — sort dominates; the two-pointer sweep is O(n)
# S: O(n) — Timsort's auxiliary buffer; the pointers and best-pair vars are O(1)

def smallest_range(arr, k):
    l, r = 0, 0
    hightest, lowest = float('inf'), 0
    arr.sort()
    while True:
        must_grow = r - l < k
        if must_grow:
            if r == len(arr):
                break
            r += 1
        else:
            if arr[r - 1] - arr[l] < hightest - lowest:
                hightest, lowest = arr[r - 1], arr[l]
            l += 1
    return [lowest, hightest]


# # Smallest Range With K Elements

# Given an array of integers, `arr`, and a number `k` with `1 ≤ k ≤ len(arr)`, return a pair of numbers `[low, high]`, with `low ≤ high`, representing the smallest range such that there are at least `k` elements in `arr` with values at least `low` and at most `high`.

# If there are multiple valid answers, return any of them.

# Example 1: arr = [1, 2, 5, 7, 8], k = 3
# Output: [5, 8]
# The range has 3 elements in arr (5, 7, and 8).
# It is smaller than other ranges with 3 elements, such as [1, 5], because 8-5 < 5-1.

# Example 2: arr = [5, 5, 2, 2, 8, 8], k = 3
# Output: [2, 5]
# The range has 4 elements in arr (5, 5, 2, and 2).
# There is no smaller range with at least 3 elements.
# [5, 8] is also a valid answer.

# Example 3: arr = [0], k = 1
# Output: [0, 0]

# Constraints:

# - `1 <= k <= len(arr) <= 10^5`
# - `-10^9 <= arr[i] <= 10^9`