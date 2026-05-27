# 1. Use a stack of lists [val, count]
# 2. For each element in the arr:
#       - If the stack is non-empty and the top has the same value, increment its count
#       - Otherwise, push(elem, 1)
# While the top's count equals k:
#       - Pop it, compute val * k
#       - If the new top == val * k, increment its count
#       - Otherwise, push(val * k, 1)
# 3. Build the result from the stack: expand (val, count) to count copies of val
# 
# n: length of arr
# T: O(n) - each element is pushed and popped at most once; result construction is O(n)
# S: O(n) - worst case no merges happen, every element stays in the stack

def compress_array_by_k(arr, k):
    stack = []
    res = []
    for elem in arr:
        if stack and stack[-1][0] == elem:
            stack[-1][1] += 1
        else:
            stack.append([elem, 1])
        while stack and stack[-1][1] == k:
            merge = stack.pop()[0] * k
            if stack and stack[-1][0] == merge:
                stack[-1][1] += 1
            else:
                stack.append([merge, 1])
    for val, count in stack:
        res += [val] * count
    return res

# More elegent approach but must build the recursion right
def compress_array_by_k(arr, k):
    stack = []
    
    def merge(num):
        if not stack or stack[-1][0] != num:
            stack.append([num, 1]) # push new group
        elif stack[-1][1] < k - 1: # top matches num
            stack[-1][1] += 1 # fewer than k count
        else: 
            stack.pop()
            merge(num * k)
    
    for num in arr:
        merge(num)
    
    res = []
    for num, count in stack:
        for _ in range(count):
            res.append(num)
    return res         
            
# print(compress_array_by_k([1, 9, 9, 3, 3, 3, 4], 3))



# # Compress Array By K

# Given an array of integers, `arr`, and an integer `k ≥ 2`, a _k-compress operation_ finds the first block of `k` consecutive equal numbers and combines them into their sum. If there are no `k` consecutive equal numbers, the array is considered fully k-compressed.

# Here is an example of a 2-compress operation:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/stacks-and-queues-fig2.png

# Your goal is to repeatedly apply k-compress operations until the array is fully k-compressed.

# Example 1: arr = [1, 9, 9, 3, 3, 3, 4], k = 3
# Output: [1, 27, 4]
# The steps are [1, 9, 9, 3, 3, 3, 4] -> [1, 9, 9, 9, 4] -> [1, 27, 4]

# Example 2: arr = [8, 4, 2, 2], k = 2
# Output: [16]

# Example 3: arr = [4, 4, 4, 4], k = 5
# Output: [4, 4, 4, 4]

# Constraints:

# - The length of `arr` is at most `10^5`
# - Each element in `arr` is a non-negative integer less than `10^3`
# - `2 ≤ k ≤ 10^5`