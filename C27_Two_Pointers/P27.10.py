# initialize empty list res = [], p1, p2 = 0, low
# take low and high as two bounds of an array, using p2 to traverse this non-exisitng array
# low <= arr[p1] <= high
# compare arr and non-existing arr within the given low and high range, 
# push elements that don't exist in arr but exist in non-existing arry to res
# if not arr:
    # return [low, low + ..., high]
# while p2 <= high:
    # if p1 = arr[len] and p2 <= high:
        # res.append(p2)
        # p2 += 1
    # if arr[p1] < low:
        # p1 += 1
    # elif arr[p1] = p2:
        # p1 += 1
        # p2 += 1
    # elif arr[p1] > p2:
        # res.append(p2)
        # p2 += 1
# return res

# n: length of arr
# r: range of (high - low + 1)
# T: O(n + r) - since every element in range [low, high] and arr is visited once
# S: O(1) - only using constant extra space for the pointers, not counting the output array

def missing_num(arr, low, high):
    res = []
    p1, p2 = 0, low
    
    if not arr:
        return list(range(low, high + 1))
    
    while p2 <= high:
        if p1 >= len(arr):
            res.append(p2)
            p2 += 1
        elif arr[p1] < p2:
            p1 += 1
        elif arr[p1] == p2:
            p1 += 1
            p2 += 1
        else:
            res.append(p2)
            p2 += 1
            
    return res

# # Missing Numbers in Range

# Given a sorted array of integers, `arr`, and two values indicating a range, `low` and `high`, with `low <= high`, return a new array with all the numbers in the range that do not appear in `arr`.

# Example 1:
# Input: arr = [6, 9, 12, 15, 18], low = 9, high = 13
# Output: [10, 11, 13]
# Explanation: The numbers 10, 11, and 13 are in the range [9, 13] but not in arr.

# Example 2:
# Input: arr = [], low = 9, high = 9
# Output: [9]
# Explanation: 9 is in the range [9, 9] but arr is empty.

# Example 3:
# Input: arr = [6, 7, 8, 9], low = 7, high = 8
# Output: []
# Explanation: Every number in the range [7, 8] appears in arr.

# Constraints:

# - arr is sorted in ascending order
# - 0 ≤ arr.length ≤ 10^6
# - -10^9 ≤ low ≤ high ≤ 10^9
# - All elements in arr are in the range [-10^9, 10^9]
# - high - low ≤ 10^6