# 3 groups = remainder mod 3: {0, 1, 2}
# "all 3 groups" is hard to window directly, so count the complement:
#   at most 2 groups  =  missing at least one group  =  not all 3
#   answer = total - atMost(2 groups)
#   total  = n * (n + 1) / 2

from collections import defaultdict


def count_subarrays(arr):
    n = len(arr)
    total = n * (n + 1) // 2
    return total - count_at_most_two(arr)

def count_at_most_two(arr):
    l, r = 0, 0
    freq_map = defaultdict(int)
    count = 0
    while r < len(arr):
        can_grow = arr[r] % 3 in freq_map or len(freq_map) < 2
        if can_grow:
            freq_map[arr[r] % 3] += 1
            r += 1
            count += r - l
        else:
            freq_map[arr[l] % 3] -= 1
            if freq_map[arr[l] % 3] == 0:
                del freq_map[arr[l] % 3]
            l += 1
    return count


# # Count Subarrays With All Remainders

# Given an array of positive integers, `arr`, return the number of subarrays that have at least one of each of the following:

# 1. a multiple of 3
# 2. a number with remainder 1 when divided by 3
# 3. a number with remainder 2 when divided by 3

# Example 1: arr = [9, 8, 7]
# Output: 1
# The subarray [9, 8, 7] counts because:
#   - 9 % 3 is 0
#   - 7 % 3 is 1
#   - 8 % 3 is 2

# Example 2: arr = [1, 2, 3, 4, 5]
# Output: 6
# The subarrays are:
#   - [1, 2, 3]
#   - [2, 3, 4]
#   - [3, 4, 5]
#   - [1, 2, 3, 4]
#   - [2, 3, 4, 5]
#   - [1, 2, 3, 4, 5]

# Example 3: arr = [1, 3, 4, 6, 7, 9]
# Output: 0
# There are no numbers with remainder 2 when divided by 3.

# Constraints:

# - `0 <= arr.length <= 10^5`
# - `1 <= arr[i] <= 10^9`