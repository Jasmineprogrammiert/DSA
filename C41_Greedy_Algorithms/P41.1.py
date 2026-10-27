# a pair of integers `[l, r]`, with `l ≤ r`, representing an interval (with both endpoints included)
#  Return the largest number of non-overlapping intervals.

# intervals = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 9]]
# Output: 2

 
#  IDX          0 1 2 3 4 5 6 7 8 9
#                   i i 
#                 i i i i
#                     i i i i
#                               i i

# count         2
# end           9
# intervals     [[2, 3], [1, 4], [3, 6], [8, 9]]


# n: number of intervals
# T: O(n log n) - sorting dominates the O(n) scan
# S: O(n) - Python sorting workspace; the scan uses O(1) extra space

def most_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    count = 0
    for l, r in intervals:
        if l > end:
            count += 1
            end = r
    return count


# # Most Non-Overlapping Intervals

# Given a list, `intervals`, where each element is a pair of integers `[l, r]`, with `l ≤ r`, representing an interval (with both endpoints included). Return the largest number of non-overlapping intervals.

# Example 1:
# intervals = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 9]]
# Output: 2
# For instance, [2, 3] and [8, 9] don't overlap. We can't add [3, 6] because it overlaps with [2, 3] at value 3.

# Example 2:
# intervals = [[1, 2], [2, 3], [3, 4]]
# Output: 2

# Example 3:
# intervals = [[1, 10], [8, 9], [2, 3]]
# Output: 2

# Constraints:

# - `0 ≤ intervals.length ≤ 10^5`
# - `intervals[i].length = 2`
# - `0 ≤ intervals[i][j] ≤ 10^9`