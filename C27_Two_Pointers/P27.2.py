def smaller_prefixes(arr):
    max_k = len(arr) // 2

    for k in range (1, max_k + 1):
        sum_k = sum(arr[0:k])
        sum_2k = sum(arr[0:2*k])

        if sum_k > sum_2k:
            return False
    
    return True

# Algo: Brute force
# n: length of the array
# T: O(n^2)
# S: O(n)

# O(k): the time to sum up k elements for a particular k
# When all numbers from k = 1 to n/2 are added up, you get:
# O(1) + O(2) + O(3) + ... + O(n/2)
# = 1 + 2 + 3 + ... + m
    # 1 + 2 + 3 + ... + m = (1 + m) + (2 + (m-1)) + (3 + (m-2)) + ... 
    # Each pair sums to (m+1), and you have m/2 such pairs, giving you m(m+1)/2.
# = m*(m+1)/2
# So, for m = n/2:
# Sum = (n/2) * (n/2 + 1) / 2 ≈ n² / 8



def smaller_prefixes(arr):
    n = len(arr)
    prefix = [0] * (n + 1) # sum of all length from 0 to n
    max_k = n // 2
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    for k in range (1, max_k + 1):
        sum_k = prefix[k]
        sum_2k = prefix[2 * k]

        if sum_k > sum_2k:
            return False
    
    return True

# Algo: Brute force (optimized)
# n: length of the array
# T: O(n)
# S: O(n)



def smaller_prefixes(arr):
  sp, fp = 0, 0
  slow_sum, fast_sum = 0, 0
  
  while fp < len(arr):
    slow_sum += arr[sp]
    fast_sum += arr[fp] + arr[fp + 1]
                              
    if slow_sum >= fast_sum:
      return False
    
    sp += 1
    fp += 2
  
  return True
                                
# Algo: Slow and fast pointers
# n: length of the array
# T: O(n) - both pointers traverse the array once, and each element is visited at most once by each pointer
# S: O(1) - constant extra space for the two pointers and running sums
    

  
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