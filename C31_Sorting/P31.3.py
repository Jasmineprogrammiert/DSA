# Problem 31.3 - Delete Operations
# Given an array nums and an array operations:
# - k >= 0: delete the number at index k in the original array (if not already deleted)
# - -1: delete the smallest non-deleted number (tie-break by smaller index)
# Return the state of nums after all operations.
#
# Example: nums = [50, 30, 70, 20, 80], operations = [2, -1, 4, -1] -> [50]
#
# Constraints:
# - 1 <= n <= 10^5
# - elements in nums between -10^9 and 10^9
# - operations.length <= n
# - each operation between -1 and n-1