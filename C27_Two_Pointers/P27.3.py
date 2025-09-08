def _intersection_(arr1, arr2):
    p1, p2 = 0, 0
    arr = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            arr.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1
    return arr

# Algo: Parallel pointers
# n1: the length of arr1
# n2: the length of arr2
# T: O(n1 + n2) - each element in both arrays is visite at most once
# S: O(min(n1, n2))



# # Array Intersection

# Given two sorted arrays, `arr1` and `arr2`, return their _intersection_.

# The intersection is a new array that contains all elements that appear in both arrays, in sorted order, including duplicates.

# Example 1:
# Input:
# arr1 = [1, 2, 3]
# arr2 = [1, 3, 5]
# Output: [1, 3]
# Explanation: 1 and 3 appear in both arrays.

# Example 2:
# Input:
# arr1 = [1, 1, 1]
# arr2 = [1, 1]
# Output: [1, 1]
# Explanation: Two 1s appear in both arrays.

# Example 3:
# Input:
# arr1 = [1, 2, 2, 3]
# arr2 = []
# Output: []

# Constraints:

# - The input arrays are sorted in ascending order
# - 0 ≤ arr1.length, arr2.length ≤ 10^6
# - -10^9 ≤ arr1[i], arr2[i] ≤ 10^9