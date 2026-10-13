# arr = ['x', 'y', 'z']

# res  = []
# path = [x y]
# used = [T T F]
# i = 1

# n: length of arr
# T: O(n * n!) - n! permutations, each copied in O(n)
# S: O(n * n!) including output; O(n) auxiliary for path, used and the call stack

def permutation(arr):
    res = []
    path = []
    used = [False] * len(arr)

    def visit():
        if len(path) == len(arr):
            res.append(path.copy())
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            used[i] = True
            path.append(arr[i])
            visit()
            path.pop()
            used[i] = False
    visit()
    return res


# # Permutation Enumeration

# A _permutation_ of a list is a list with the same elements but in any order. Finding all permutations means finding all possible orderings of the input elements.

# Given an array of unique characters, `arr`, return all possible permutations, in any order.

# Example 1: arr = ['x', 'y', 'z']
# Output: [['x', 'y', 'z'],
#          ['x', 'z', 'y'],
#          ['y', 'x', 'z'],
#          ['y', 'z', 'x'],
#          ['z', 'x', 'y'],
#          ['z', 'y', 'x']]

# Example 2: arr = ['x']
# Output: [['x']]

# Constraints:

# - The elements in `arr` are unique.
# - The length of `arr` is at most `10`.