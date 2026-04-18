# 1) Find key-value pairs that have square relationship
# 2) Return their indices 
# => Create a dictionary {value: index} so that any value can be looked up in O(1)
# => Loop through the array, compute arr[i]^2, and check if the square is in the dictionary
#       If it is, append the position of this value and its square to a new list of array. i.e. [i, dict[arr[i]^2]]
# Return the result

# n: the length of arr
# T: O(n) - two passes through the array O(2n), each with O(1) dict lookup
# S: O(n) - pos and res each store up to n entries

def find_all_squares(arr):
    pos = dict()
    res = list()
    
    for idx, val in enumerate(arr):
        pos[val] = idx
        
    for idx, val in enumerate(arr):
        square = val ** 2
        if square in pos:
            res.append([idx, pos[square]])
    return res

# For each value, check both whether its square and square root exists in the map
# DON'T prefer this method, easy to make mistake to do multiple things in a loop
# def find_all_squares(arr):
#     pos = dict()
#     res = list()
    
#     for idx, val in enumerate(arr):
#         square = val ** 2
#         square_root = val ** 0.5
#         int_square_root = int(square_root)
        
#         if square in pos:
#             res.append([idx, pos[square]])
#         if square_root == int_square_root and int_square_root in pos:
#             res.append([pos[int_square_root], idx])
            
#         pos[val] = idx
#     return res



# # Find All Squares

# Given an array of unique integers, `arr`, return a list with all pairs of indices, `[i, j]`, such that `arr[i]^2 == arr[j]`. You can return the pairs in any order.

# Example 1: arr = [4, 10, 3, 100, 5, 2, 10000]
# Output: [[5, 0], [1, 3], [3, 6]]. The 3 pairs of values that satisfy the constraint are (2, 4), (10, 100), and (100, 10000). We return [5, 0] because arr[5] is 2 and arr[0] is 4, and similarly for the other two pairs. Other orders like [[1, 3], [5, 0], [3, 6]] would also be valid.

# Example 2: arr = [1]
# Output: [[0, 0]]. Since 1 is its own square, a 1 forms a pair with itself.

# Constraints:

# - The length of `arr` is at most `10^6`
# - `1 ≤ arr[i] ≤ 10^9`
# - All elements in `arr` are unique