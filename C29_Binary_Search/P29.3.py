# non-empty, unique elements
# prefix: decreasing order
# suffix: increasing order
# return the smallest value.

# n: length of arr
# T: O(log n) - each iteration halves the search range, O(1) work per iteration
# S: O(1) - a fixed number of variables regardless of the size of arr

def valley_bottom(arr):
    def is_before(i):
        return i == 0 or arr[i] < arr[i - 1]

    l, r = 0, len(arr) - 1
    if is_before(r):
        return arr[r]

    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    return arr[l]


# # Valley Bottom

# A _valley-shaped_ array is an array of integers such that:

# - It can be split into a non-empty prefix and a non-empty suffix,
# - The prefix is sorted in decreasing order,
# - The suffix is sorted in increasing order,
# - All the elements are unique.

# Given a valley-shaped array,  `arr`, return the smallest value.

# Example 1: arr = [6, 5, 4, 7, 9]
# Output: 4

# Example 2: arr = [5, 6, 7]
# Output: 5. The prefix sorted in decreasing order is just [5].

# Example 3: arr = [7, 6, 5]
# Output: 5. The suffix sorted in increasing order is just [5].

# Constraints:

# - `2 ≤ arr.length ≤ 10^6`
# - `-10^9 ≤ arr[i] ≤ 10^9`