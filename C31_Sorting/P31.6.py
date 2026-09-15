# n: length of arr
# k: number of smallest elements
# T: O(n) average - one O(n) pass, then one recursive call on about half: n + n/2 + n/4 + ... < 2n. Worst O(n^2) with bad pivots, which random.choice makes unlikely
# S: O(n) - the three lists total n per call and shrink by half each level, same series; plus O(log n) recursion depth

import random

def first_k(arr, k):
    if k == 0:
        return []
    if k >= len(arr):
        return arr

    pivot = random.choice(arr)
    small, mid, large = [], [], []
    for elem in arr:
        if elem < pivot:
            small.append(elem)
        elif elem == pivot:
            mid.append(elem)
        else:
            large.append(elem)

    if k <= len(small):
        return first_k(small, k)
    return small + mid + first_k(large, k - len(small) - len(mid))


# ---- Reference: size-k max-heap, O(n log k) guaranteed ----

# keep a max-heap of the k smallest seen so far; a new element that beats the heap top replaces it
# heapq is a min-heap, so push -elem to get a max-heap

# n: length of arr
# k: number of smallest elements
# T: O(n log k) - each of the n elements does at most one heap operation on a heap of size k
# S: O(k) - the heap holds at most k elements

import heapq

def first_k_heap(arr, k):
    max_heap = []
    for elem in arr:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -elem)
        elif elem < -max_heap[0]:
            heapq.heapreplace(max_heap, -elem)
    return [-x for x in max_heap]


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