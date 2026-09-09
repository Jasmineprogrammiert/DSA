# dict = {num: idx}
# 0 1  2 3   4 5 6
# 4 10 3 100 5 2 10000
# check if val**2 is in the dict
# res = [[1, 3], [3, 6], [5, 0]]

# n: length of arr
# T: O(n) - one pass to build {val: idx}, one pass to query it, O(1) per lookup
# S: O(n) - the map holds n entries and res at most n pairs, O(2n) -> O(n)

def find_all_squares(arr):
    pos = {}
    for idx, val in enumerate(arr):
        pos[val] = idx

    res = []
    for idx, val in enumerate(arr):
        square = val ** 2
        if square in pos:
            res.append([idx, pos[square]])
    return res


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