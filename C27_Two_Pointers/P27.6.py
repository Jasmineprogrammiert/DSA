# use two parallel pointers to traverse arr1 and arr2 to generate a new array
# res = [], p1, p2 = 0, 0
# p1 and p2 traverse to arr1 and arr2, respectively
# compare arr1[p1] and arr2[p2], push the smaller one into res, then push the other one
# if they're equal, push arr1[p1] first, then push arr2[p2]
# increment pointers by 1 after each iteration
# if one pointer is out of bound and the other hasn't, push the rest of the arr the pointer is in to res
# return res[]

def merge_sorted_arrays(arr1, arr2):
    res = []
    p1, p2 = 0, 0
    
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            res.append(arr2[p2])
            p2 += 1
        else:
            res.append(arr1[p1])
            res.append(arr2[p2])
            p1 += 1
            p2 += 1
            
    if p1 > len(arr1) - 1:
        res.extend(arr2[p2:])
    if p2 > len(arr2) - 1:
        res.extend(arr1[p1:])
            
    return res

# n: length of arr1 and arr2 
# T: O(n) - each element is visited once
# S: O(n) - a new array with total length of arr1 and arr2 is created



# Given two sorted arrays of integers, `arr1` and `arr2`, return a new array that contains all the elements in `arr1` and `arr2` in sorted order, including duplicates.

# Example 1:
# Input:
# arr1 = [1, 3, 4, 5]
# arr2 = [2, 4, 4]
# Output: [1, 2, 3, 4, 4, 4, 5]
# Explanation: All elements are merged in sorted order.

# Example 2:
# Input:
# arr1 = [-1]
# arr2 = []
# Output: [-1]
# Explanation: When one array is empty, the result is just the other array.

# Example 3:
# Input:
# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Constraints:

# - arr1 and arr2 are sorted in ascending order
# - 0 ≤ arr1.length, arr2.length ≤ 10^6
# - -10^9 ≤ arr1[i], arr2[i] ≤ 10^9