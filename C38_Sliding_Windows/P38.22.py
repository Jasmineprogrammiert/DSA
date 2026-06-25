# If the "at most k" count has the maximum-window property, solve it first and derive the rest:
#   exactly k  = atMost(k) − atMost(k − 1)
#   at least k = total − atMost(k − 1),   total = n(n + 1) / 2 subarrays
# atMost is the standard maximum sliding-window template with a slight modification
# Reuse: computing atMost(k) and atMost(k − 1) once and passing them in halves the passes (2 vs 4)
#
# n: length of arr
# T: O(n) — atMost scans with two forward-only pointers; called a constant number of times
# S: O(1) — a few scalar counters; the derived counts are just subtractions

def at_most(arr, k):
    l = r = 0
    count = drops = 0
    while r < len(arr):
        can_grow = r == 0 or arr[r] >= arr[r - 1] or drops < k
        if can_grow:
            if r > 0 and arr[r - 1] > arr[r]:
                drops += 1
            r += 1
            count += r - l
        else:
            if arr[l] > arr[l + 1]:
                drops -= 1
            l += 1
    return count

def exactly(arr, k):
    if k == 0:
        return at_most(arr, 0)
    return at_most(arr, k) - at_most(arr, k - 1)

def at_least(arr, k):
    n = len(arr)
    total_subarrays = n * (n + 1) // 2
    if k == 0:
        return total_subarrays
    return total_subarrays - at_most(arr, k - 1)

def count_subarrays(arr, k):
    return [
        at_most(arr, k),
        exactly(arr, k),
        at_least(arr, k),
    ]


# # Count Subarrays With Drops

# Given an array, `arr`, of integers and a number `k`, count how many subarrays have:

# 1. at most `k` drops
# 2. exactly `k` drops
# 3. at least `k` drops

# A _drop_ is a sequence of two consecutive numbers where the first is larger than the second.

# Return an array with the three values.

# Example 1: arr = [1, 2, 3], k = 1
# Output: [6, 0, 0]
# - The array has 6 subarrays: [1], [2], [3], [1, 2], [2, 3], and [1, 2, 3].
# - At most k drops:  6. The array has no drops, so every subarray has 0 drops.
# - Exactly k drops:  0. The array has no drops.
# - At least k drops: 0. The array has no drops.

# Example 2: arr = [3, 2, 1], k = 1
# Output: [5, 2, 3]
# - The array has 6 subarrays: [3], [2], [1], [3, 2], [2, 1], and [3, 2, 1].
# - At most k drops:  5. [3, 2] and [2, 1] have 1 drop and [3], [2], and [1] have 0 drops.
# - Exactly k drops:  2. [3, 2] and [2, 1] have exactly 1 drop.
# - At least k drops: 3. [3, 2] and [2, 1] have 1 drop and [3, 2, 1] has 2 drops.

# Example 3: arr = [5, 4, 3, 2, 1], k = 2
# Output: [12, 3, 6]
# - The array has 5 + 4 + 3 + 2 + 1 = 15 subarrays.
# - At most k drops: 12. All the subarrays with 1, 2, or 3, elements.
# - Exactly k drops:  3. All the subarrays with 3 elements: [5, 4, 3], [4, 3, 2], and [3, 2, 1].
# - At least k drops: 6. All the subarrays with 3, 4, or 5 elements.

# Constraints:

# - `0 <= arr.length <= 10^5`
# - `-10^9 <= arr[i] <= 10^9`
# - `0 <= k <= 10^5`