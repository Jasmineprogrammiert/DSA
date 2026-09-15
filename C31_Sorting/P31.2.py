# 1. There is a single circle.
# 2. One circle completely surrounds all the others (without touching boundaries), and the other circles are themselves _nested_ (this is a recursive definition).
# If 1 and 2: True. else False

# sort by radius, biggest first -> contains is transitive, check neighbouring pairs only
# inside: d + r < R (strict, touching fails), d = sqrt(dx^2 + dy^2) between centres
# trap: axis shadows (x +- r) are not containment

# n: length of circles
# T: O(n log n) - the sort dominates; the loop iterates the n - 1 neighbouring pairs once, O(1) each
# S: O(n) - Timsort uses up to O(n) extra space; the loop itself is O(1)

import math

def nested_circles(circles):
    if len(circles) == 1:
        return True
    circles.sort(key=lambda circle: circle[1], reverse=True)
    for i in range(len(circles) - 1):
        (x1, y1), r1 = circles[i]
        (x2, y2), r2 = circles[i + 1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if distance + r2 >= r1:
            return False
    return True

    
# # Nested Circles

# You are given a non-empty array of circles, `circles`, where each circle is specified by its center coordinates `(x, y)` and its radius `r`. Your task is to determine whether the circles are _nested_. For the circles to be considered nested, one of the following conditions must be met:

# 1. There is a single circle.
# 2. One circle completely surrounds all the others (without touching boundaries), and the other circles are themselves _nested_ (this is a recursive definition).

# Write a function that returns a boolean indicating whether the circles are nested.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/sorting-figure-5.png

# Example 1: circles = [
#     ((4, 4), 5),  # Circle with center (4, 4) and radius 5
#     ((8, 4), 2)   # Circle with center (8, 4) and radius 2
# ]
# Output: false. Neither circle is surrounded by the other.

# Example 2: circles = [
#     ((5, 3), 3),
#     ((5, 3), 2),
#     ((4, 4), 5)
# ]
# Output: true. The third circle contains all the first and second circles, and the first circle contains the second circle.

# Example 3: circles = [((5, 3), 3)]
# Output: true. A single circle is considered nested.

# Constraints:

# - The length of circles is at most 10^4
# - All coordinates and radii are integers between -10^4 and 10^4