# 1. Iterate each num in the arr
# 2. While the stack is not empty and stack[-1] == num:
#       pop the top, add it to num (merge upward into num)
# 3. After no more merges, push num onto the stack
# 4. Return stack after loop ends
# 
# n: length of arr
# T: O(n) - each element is pushed and popped at most once
# S: O(n) - worst case no merges, stack holds all n elements
def compress_array(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] == num:
            num += stack.pop()
        stack.append(num)
    return stack

# 1. Iterate the arr, push each num onto the stack
# 2. While the stack has at least 2 elements and the top two are equal:
#       pop both, push their sum (repeat this check with the new top)
# 3. Return stack after loop ends
# 
# def compress_array(arr):
#     stack = []
#     for num in arr:
#         stack.append(num)
#         while len(stack) >= 2 and stack[-1] == stack[-2]:
#             stack.pop()
#             stack[-1] *= 2
#     return stack

# print(compress_array([8, 4, 2, 2, 2, 4]))



# # Compress Array

# Given an array of integers, `arr`, a _compress operation_ finds the first pair of consecutive equal numbers and combines them into their sum. If there are no consecutive equal numbers, the array is considered fully compressed. Your goal is to repeatedly compress the array until it is fully compressed.

# Here is an example of a compress operation:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/stacks-and-queues-fig2.png

# Example 1: arr = [8, 4, 2, 2, 2, 4]
# Output: [16, 2, 4].
# The steps are [8, 4, 2, 2, 2, 4] -> [8, 4, 4, 2, 4] -> [8, 8, 2, 4] -> [16, 2, 4]

# Example 2: arr = [4, 4, 4, 4]
# Output: [16]
# The steps are [4, 4, 4, 4] -> [8, 4, 4] -> [8, 8] -> [16]

# Example 3: arr = [1, 2, 3, 4]
# Output: [1, 2, 3, 4]

# Constraints:

# - The length of arr is at most 10^5
# - Each element in arr is a non-negative integer less than 10^3