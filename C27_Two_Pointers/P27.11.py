# initialize empty list arr, pointers p1 and p2
# p1 traverses in arr1 and p2 traverses in arr2
# while p1 < len(arr1) and p2 < len(arr2)
# compare arr1[p1][1] and arr2[p2][0]:
    # if arr1[p1][1] < arr2[p2][0]:
    # p1 += 1
    # elif arr1[p1][0] > arr2[p2][1]:
    # p2 += 1
    # else
    # they have overlap
    
# if they have overlap:
# intersection = [max(arr1[0], arr2[0]), min(arr1[1], arr2[1])]
# if arr1[p1][1] < arr2[p2][1]:
    # p1 += 1
# else:
    # p2 += 1

def interval_intersection(arr1, arr2):
    res = []
    p1, p2 = 0, 0
    n1, n2 = len(arr1), len(arr2)
    
    while p1 < n1 and p2 < n2:
        int1, int2 = arr1[p1], arr2[p2]
        
        if int1[1] < int2[0]:
            p1 += 1
        elif int1[0] > int2[1]:
            p2 += 1
        else:
            res.append(intersection(int1, int2))
            if int1[1] < int2[1]:
                p1 += 1
            else:
                p2 += 1
    return res

def intersection(int1, int2):
    start = max(int1[0], int2[0])
    end = min(int1[1], int2[1])
    return [start, end]
    
# n1: length of arr1
# n2: length of arr2
# T: O(n1 + n2) - there're at most n1+n2 array length, each element is visited once
    # S: O(n1 + n2) - on worst case a new array of length n1 + n2 is created
# Extra space: O(1) - only using constant extra space for the pointers, not counting the output array


# # Interval Intersection

# In this problem, we represent an interval as an array with two integers, `[start, end]`, where `start <= end`. Both endpoints are considered part of the interval, which may consist of a singular point if `start == end`.

# You are given two arrays of intervals, `arr1` and `arr2`. For each array, the intervals are non-overlapping (they don't even share an endpoint) and sorted from left to right. Return a similarly non-overlapping, sorted array of intervals representing the _intersection_ of the intervals in `arr1` and `arr2`. An interval shouldn't start at the same value where another interval ends.

# Example 1:
# Input:
# arr1 = [[0, 1], [4, 6], [7, 8]]
# arr2 = [[2, 3], [5, 9], [10, 11]]
# Output: [[5, 6], [7, 8]]
# Explanation:
# - [4, 6] from arr1 intersects with [5, 9] from arr2 to give [5, 6]
# - [7, 8] from arr1 intersects with [5, 9] from arr2 to give [7, 8]

# Example 2:
# Input:
# arr1 = [[2, 4], [5, 8]]
# arr2 = [[3, 3], [4, 7]]
# Output: [[3, 3], [4, 4], [5, 7]]
# Explanation:
# - [2, 4] intersects with [3, 3] to give [3, 3]
# - [2, 4] intersects with [4, 7] to give [4, 4]
# - [5, 8] intersects with [4, 7] to give [5, 7]
# The array [[3, 3], [4, 4], [5, 6], [6, 7]] would not be correct because [5, 6] and [6, 7] can be combined.

# Here is a visualization of Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/interval-intersection-1.png

# Constraints:

# - 0 ≤ arr1.length, arr2.length ≤ 10^6
# - arr1[i].length = arr2[j].length = 2
# - -10^9 ≤ start ≤ end ≤ 10^9 for each interval
# - Each list is sorted and non-overlapping (any two intervals from the same list don't even share an endpoint)