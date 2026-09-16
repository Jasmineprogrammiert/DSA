# sorted array of integers
# the number of occurrences of "target" in arr is a multiple of `k`

# target = 2, k = 3
# 0 1 2 3 4 5 6 7       IDX
# 1 2 2 2 2 2 2 3       ARR
#   ^         ^
#   first     last      count = last - first + 1 = 6 - 1 + 1 = 6

# transition_point(is_before): first index where is_before is False
#   l = rightmost index known True, r = leftmost index known False; they squeeze until adjacent
#   first = transition_point(arr[i] < target)        False starts at the first target
#   last  = transition_point(arr[i] <= target) - 1   False starts one past the last target

# n: length of arr
# T: O(log n) - two binary searches, each halves the range per iteration
# S: O(1) - a fixed number of variables regardless of the size of arr

def target_count_divisible_by_k(arr, target, k):
    def transition_point(is_before):    # first index where is_before is False; len(arr) if none
        l, r = 0, len(arr) - 1
        if not is_before(l):
            return 0
        if is_before(r):
            return len(arr)
        while r - l > 1:
            mid = (l + r) // 2
            if is_before(mid):
                l = mid
            else:
                r = mid
        return r

    first = transition_point(lambda i: arr[i] < target)
    last = transition_point(lambda i: arr[i] <= target) - 1
    return (last - first + 1) % k == 0


# # Target Count Divisible by K

# Given a sorted array of integers, `arr`, a target value, `target`, and a positive integer, `k`, return whether the number of occurrences of the target in the array is a multiple of `k`.

# Example 1: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 3
# Output: True. 2 occurs 6 times, which is a multiple of 3.

# Example 2: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 4
# Output: False. 2 occurs 6 times, which is not a multiple of 4.

# Example 3: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 4, k = 3
# Output: True. 4 occurs 0 times, and 0 is a multiple of any number.

# Constraints:

# - `1 ≤ arr.length ≤ 10^6`
# - `-10^9 ≤ arr[i], target ≤ 10^9`
# - `1 ≤ k ≤ 10^6`
# - `arr` is sorted in ascending order