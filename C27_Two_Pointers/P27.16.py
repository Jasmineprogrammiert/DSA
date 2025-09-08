# use two inward pointers with a middle benchmark pointer
# l(R), r(B), curr(W) = 0, len(arr) - 1, 0
# while curr <= r
# if arr[curr] == B
    # arr[curr], arr[r] = arr[r], arr[curr]
    # r -= 1
# elif arr[curr] == R
    # arr[l], arr[curr] = arr[curr], arr[l]
    # l += 1
    # curr += 1
# else
    # curr += 1
# return arr

# n: arr length
# T: O(n) - pointers check n elements in total
# S: O(1) - no new array is created

def dutch_flag_pro(arr):
    l, r, curr = 0, len(arr) - 1, 0
    
    while curr <= r:
        if arr[curr] == 'B':
            arr[curr], arr[r] = arr[r], arr[curr]
            r -= 1
        elif arr[curr] == 'R':
            arr[l], arr[curr] = arr[curr], arr[l]
            l += 1
            curr += 1
        else:
            curr += 1
        
    return arr

# Alternative: counting sort
# count the occurence of R and W, then rewrtie the array with R, W and B
 
# def sort_colors(arr):
#     r_count = sum(1 for c in arr if c == 'R')
#     w_count = sum(1 for c in arr if c == 'W')
    
#     i = 0
#     for _ in range(r_count):
#         arr[i] = 'R'
#         i += 1
#     for _ in range(w_count):
#         arr[i] = 'W'
#         i += 1
#     while i < len(arr):
#         arr[i] = 'B'
#         i += 1



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