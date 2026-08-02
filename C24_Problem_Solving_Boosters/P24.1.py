# BRUTE FORCE + BOTTLENECK
#
# naive       triple nested loop -> O(n^3)
# lower       Omega(n) - output is one bool, but must read every element
# upper       O(n^2) - min(naive O(n^3), TLE)
#             n = 1000 -> n^3 = 10^9 too slow, n^2 = 10^6 fits
#             bounds don't meet -> aim at the lower end
#
# trigger     find a combination of values summing to a target
#
# bottleneck  the innermost loop scans for the 3rd value
#             fix the 1st and 2nd -> 3rd must be w - 1st - 2nd, a membership question


# METHOD 1 - HASH MAP
#
# idea        preprocess {val: [indices]}, look up the complement,
#             accept only at an index other than i and j
# not a set   a set collapses dupes, so it can't tell
#             "the copy you already used" from "a spare copy"
#
# why O(1)    inner scan only continues while k == i or k == j,
#             so it exits by iteration 3 regardless of n
#
# T           O(n) build + O(n^2) pairs x O(1) lookup = O(n^2)
# S           O(n) for the map

from collections import defaultdict


def three_sum_hash(arr, w):
    val_to_idx = defaultdict(list)
    for idx, val in enumerate(arr):
        val_to_idx[val].append(idx)

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            target = w - arr[i] - arr[j]
            for k in val_to_idx.get(target, ()):
                if k != i and k != j:
                    return True
    return False


# METHOD 2 - TWO POINTERS
#
# setup       sort the array
#             for each i: l = i+1, r = n-1, walk them inward
#
# rule        s = arr[i] + arr[l] + arr[r]
#             s == w  ->  True
#             s <  w  ->  move l right   (only way to make s bigger)
#             s >  w  ->  move r left    (only way to make s smaller)
#             l == r  ->  no pair left for this i, next i
#             all i checked, no hit -> False
#
# why safe    when s < w, arr[l] + arr[r] is already the best arr[l] can do
#             (arr[r] is the biggest left), so arr[l] is dead - discard it
#             mirror for r when s > w
#
# T           sort O(n log n) + outer O(n) x inner O(n) = O(n^2)
# why O(n)    each pass moves l or r one step inward,
#             so together they cover the span between them once
# S           O(n) - sorted() builds a new array
# in place    arr.sort() avoids the copy, but Timsort still needs
#             an O(n) buffer internally

def three_sum_two_pointers(arr, w):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            cur_sum = sorted_arr[i] + sorted_arr[l] + sorted_arr[r]
            if cur_sum == w:
                return True
            elif cur_sum < w:
                l += 1
            else:
                r -= 1
    return False


# # 3-Sum

# Given an array of integers, `arr`, and a number `w`, return whether there are 3 integers in `arr` that add up to `w`. We cannot use the value at the same index more than once.

# Example: arr = [4, 4, 5, -6, -4, 0], w = 4
# Output: True. The triplet (4, 4, -4) adds up to 4.

# Example: arr = [5, 0, 1], w = 5
# Output: False. We cannot use the 0 twice.

# Constraints:

# - `0 <= arr.length <= 1000`
# - `-10^7 <= arr[i] <= 10^7
# - `-10^7 <= w <= 10^7`