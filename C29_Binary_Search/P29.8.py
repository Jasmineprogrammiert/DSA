# len(arr) is unknown => double the index until eventually 
#       (1) go "out of bounds" and the API returns -1 or 
#       (2) find an element greater than the target.
# Exponential search: If the length is n, the end of the array can be reached in approx. log2(n) doublings

# transition_point_recipe():
# is_before(val) when it's smaller than target
# inisialize l and r to the first and last values in the range:
    #   l = 0
# handle three edge cases:
#       the range is empty (not applicable)
#       l is 'after'
#       r is 'before'

# while l and r are not next to each other (r - l > 1)
#       mid = (l + r) // 2
#       if is_before(mid):
#           l = mid
#       else:
#           r = mid
# return r (first 'after')
# if fetch(r) != target, return -1

# n: the length of the array
# T: O(log n) - exponential search takes O(log n) to find the valid right boundry, then the binary search take O(log n) to find the target
# S: O(1) - a constant amount of extra space (for variables) is used regardless of the input size

def search_in_huge_array(target, fetch):
    def is_before(i):
        val = fetch(i)
        if val == -1: return False
        return val < target
    
    # check if l is 'after'
    l = 0
    if not is_before(l):
        return 0 if fetch(l) == target else -1
    
    # Step 1: get the rightmost boundry (exponential grow r untill it's 'after' or out of bound)
    r = 1
    while is_before(r):
        r *= 2
    
    # Step 2: Binary Search
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    
    return r if fetch(r) == target else -1



# # Search in Huge Array

# We are trying to search for a target integer, `target`, in a sorted array of positive integers (duplicates allowed) that is too big to fit into memory. We can only access the array through an API, `fetch(i)`, which returns the value at index `i` if `i` is within bounds or `-1` otherwise.

# Using as few calls to the API as possible, return the index of the `target`, or `-1` if it does not exist. If the `target` appears multiple times, return any of the indices.

# There is no API to get the array's length.

# Note: The array is 0-indexed and all elements in the array are positive.

# Example 1: arr = [1, 3, 5, 7, 9], target = 5
# Output: 2. The target 5 is at index 2.

# Example 2: arr = [2, 4, 6, 8, 10], target = 1
# Output: -1. The target 1 is not in the array.

# Example 3: arr = [1, 3, 5, 7, 9], target = 10
# Output: -1. The target 10 is not in the array.

# Constraints:

# - The array is sorted in ascending order
# - The array may contain duplicates
# - All numbers in the array are positive
# - `target` is positive
# - The length of the array is at most `10^9`