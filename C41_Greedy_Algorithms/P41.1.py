# Greedy: to fit the most intervals, always keep the one that frees up
# the timeline earliest -> the smallest right endpoint.
#   -> sort by right endpoint r
#   -> scan left to right, greedily take an interval when it starts
#      after the last taken one ended (l > prev_end)
#   -> taking the earliest-ending interval never rules out a choice a
#      later-ending one would have allowed -> safe exchange argument
# 
# n: number of intervals
# T: O(n log n) — sort dominates, single linear pass after
# S: O(n) — Python's sort needs extra space; only scalars beyond that

def most_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = float("-inf")
    for l, r in intervals:
        if l > prev_end:
            count += 1
            prev_end = r
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