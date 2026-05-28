# Array length is a power of 2, find the laminal subarray with the max sum
# Use recursion to split the array in half and compare sums
#
# Recursive func takes a subarray (via indices or slicing):
#   Compute its sum, track the max
#   Base case: length == 1 → return (single element)
#   Find mid, recurse on left half and right half
# Return the max sum
# 
# n: length of array
# S: O(log n) — recursion depth. The array is halved at each level, so the call stack is log n frames deep

# T: O(n) — by BAD method: b=2, d=log n, A=O(1), so O(2^log₂n * 1) = O(n)
def laminal_arr(arr):
    def find_max(l, r):
        if r - l == 1:
            return arr[l], arr[l]
        mid = (l + r) // 2
        left_max, left_sum = find_max(l, mid)
        right_max, right_sum = find_max(mid, r)
        curr_sum = left_sum + right_sum
        return max(left_max, right_max, curr_sum), curr_sum
    return find_max(0, len(arr))[0]

# T: O(n log n) — each of the log n levels sums all n elements
def laminal_arr(arr):
    max_val = float('-inf')
    
    def find_max(arr):
        nonlocal max_val
        s = sum(arr)
        if s > max_val: max_val = s
        if len(arr) == 1: return
        mid = len(arr) // 2
        find_max(arr[:mid])
        find_max(arr[mid:])
    find_max(arr)
    return max_val

# print(laminal_arr([3, -9, 2, 4, -1, 5, 5, -4]))



# # Laminal Arrays

# We are given an array, `arr`, whose **length is a power of 2**.

# We define the set of _laminal arrays_ as follows:

# - The array `arr` is laminal.
# - Each half of a laminal array with even length is laminal.

# Find the laminal array with maximum sum and return its sum.

# Example 1: arr = [3, -9, 2, 4, -1, 5, 5, -4]
# Output: 6
# The laminal arrays are:
# [3, -9, 2, 4, -1, 5, 5, -4],
# [3, -9, 2, 4], [-1, 5, 5, -4],
# [3, -9], [2, 4], [-1, 5], [5, -4],
# [3], [-9], [2], [4], [-1], [5], [5], [-4]
# The one with the maximum sum is [2, 4].

# Example 2: arr = [1]
# Output: 1

# Example 3: arr = [-1, -2]
# Output: -1

# Example 4: arr = [1, 2, 3, 4]
# Output: 10

# Example 5: arr = [-2, -1, -4, -3]
# Output: -1

# Constraints:

# - The length of `arr` is a power of `2`
# - `1 ≤ len(arr) ≤ 10^5`
# - `-10^9 ≤ arr[i] ≤ 10^9`