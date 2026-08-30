# [0, l): R
# [l, cur): W
# [cur, r]: unsorted
# (r, end]: B

# RWB                         ORDER
# 0  1  2  3  4  5  6         INDEX
# R  W  B  B  W  R  W         INPUT
# R  R  W  W  W  B  B         RES
#       l
#             r
#             cur

# n: length of arr
# T: O(n) - iterate each element once
# S: O(1) - modify the arr in place

def dutch_flag_pro(arr):
    l, cur, r = 0, 0, len(arr) - 1
    
    while cur <= r:
        if arr[cur] == 'R':
            arr[l], arr[cur] = arr[cur], arr[l]
            l += 1
            cur += 1
        elif arr[cur] == 'W':
            cur += 1
        else:
            arr[cur], arr[r] = arr[r], arr[cur]
            r -= 1
    return arr


# Alternative: counting sort
# count the occurence of R and W, then rewrtie the array with R, W and B
 
def sort_colors(arr):
    r_count = sum(1 for c in arr if c == 'R')
    w_count = sum(1 for c in arr if c == 'W')
    
    i = 0
    for _ in range(r_count):
        arr[i] = 'R'
        i += 1
    for _ in range(w_count):
        arr[i] = 'W'
        i += 1
    while i < len(arr):
        arr[i] = 'B'
        i += 1


# # Dutch Flag Problem

# Given an array, `arr`, containing only of the characters 'R' (red), 'W' (white), and 'B' (blue), sort the array in place so that the same colors are adjacent, with the colors in the order red, white, and blue.

# Example 1:
# Input: arr = ['R', 'W', 'B', 'B', 'W', 'R', 'W']
# Output: ['R', 'R', 'W', 'W', 'W', 'B', 'B']

# Example 2:
# Input: arr = ['B', 'R']
# Output: ['R', 'B']

# Constraints:

# - 0 ≤ arr.length ≤ 10^6
# - arr[i] is either 'R', 'W', or 'B'