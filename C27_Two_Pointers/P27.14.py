# if not arr, return 0
# s = w = 1
# while s < len(arr)
# arr[s] != arr[s - 1]
#       arr[w] = arr[s], s += 1, w += 1
# else 
#       s += 1
# return w

# n: length of arr
# T: O(n) - the seeker makes one left-to-right pass; the writer never overtakes it
# S: O(1) - two indices, no second array

# INDEX    0, 1, 2, 3, 4, 5, 6
# ORG_ARR  1, 2, 2, 3, 3, 3, 5
# ARR      1, 2, 3, 5, 3, 3, 5
#                      w
#                            s

def duplicate_removal(arr):
    if not arr:
        return 0
    
    s = w = 1
    while s < len(arr):
        if arr[s] != arr[s - 1]:
            arr[w] = arr[s]
            w += 1
        s += 1
    return w


# # In-Place Duplicate Removal

# Given a sorted array of integers, `arr`, remove duplicates in place while preserving the order, and return the number of unique elements. It doesn't matter what remains in `arr` beyond the unique elements.

# Example 1:
# Input: arr = [1, 2, 2, 3, 3, 3, 5]
# Output: 4
# After the operation, the first 4 elements should be [1, 2, 3, 5]
# The last 3 values could be anything

# Example 2:
# Input: arr = []
# Output: 0
# After the operation, the array remains empty

# Example 3:
# Input: arr = [1, 1, 1]
# Output: 1
# After the operation, the first element should be [1]
# The last 2 values could be anything.

# Constraints:

# - The array is sorted in non-decreasing order
# - The length of arr is at most 10^6