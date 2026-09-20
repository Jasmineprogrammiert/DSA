# + 3 7 15      WIDTH
#   2 3 4       STORY

# An `n`-story castle is made with two `(n-1)`-story castles, side by side, one unit apart, with a row of blocks above them connecting them

# optimal: carry the width up with the block count, one recursion
# n: number of stories
# T: O(n) - one chain of n calls, O(1) work each
# S: O(n) - the call stack

def lego_castle(n):
    if n == 1:
        return 1

    def rec(story):
        if story == 1:
            return 1, 1
        blocks, width = rec(story - 1)
        return blocks * 2 + width * 2 + 1, width * 2 + 1
    return rec(n)[0]

# brute force: the width is recomputed from scratch at every story
# T: O(n^2) - n lego_castle calls, each running an O(n) width_of_castle chain; b = 1, so depth x work, not b^d
# S: O(n) - lego_castle frames plus width_of_castle frames on top, each at most n

def lego_castle(n):
    if n == 1:
        return 1

    def width_of_castle(story):
        if story == 1:
            return 1
        return width_of_castle(story - 1) * 2 + 1
    return lego_castle(n - 1) * 2 + width_of_castle(n)


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