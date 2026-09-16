# no length -> double k until fetch(k) is out of bounds or >= target, then binary search [k // 2, k]
# out of bounds counts as 'after'

# n: length of the array
# T: O(log n) - log n doublings, then a log n search
# S: O(1) - a few index variables, nothing stored

def search_in_huge_array(target, fetch):
    def is_before(i):
        val = fetch(i)
        return val != -1 and val < target

    k = 1
    while is_before(k):
        k *= 2

    l, r = k // 2, k
    if not is_before(l):
        return l if fetch(l) == target else -1

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