# For each element x in the unsorted array, binary searc the sorted array to find -x

# transition_point_recipe():
    # Define is_before(val) to return whethere val is 'before':
    # if the element at that position is less than -x

    # Initialize l and r to the first and last values in the range: 
    # l, r = 0, len(sorted_arr - 1)

    # Handle three edge cases:
        # the range is empty (doesn't apply for this question)
        # l is 'after'
            # when the first element is larger than -x:
            # skip to the next element
        # r is 'before'
            # when the last element is smaller than -x:
            # skip to the next element

    # While l and r are not next to each other (r - l > 1)
        # mid = (l + r) // 2
        # if mid is before the transition(is_before(mid)), move l to mid
        # otherwise, move r to mid
    # Check if sorted_arr[r] equals -x
    # If it does, return [r, current index in unsorted_arr]
    # If the loop is looped through without finding a match, return [-1, -1] 

# n1: length of the sorted array
# n2: length of the unsorted array
# T: O(n2 * log n1)
# S: O(1)

def zero_sum_arr(sorted_arr, unsorted_arr):
    def binary_search(arr, target):
        def is_before(i):
            return arr[i] < target
    
        l, r = 0, len(arr) - 1
        if arr[l] > target or arr[r] < target:
            return -1
        if arr[l] == target:
            return l
        
        while r - l > 1:
            mid = (l + r) // 2
            if is_before(mid):
                l = mid
            else:
                r = mid
        
        if arr[r] == target:
            return r
        return -1
    
    for i, val in enumerate(unsorted_arr):
        idx = binary_search(sorted_arr, -val)
        if idx != -1:
            return [idx, i]    
    return [-1, 1]


    
# # 2-Array 2-Sum

# You are given two non-empty arrays of integers, `sorted_arr` and `unsorted_arr`. The first one is sorted, but the second is not. The goal is to find one element from each array with sum `0`. If you can find them, return an array with their indices, starting with the element in `sorted_arr`. Otherwise, return `[-1, -1]`. Use `O(1)` _extra space_ and do not modify the input.

# Example 1:
# sorted_arr = [-5, -4, -1, 4, 6, 6, 7]
# unsorted_arr = [-3, 7, 18, 4, 6]
# Output: [1, 3]
# Explanation: We can use -4 from the sorted array and 4 from the unsorted array.

# Example 2:
# sorted_arr = [1, 2, 3]
# unsorted_arr = [1, 2, 3]
# Output: [-1, -1]
# Explanation: No pair of elements sums to 0.

# Example 3:
# sorted_arr = [-2, 0, 1, 2]
# unsorted_arr = [0, 2, -2, 4]
# Output: [0, 1]
# Explanation: We can use -2 from the sorted array and 2 from the unsorted array.

# Constraints:

# - `1 ≤ sorted_arr.length, unsorted_arr.length ≤ 10^6`
# - -`10^9 ≤ sorted_arr[i], unsorted_arr[i] ≤ 10^9`
# - `sorted_arr` is sorted in ascending order
# - The arrays have no duplicates
# - Use `O(1)` _extra space_ and do not modify the input