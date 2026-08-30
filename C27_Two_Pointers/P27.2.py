# 0  1  2  3     INDEX
# 1  2  2  1     ARR
#    p1
#       p2
# p1_sum = 3
# p2_sum = 6

# p1: next index to add to the slow sum
# p2:                          fast
#
# n: length of arr
# T: O(n) - each item is iterated once
# S: O(1) - constant four variable integers regardless of the arr size

def smaller_prefixes(arr):
    p1, p2 = 0, 0
    p1_sum, p2_sum = 0, 0
    
    while p1 < len(arr) // 2:
        p1_sum += arr[p1]
        p2_sum += arr[p2] + arr[p2 + 1]
        
        if p1_sum >= p2_sum:
            return False
        
        p1 += 1
        p2 += 2
        
    return True


# # Smaller Prefixes

# Given an array of integers, `arr`, where the length, `n`, is even, return whether the following condition holds for every `k` in the range `1 ≤ k <= n/2`: "the sum of the first `k` elements is smaller than the sum of the first `2k` elements." If this condition is false for any `k` in the range, return `false`.

# Example 1: arr = [1, 2, 2, -1]
# Output: True. The prefix [1] has a smaller sum than the prefix [1, 2], and the prefix [1, 2] has a smaller sum than the prefix [1, 2, 2, -1]. The other prefixes have length > n/2.

# Example 2: arr = [1, 2, -2, 1, 3, 5]
# Output: False. The prefix [1, 2] has a larger sum than the prefix [1, 2, -2, 1].

# Constraints:

# - len(arr) is even
# - 0 ≤ len(arr) ≤ 10^6
# - -10^9 ≤ arr[i] ≤ 10^9