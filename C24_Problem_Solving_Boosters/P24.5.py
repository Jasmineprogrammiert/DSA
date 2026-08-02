# case 1: balls of one color => that color
# case 2: balls of all three colors => every color
#       (merge same-color balls down to one each, then case 3a in any order)
# case 3: balls of exactly two colors
#       -> both counts == 1 => the 3rd (absent) color
#       -> both counts >= 2 => every color (merge the two => case 2)
#       -> one count == 1, other >= 2 => every color except the one with count >= 2

# T: O(1) - balls is always 3 pairs; every pass is a fixed 3 steps independent of how large r, g, b get
# S: O(1) - present/big hold at most 3 letters

def magic_balls(r, g, b):
    balls = [('R', r), ('G', g), ('B', b)]
    
    present = [ball for ball, n in balls if n >= 1]
    big = [ball for ball, n in balls if n >= 2]
    
    if len(present) == 1:
        return present[0]
    if len(present) == 3:
        return "BGR"
    
    if len(big) == 0:
        absent = [ball for ball, n in balls if n == 0]
        return absent[0]
    if len(big) == 2:
        return "BGR"
    return "".join(sorted(ball for ball, _ in balls if ball != big[0]))


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