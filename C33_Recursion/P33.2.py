# Input: nested array (elements are ints or arrays)
# Output: the total sum of all ints
# Base case: empty array -> return 0
# Recursive case: 
#   int -> add to res; 
#   list -> recurse on it and add result to res
# 
# n: number of int in arr
# d: max nesting depth
# T: O(n) - iterate through every int in arr 
# S: O(d) - recursion stack depth, worst case O(n)
# Note: each recursive call adds a frame to the call stack that isn't freed until it returns, so the peak memory usage equals the max depth

# Eager checking: 
# check if arr[i] is a number before passing it to a recursive call
def nested_arr_sum_eager(arr):
    res = 0
    for elem in arr: 
        if isinstance(elem, int): # the base case is empty array
            res += elem
        else:
            res += nested_arr_sum_eager(elem)
    return res

# Lazy checking:
# pass arr[i] to a recursive call even if it's a number, and catch it in a base case
def nested_arr_sum_lazy(arr):
    if isinstance(arr, int): # the base case is int 
        return arr
    res = 0
    for elem in arr:
        res += nested_arr_sum_lazy(elem)
    return res

# print(nested_arr_sum_eager([1, [2, 3], [4, [5]], 6]))
# print(nested_arr_sum_lazy([1, [2, 3], [4, [5]], 6]))



# # Nested Array Sum

# A _nested array_ is an array where each element is either:

# 1. An integer, or
# 2. A nested array (note that this is a recursive definition).

# The _sum_ of a nested array is defined recursively as the sum of all its elements.
# Given a nested array, `arr`, return its sum.

# Example 1: arr = [1, [2, 3], [4, [5]], 6]
# Output: 21

# Example 2: arr = [[[[1]], 2]]
# Output: 3

# Example 3: arr = []
# Output: 0

# Example 4: arr = [[], [1, 2], [], [3]]
# Output: 6

# Example 5: arr = [-1, [-2, 3], [4, [-5]], 6]
# Output: 5

# Constraints:

# - The array can be nested to depth at most 500
# - Each integer in the array is between -10^9 and 10^9
# - The total number of integers in the array (counting nested ones) is at most 10^5