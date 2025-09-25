# use inward pointers to swap element

def array_reversal(arr):
    p1, p2 = 0, len(arr) - 1
    
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1

# n: array length
# T: O(n) - there're n/2 swaps and big O ignores constant
# S: O(1) - no new array is created



# # Array Reversal

# Reverse an array of letters, `arr`, in place using `O(1)` extra space.

# Example 1:
# Input: arr = ['h', 'e', 'l', 'l', 'o']
# Output: ['o', 'l', 'l', 'e', 'h']

# Example 2:
# Input: arr = ['a']
# Output: ['a']

# Example 3:
# Input: arr = []
# Output: []

# Constraints:

# - 0 ≤ arr.length ≤ 10^5
# - arr contains only letters