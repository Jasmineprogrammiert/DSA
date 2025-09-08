# initialize two inward pointers p1, p2 = 0, len(arr) - 1
# if arr[p1] < pivot, increment p1
# if arr[p2] > pivot, decrement p2
# if arr[p1] >= pivot and arr[p2] < pivot, swap them, them increment p1 and decrement p2

# ABOVE DOESN'T HANDLE arr[p] = pivot (can fix it with two pass partition. i.e. a second pass)
# BELOW: DUTCH NATIONAL FLAG ALGO

# initialize three pointers low, curr, high = 0, 0, len(arr) - 1
# low means the dividing line that separates elements less than the pivot
# curr reprensents the curretn value
# if arr[curr] < pivot
    # arr[low], arr[curr] = arr[curr], arr[low]
    # low += 1
    # curr += 1
# elif arr[curr] > pivot
    # arr[curr], arr[high] = arr[high], arr[curr]
    # high -= 1
# else arr[curr] == pivot
    # curr += 1 (harmlessly swapping identical element)
# return arr

# n: arr length
# T: O(n) - pointers check n elements in total
# S: O(1) - no new array is created

def quicksort_partition(arr, pivot):
    low, curr, high = 0, 0, len(arr) - 1
    
    while curr <= high:
        if arr[curr] < pivot:
            arr[low], arr[curr] = arr[curr], arr[low]
            low += 1
            curr += 1
        elif arr[curr] > pivot:
            arr[curr], arr[high] = arr[high], arr[curr]
            high -= 1
        else:
            curr += 1

    return arr

# def quicksort_partition(arr, pivot):
#     l, r = 0, len(arr) - 1

#     while l < r:
#         if arr[l] <= pivot:
#             l += 1
#         elif arr[r] > pivot:
#             r -= 1
#         else:
#             arr[l], arr[r] = arr[r], arr[l]
#             l += 1
#             r -= 1

# # second pass: seperate <= pivot section into < pivot and = pivot
#     boundary = 0
    
#     while boundary < len(arr) and arr[boundary] <= pivot:
#         boundary += 1
        
#     l, r = 0, boundary - 1
    
#     while l < r: 
#         if arr[l] < pivot:
#             l += 1
#         elif arr[r] == pivot:
#             r -= 1
#         else: 
#             arr[l], arr[r] = arr[r], arr[l]
#             l += 1
#             r -= 1

#     return arr



# # Quicksort Partition

# Given an array of integers, `arr`, and an integer, `pivot`, modify `arr` in place using only O(1) extra space so that (1) every element smaller than the pivot appears before every element greater than or equal to the pivot, and (2) every element larger than the pivot appears after every element smaller than or equal to the pivot.

# The relative order of the elements smaller than or greater than the pivot does not matter.

# Example 1:
# Input: arr = [1, 7, 2, 3, 3, 5, 3], pivot = 4
# Output: [1, 2, 3, 3, 3, 7, 5]
# Explanation: The array is partitioned into:
# - Elements less than 4: [1, 2, 3, 3, 3]
# - Elements equal to 4: []
# - Elements greater than 4: [7, 5]
# Other orders, such as [3, 2, 1, 3, 3, 5, 7], would also be valid.

# Example 2:
# Input: arr = [1, 7, 2, 3, 3, 5, 3], pivot = 3
# Output: [1, 2, 3, 3, 3, 7, 5]
# Explanation: The array is partitioned into:
# - Elements less than 3: [1, 2]
# - Elements equal to 3: [3, 3, 3]
# - Elements greater than 3: [7, 5]
# Other orders, such as [2, 1, 3, 3, 3, 5, 7], would also be valid.

# Constraints:

# - 0 ≤ arr.length ≤ 10^6
# - -10^9 ≤ arr[i], pivot ≤ 10^9