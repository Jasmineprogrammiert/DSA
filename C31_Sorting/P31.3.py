# 1. Create a set to track deleted indices
# 2. Create a sorted list of (value, index) tuples for finding the smallest non-deleated element
# 3. Loop through operations:
#       k >= 0 => add k to the deleted set (skipped if already deleted)
#       -1 => iterate through the sorted list, find the first element whose index is not in the deleted set, and delete it
# 4. Build the result: a copy of the original array in which the element index is not in the deleted set
# 
# n: length of nums
# k: length of operations
# T: T(n log n + k) - sorting takes n log n; outer loop runs k times
# S: O(n) - sorted list + deleted set

def delete_operations(nums, operations):
    deleted = set()
    sorted_nums = sorted(enumerate(nums), key=lambda elem: elem[1])
    smallest_idx = 0

    for k in operations:
        if k >= 0:
            deleted.add(k)
        else:
            while smallest_idx < len(nums) and sorted_nums[smallest_idx][0] in deleted:
                smallest_idx += 1 # skip alreadt-deleted
            if smallest_idx < len(nums):
                deleted.add(sorted_nums[smallest_idx][0])
                smallest_idx += 1

    return [num for idx, num in enumerate(nums) if idx not in deleted]

# print(delete_operations([50, 30, 70, 20, 80], [2, -1, 4, -1]))



# # Delete Operations

# You're given an array of `n` integers, `nums`, and another array of at most `n` integers, `operations`, where each integer represents an _operation_ to be performed on `nums`.

# - If the operation number is `k ≥ 0`, the operation is "delete the number at index `k` in the **original** array if it has not been deleted yet. Otherwise, do nothing."
# - If the operation number is `-1`, the operation is "delete the smallest number in `nums` that has not been deleted yet, breaking ties by smaller index."

# Return the state of `nums` after applying all the operations. Every number in operations is guaranteed to be between `-1` and `n-1` inclusive.

# Example 1: nums = [50, 30, 70, 20, 80], operations = [2, -1, 4, -1]
# Output: [50]
# Explanation:
# - Delete index 2 in the original array, element 70: [50, 30, 20, 80]
# - Delete 20, the smallest non-deleted number: [50, 30, 80]
# - Delete index 4 in the original array, element 80: [50, 30]
# - Delete 30, the smallest non-deleted number: [50]

# Example 2: nums = [1, 2, 3], operations = []
# Output: [1, 2, 3]. No operations to perform.

# Example 3: nums = [1, 2, 3], operations = [-1, -1, -1]
# Output: []. All elements are deleted.

# Constraints:

# - `1 ≤ n ≤ 10^5`
# - Each element in `nums` is between `-10^9` and `10^9`
# - `operations.length ≤ n`
# - Each element in `operations` is between `-1` and `n-1`