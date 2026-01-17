# The key is to find the first and last occurance of target in the sorted array
# If present, the number of occurance = the index of last - first + 1
# Then check if this number is multiple of k

# Can run transition_point_recipe() twice, 
# First time define 'before' as anything < target (r points to the first element not less than the target)
# Then define 'before' as <= target (l points to the last element less than or equal to the target)

# n: the length of the sorted array
# T: O(log n) - two separate binary searches are run, O(2*log n) => O(log n)
# S: O(1)

# transition_point_recipe()
   # define 'is_before(val)' to return whether val is 'before'
   # initialize l and r to the first and last values in the range
   # handle three edge cases:
       # the range is empty
       # l is 'after' (the whole range is 'after')
       # r is 'before' (the whole range is 'before')

   # while l and r are not next to each other (r - l > 1)
#        mid = (l + r) // 2
#        if is_before(mid):
#            l = mid
#        else:
#            r = mid
#    return l (last 'before'), r (first 'after'), or something else,
#    depending on the problem

def target_count_divisible_by_k(arr, target, k):
    def first_target_index():
        def is_before(i):
            return arr[i] < target
    
        l, r = 0, len(arr) - 1
        if arr[l] > target or arr[r] < target:
            return -1
        if arr[l] == target:
            return l   
        
        while r - l > 1:
            mid = (l + r) // 2
            if is_before(mid):
                l = mid
            else:
                r = mid
        
        if arr[r] == target:
            return r
        return -1
    
    def last_target_index():
        def is_before(i):
            return arr[i] <= target
        
        l, r = 0, len(arr) - 1
        if arr[r] == target:
            return r
        
        while r - l > 1:
            mid = (l + r) // 2
            if is_before(mid):
                l = mid
            else:
                r = mid
        return l
    
    first = first_target_index()
    if first == -1:
        return True # 0 is a multiple of any number
    last = last_target_index()
    count = last - first + 1
    return count % k == 0

# print(target_count_divisible_by_k([1, 2, 2, 2, 2, 2, 2, 3], 2, 3))



# # Target Count Divisible by K

# Given a sorted array of integers, `arr`, a target value, `target`, and a positive integer, `k`, return whether the number of occurrences of the target in the array is a multiple of `k`.

# Example 1: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 3
# Output: True. 2 occurs 6 times, which is a multiple of 3.

# Example 2: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 4
# Output: False. 2 occurs 6 times, which is not a multiple of 4.

# Example 3: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 4, k = 3
# Output: True. 4 occurs 0 times, and 0 is a multiple of any number.

# Constraints:

# - `1 ≤ arr.length ≤ 10^6`
# - `-10^9 ≤ arr[i], target ≤ 10^9`
# - `1 ≤ k ≤ 10^6`
# - `arr` is sorted in ascending order