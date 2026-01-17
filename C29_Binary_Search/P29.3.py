# use the transition_point_recipe()
    # define is_before(i): check if arr[i] is part of the decreasing prefix
        # return true if i == 0 (start of array) or if arr[i] < arr[i - 1] (still decreasing)
        
    # initialize pointers
        # l and r as the first and last values in the range
    
    # handle edge case
        # if the last element is still in the decreasing order, return arr[r] immediately
        
    # binary search for transition point: 
        # while the searching window is larger than 1
        # find midpoint = (l+r) // 2
        # if mid is in the decreasing prefix, move l to mid
        # otherwise move r to m
    
    # return arr[l] in the en, the smallest element at the transition from decreasing to increasing
    
# n = len(arr)
# T: O(log n) - binary search repeatedly halves the search range till valley bottom is found
# S: O(1) - constant extra space is used regardless of input size

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