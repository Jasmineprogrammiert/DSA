# # Magic Balls

# A magician has R red balls, G green balls, and B blue balls. The balls are magic because when two of them touch, they transform into a single ball:

# - Two balls of the same color become one ball of that color.
# - Two balls of different colors become a ball of the third color.

# If the magician starts with at least one ball and starts transforming balls until there is a single ball left, what are the possible colors of the final ball? Return a string with a character for each possible color ('R', 'G', and 'B').

# Example: R = 4, G = 0, B = 0
# Output: "R". We only have red balls, so combining them can only result in more red balls.

# Example: R = 2, G = 1, B = 0
# Output: "BG".

# The below figure illustrates example 2.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/magic-balls-1.png

# With two red balls and one green ball, we can end up with a blue ball or a green ball.

# Constraints:

# - `0 <= R, G, B <= 10^9` (number of red, green, and blue balls respectively)
# - `R + G + B >= 1` (at least one ball total)