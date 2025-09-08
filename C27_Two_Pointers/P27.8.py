# use three parallel pointers to traverse arr1, arr2 and arr3 to generate a new array
# initialize res = [], p1, p2, p3 = 0, 0, 0
# each pointer traverses its respective array as long as it's within bounds

# for each iteration:
	# assign v1, v2, and v3 to the current values pointed to by p1, p2, and p3
	# if a pointer is out of bound, assign its value as infinity (a very large number)
	#  find the minimal value among three values
	# append the minimal number to res if:
		# it is not identical to the last number in res
		# increment all pointers whose current value equals the minimal value (last numebr in res)

# return res[]

def three_array_merge(arr1, arr2, arr3):
    res = []
    p1, p2, p3 = 0, 0, 0
    inf = float('inf')
    
    while p1 < len(arr1) or p2 < len(arr2) or p3 < len(arr3):
        v1 = arr1[p1] if p1 < len(arr1) else inf
        v2 = arr2[p2] if p2 < len(arr2) else inf
        v3 = arr3[p3] if p3 < len(arr3) else inf
        min_val = min(v1, v2, v3)
        
        if not res or res[-1] != min_val:
            res.append(min_val)
        
        if min_val == v1:
            p1 += 1
        if min_val == v2:
            p2 += 1
        if min_val == v3:
            p3 += 1
        
    return res

# n: sum of all array length
# T: O(n) - each element is visited once
# S: O(n) - a new array with a length smaller or equal to the total length of all arrays



# # Three Way Merge Without Duplicates

# Given three sorted arrays, `arr1`, `arr2`, and `arr3`, return a new array with the elements of all three arrays, in sorted order, without duplicates.

# Example 1:
# Input:
# arr1 = [2, 3, 3, 4, 5, 7]
# arr2 = [3, 3, 9]
# arr3 = [3, 3, 9]
# Output: [2, 3, 4, 5, 7, 9]
# Explanation: The value 3 appears multiple times in the input but only once in the output.

# Example 2:
# Input:
# arr1 = [1, 2, 3]
# arr2 = [2, 3, 4]
# arr3 = [3, 4, 5]
# Output: [1, 2, 3, 4, 5]
# Explanation: Each duplicate value is included only once.

# Example 3:
# Input:
# arr1 = [1, 1, 1, 1]
# arr2 = [1, 1, 1]
# arr3 = [1, 1]
# Output: [1]
# Explanation: All ones are merged into a single occurrence.

# Constraints:

# - The input arrays are sorted in ascending order
# - 0 ≤ arr1.length, arr2.length, arr3.length ≤ 10^6
# - -10^9 ≤ arr1[i], arr2[i], arr3[i] ≤ 10^9