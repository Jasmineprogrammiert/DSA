# multiset: a set that allows repeated elements
# submultiset: removing any number of elements from multiset
# Return the number of unique submultisets with sum `0`, ignoring position

#       0         1         2       COPIES OF 1
#    0  1  2   0  1  2   0  1  2    COPIES OF -1
#    0 -1 -2   1  0 -1   2  1  0    SUM

# n: length of S; u: number of distinct values
# T: O(2^n) - worst case: n distinct values, two choices per group
# S: O(u), at most O(n) - freq, groups and the call stack

from collections import defaultdict

def count_unique_submultisets(S):
    freq = defaultdict(int)
    
    for elem in S:
        freq[elem] += 1
    groups = list(freq.items())

    def visit(i, sub_sum):
        if i == len(groups):
            if sub_sum == 0:
                return 1
            return 0
        val, count = groups[i]
        total = 0

        for k in range(count + 1):
            total += visit(i + 1, sub_sum + k * val)
        return total
    
    return visit(0, 0)


# # Count Unique Submultisets With Sum Zero

# A _multiset_ is a set that allows repeated elements. A _submultiset_ of a multiset `S` is another multiset obtained by removing any number of elements from `S`.

# We are given an array with `n` integers representing a multiset (it can have duplicates).

# Return the number of **unique** submultisets of `S` with sum `0`, ignoring which position in `S` the values came from.

# Example 1: S = [1, 1, -1, -1]
# Output: 3. The unique submultisets with sum 0 are [], [1, 1, -1, -1] and [1, -1]. The last one can be obtained in more than one way.

# Example 2: S = []
# Output: 1. [] is a submultiset of [] with sum 0.

# Example 3: S = [-1, 2, 1, 0, 3]
# Output: 4. The unique submultiset with sum 0 are [-1, 1], [-1, 1, 0], [0], and [].

# Constraints:

# - The length of `S` is at most `20`.
# - The elements in `S` are integers.