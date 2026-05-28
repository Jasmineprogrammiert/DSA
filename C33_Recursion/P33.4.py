# recurrence: one function with an inner nested function
# 
# base case: n = 1, return 1. width(1) = 1
# Each recursive call returns the blocks used by n-story castle
# The blocks of n-story castle = 2 * blocks of (n-1) castles + blocks of width
#   blocks of width = 2 * width of (n-1) castle + 1
# 
# Two recurrences to compute:
#   width(n) - needed to know the top row size
#   blocks(n) - the answer
# 
# n: number of castle stories
# T: O(n) - each story is computed once 
# S: O(n) - memo stores n entries, call stack goes n levels deep

def lego_castle(n):
    memo = {}
    
    def blocks_of_width(n):
        if n == 1: return 1
        if n in memo: return memo[n]
        memo[n] = blocks_of_width(n-1)*2 + 1
        return memo[n]
    
    def blocks_of_castle(n):
        if n == 1: return 1
        return blocks_of_castle(n-1)*2 + blocks_of_width(n)

    return blocks_of_castle(n)

# def lego_castle(n):
#     memo = {} # every call to lego_castle creates a fresh empty dict
#     if n == 1: return 1
    
#     def blocks_of_width(n):
#         if n == 1: return 1
#         if n in memo: return memo[n]
#         memo[n] = blocks_of_width(n-1)*2 + 1
#         return memo[n]
        
#     return lego_castle(n-1)*2 + blocks_of_width(n)

# BRUTE FORCE
# def lego_castle(n):
#     if n == 1: return 1
    
#     def blocks_of_width(n):
#         if n == 1: return 1
#         return blocks_of_width(n-1)*2 + 1
    
#     return lego_castle(n-1)*2 + blocks_of_width(n)

# print(lego_castle(4))



# # Lego Castle

# You want to build an `n`-story 2D Lego castle following these instructions:

# - A 1-story castle is just a `1x1` block.
# - An `n`-story castle is made with two `(n-1)`-story castles, side by side, one unit apart, with a row of blocks above them connecting them.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/recursion-fig11.png

# Given `n > 0`, how many `1x1` blocks will you need to buy to build an `n`-story castle?

# Example 1: n = 1
# Output: 1

# Example 2: n = 2
# Output: 5

# Example 3: n = 3
# Output: 17

# Example 4: n = 4
# Output: 49

# Example 5: n = 5
# Output: 129

# Constraints:

# - `1 ≤ n ≤ 57`
# - Assume that the solution will fit in a signed `64`-bit integer.