# Brute force: try every way of splitting the array into k subarrays, which takes exponential time

# A better approach is 'Guess-and-Check Technique':
# Guess a potential maximum sum (max_sum) and check if it's possible to split the array into k subarrays, such that no sum(subarray) > max_sum
# The mininum possible value of the max(subarray) lies between max(arr) and sum(arr): max(arr) <= max_sum <= sum(arr)
# Use binary search with transition_point_recipe(), the is_before() determines whether a given max_sum is too small:
#       smaller max_sum -> smaller allowed subarray sums -> more splits needed -> more than k subarrays

# Can the array be split into k subarrays such that every subarray has sum at most max_sum?
#       => max_sum < max(arr), no. Cause max(arr) is too large to fit into any subarray
#       => max_sum = sum(arr), Yes. Any split will do (only 1 subarray, i.e. the array itself)

# Binary search the transition point where the answer goes from 'no' to 'yes'. 
#       => max_sum is the first 'yes'
#       => is_before(max_sum) can be defined by growing a subarray till sum(subarray) > max_sum.
#       At this point, create a new subarray. Unless the number of subarray > k


# n: the length of the array
# S: the sum of all elements in the array
# T: O(n * log(S)) - binary search takes O(log (S)) steps to converge, and each is_before() takes O(n) to scan through the array
# S: O(1) - only a constant amount of extra space is used regardless of the input size

# The binary search range is between max(arr) and sum(arr), 
# which repeatedly divides this numeric range in half to check if a candidate max sum (mid) is feasible.
# S = sum(arr) - max(arr), which is roughly sum(arr) for large arrays.
# After one step, the interval length is S/2, then S/4, S/8...
# For each binary search, the function get_splits runs a single pass over the array to count how many subarrays are needed for the current max_sum, which takes O(n) time


# When more splits than k is required, the current max_sum is smaller than (before) the actual max_sum
def is_before(arr, k, max_sum): 
    splits = get_splits(arr, max_sum)
    return splits > k

def get_splits(arr, max_sum):
    splits = 1
    sum = 0
    for num in arr:
        if sum + num > max_sum:
            splits += 1
            sum = num # create a new subarray
        else:
            sum += num
    return splits

def min_subarray_sum_split(arr, k):
    l, r = max(arr), sum(arr)
    
    # Check if max(arr) is large enough to split the array into k or fewer subarrays
    if not is_before(arr, k, l):
        return l
    
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(arr, k, mid):
            l = mid
        else: 
            r = mid
    return r
# print(min_subarray_sum_split([10, 5, 8, 9, 11], 3))



# # Min Subarray Sum Split

# Given a non-empty array with `n` positive integers, `arr`, and a number `k` with `1 ≤ k ≤ n`, the goal is to split `arr` into `k` non-empty subarrays so that the largest sum across all subarrays is minimized. Return the largest sum across all `k` subarrays after making it as small as possible. Each subarray must contain at least one value.

# Example 1: arr = [10, 5, 8, 9, 11], k = 3
# Output: 17. There are six ways of splitting the array into three subarrays. The optimal split is: [10, 5], [8, 9], and [11]. The largest sum among the three subarrays is 17.

# Example 2: arr = [10, 10, 10, 10, 10], k = 2
# Output: 30. The optimal split is [10, 10, 10] and [10, 10].

# Example 3: arr = [1, 2, 3], k = 3
# Output: 3. Each element becomes its own subarray.

# Constraints:

# - `1 ≤ n ≤ 10^6`
# - `1 ≤ arr[i] ≤ 10^4`
# - `1 ≤ k ≤ n`