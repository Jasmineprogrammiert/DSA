# using inward moving pointers
# initialize p1, p2 = 0, len(arr) - 1, and res = []
# the former moves from left to right, the latter one moves from right to left
# while p1 < p2:
# if arr[p1] > arr[p2], res.insert(0, arr[p1])
    # p1 += 1
# if arr[p1] < arr[p2], res.insert(0, arr[p2])
    # p2 -= 1
# if arr[p1] == arr[p2], res.insert(0, arr[p1]), res.insert(0, arr[p2])
    # p1 += 1, p2 -= 1
#if p1 = p2
    # insert res.insert(0, arr[p1])
# return res
# O(n^2) length of ele * number of time items are inserted

# Improved: Create a new array and assign number to according index, so T is O(n)
# initialize res = None * len(arr)
# create a 3rd pointer p3 = len(arr), each time p1 or p2 changes, decrement it by 1

def sort_vally_shaped_array(arr):   
    if not arr:
        return []

    p1, p2, p3 = 0, len(arr) - 1, len(arr) - 1
    res = [None] * len(arr)
    
    while p1 < p2:
        if arr[p1] > arr[p2]:
            res[p3] = arr[p1]
            p1 += 1
            p3 -= 1
        elif arr[p1] < arr[p2]:
            res[p3] = arr[p2]
            p2 -= 1
            p3 -= 1
        else:
            res[p3] = arr[p1]
            p3 -= 1
            p1 += 1
            res[p3] = arr[p2]
            p3 -= 1
            p2 -= 1
    if p1 == p2:
        res[p3] = arr[p1]
        
    return res

# n: length of arr
# T: O(n) - append element to new array n times
# S: O(n) - a new array with the same arr length is created
def sort_vally_shaped_array(arr):   
    if not arr:
        return []

    p1, p2, p3 = 0, len(arr) - 1, len(arr) - 1
    res = [None] * len(arr)
    
    while p1 < p2:
        if arr[p1] >= arr[p2]:
            res[p3] = arr[p1]
            p1 += 1
            p3 -= 1
        else:
            res[p3] = arr[p2]
            p2 -= 1
            p3 -= 1
    res[0] = arr[p1]
        
    return res      
   
             

# # Sort Valley Shaped Array

# A _valley-shaped_ array is an array of integers such that:

# - It can be split into a non-empty prefix and a non-empty suffix
# - The prefix is sorted in decreasing order (duplicates allowed)
# - The suffix is sorted in increasing order (duplicates allowed)

# Given a valley-shaped array, `arr`, return a new array with the elements sorted.

# Example 1: arr = [8, 4, 2, 6]
# Output:  [2, 4, 6, 8]
# Explanation: Note that the decreasing prefix is not necessarily unique. The decreasing prefix could be [8, 4] or [8, 4, 2]. The corresponding increasing suffixes would be [2, 6] or [6].

# Example 2: arr = [1, 2]
# Output:  [1, 2]. The array is already sorted (the decreasing prefix is just [1]).

# Example 3: arr = [2, 2, 1, 1]
# Output:  [1, 1, 2, 2]

# Constraints:

# - 0 ≤ arr.length ≤ 10^6
# - -10^9 ≤ arr[i] ≤ 10^9