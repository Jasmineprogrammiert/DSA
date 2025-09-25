# a trick to reverse a prefix of any length in place: [prefix suffix] => [suffix prefix]
    # 1. reverse an array in place
    # 2. reverse the first k letters of arr
    # 3. reverse the first n - k letters of arr

# n: arr length
# T: O(n) - pointers check n elements in total
# S: O(1) - arr is modified in place

def prefix_suffix_swap(arr):
    if not arr: return
    
    n = len(arr)
    l, r = 0, n - 1
    
    # Reverse the whole array
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    
    # Reverse the last n/3 elements
    l, r = 2 * n // 3, n - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    
    # Reverse the first 2n/3 elements
    l, r = 0, (2 * n // 3) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    
    return arr

# brute force:
# each portion: len(arr) // 3
# remove the first portion and append it to the end of the arr
# def prefix_suffix_swap(arr):
#     if not arr: return []
    
#     portion = len(arr) // 3
    
#     for _ in range(portion):
#         ele = arr.pop(0)
#         arr.append(ele)
    
#     return arr
# n: arr length
# T: O(n^2) - pop(0) operations that require shifting all remaining elements n//3 * n times
# S: O(1) - arr is modified in place



# # Prefix Suffix Swap

# We are given an array of letters, `arr`, with a length, `n`, which is a multiple of `3`. The goal is to modify `arr` in place to move the prefix of length `n/3` to the end and the suffix of length `2n/3` to the beginning.

# Example 1:
# Input: arr = ['b', 'a', 'd', 'r', 'e', 'v', 'i', 'e', 'w']
# Output: ['r', 'e', 'v', 'i', 'e', 'w', 'b', 'a', 'd']
# Explanation: The first third (bad) moves to the end, while the rest (review) stays in order.

# Example 2:
# Input: arr = ['a', 'b', 'c']
# Output: ['b', 'c', 'a']

# Example 3:
# Input: arr = []
# Output: []

# Constraints:

# - The length of arr is divisible by 3
# - 0 ≤ arr.length ≤ 10^6
# - arr[i] is a letter