# Problem 33.4 - Lego Castle
# Build an n-story 2D Lego castle following these rules:
# - A 1-story castle is just a 1x1 block.
# - An n-story castle is made with two (n-1)-story castles, side by side,
#   one unit apart, with a row of blocks above them connecting them.
# Given n > 0, how many 1x1 blocks are needed?
#
# Example 1: n = 1 -> 1
# Example 2: n = 2 -> 5
# Example 3: n = 3 -> 17
# Example 4: n = 4 -> 49
# Example 5: n = 5 -> 129
#
# Constraints:
# - 1 <= n <= 57
# - Solution fits in a signed 64-bit integer