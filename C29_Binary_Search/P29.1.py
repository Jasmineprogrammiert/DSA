# use inward two pointers from the ends of the sorted array
# check if arr[mid] is larger, smaller or equal to the target
# n = length of the array
# T: O(log n) - the number of steps is roughly how many times n can be divided by 2 till it gets down to 1
# S: O(1)

def search_in_sorted_arr(arr, target):
    l, r = 0, len(arr) - 1
    
    while l < r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
# print(search_in_sorted_arr([-2, 0, 3, 4, 7, 9, 11], 2))



# # Search in Sorted Array

# Given a sorted array of integers, `arr`, and a target value, `target`, return the target's index if it exists in the array or `-1` if it doesn't.

# Example 1: arr = [-2, 0, 3, 4, 7, 9, 11], target = 3
# Output: 2. The target 3 is at index 2.

# Example 2: arr = [-2, 0, 3, 4, 7, 9, 11], target = 2
# Output: -1. The target 2 is not in the array.

# Example 3: arr = [1, 2, 3], target = 1
# Output: 0. The target 1 is at index 0.

# Constraints:

# - `0 ≤ arr.length ≤ 10^6`
# - `-10^9 ≤ arr[i], target ≤ 10^9`
# - `arr` is sorted in ascending order, without duplicates