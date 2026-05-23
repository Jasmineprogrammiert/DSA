# Approach 1 - Heap: O(n log k)
#   Iterate through the arr, maintaining a heap of size k
#   that always holds the k smallest elements seen so far
# 
# n: length of arr
# k: number of smallest elements
# T: O(n log k) - iterate through arr takes O(n), and each heap operation is O(log k) since the heap has at most k elements
# S: O(k) - the heap holds at most k elements
# 
import heapq

def first_k(arr, k):
    max_heap = []
    for elem in arr:
        if len(max_heap) < k:
            # Negate values to simulate a max_heap (largest on top)
            heapq.heappush(max_heap, -elem)
        elif elem < -max_heap[0]:
            heapq.heapreplace(max_heap, -elem)
    return [-x for x in max_heap]

# Approach 2 - Quickselect: O(n) average
#   1. Pick a random pivot and partition the arr so that
#      smaller elements are on the left, larger on the right
#   2. If pivot index == k --> left side is the answer
#      If pivot index > k --> recurse left only
#      If pivot index < k --> recurse right only
# 
# n: length of arr
# k: number of smallest elements
# T: O(n) average - each recursion roughly halves the array: n + n/2 + n/4 + ... = 2n
# S: O(n) - left, mid and right lists hold a copy of the entire array at each level
# 
import random

def first_k(arr, k):
    if k >= len(arr): return arr
    
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if len(left) >= k:
        return first_k(left, k)
    elif len(left) + len(mid) >= k:
        return left + mid[:k - len(left)]
    else:
        return left + mid + first_k(right, k - len(left) - len(mid))

# Brute-force
# def first_k(arr, k):
#     res = []
#     for elem in arr:
#         if len(res) < k:
#             res.append(elem)
#         elif elem < res[k-1]:
#             res[k-1] = elem
#         res.sort()
#     return res

# print(first_k([15, 4, 13, 8, 10, 5, 2, 20, 3, 9, 11, 27], 5))



# # First K

# Given an array of `n` unique integers, `arr`, return the `k` smallest numbers, in any order.

# Example 1: arr = [15, 4, 13, 8, 10, 5, 2, 20, 3, 9, 11, 27], k = 5
# Output: [4, 3, 2, 5, 8]. The order doesn't matter.

# Example 2: arr = [5, 3, 1, 4, 2], k = 1
# Output: [1]. The smallest element.

# Example 3: arr = [5, 3, 1, 4, 2], k = 4
# Output: [1, 2, 3, 4]. All elements except the largest one.

# Constraints:

# - `0 ≤ k ≤ n ≤ 10^5`
# - All elements in `arr` are unique
# - Each element in `arr` is between `-10^9` and `10^9`