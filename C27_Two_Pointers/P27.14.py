# use paraller pointers, a seeker and writter, to modify the arr in place
# use seeker to find unique element, writer represents to-be-written element
# seeker, writer = 0, 0
# while seeker < len(arr)
    # if seeker == 0
        # move both pointers forward by 1
    
    # compare the value of arr[s] and arr[s - 1] (to see if arr[s] is a duplicate)
    # if arr[s] == arr[s-1]
        # move seeker forward by 1 
    # else 
        # arr[w] = arr[s], move both pointers forward by 1
# return the value of writer (the index writer is at), which represents the number of unique value

# IMPROVED
# seeker, writer = 1, 1
# if not arry, return 0
# while seeker < len(arr)
    # if arr[s] != arr[s-1]
        # arr[w] = arr[s]
        # writer += 1
    # seeker += 1
# return ...
    
# ALTERNATIVE
# seeker, writer = 0, 0
# while seeker < len(arr)
    # if seeker == 0 or if arr[s] != arr[s-1]
        # arr[w] = arr[s]
        # writer += 1
# seeker += 1
# return ...

# n: length of arr
# T: O(n) - seeker will check all elements in the array once, pointer is always smaller (slower) than seeker
# O: O(1) - no new array is created

def in_place_duplicate_removal(arr):
    if not arr: return 0

    s, w = 1, 1
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