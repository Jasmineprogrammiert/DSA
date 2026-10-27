# Assign half the points to each center; return the minimum total Euclidean distance.

# 1. Start with all points at center1.
# 2. Sort by switching cost: d2 - d1.
# 3. Move the half with the lowest switching costs to center2.

# n: number of points
# T: O(n log n) - sorting dominates calculating distances and summing the total
# S: O(n) - ordered stores n points


# points = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# center1 = [0, 0]
# center2 = [1, 1]

# Output: 4
# We can assign [-1, 0] and [0, -1] to center1 and [0, 1] and [1, 0] to center2.

# Point      d1       d2       d2-d1    Assign
# [0, 1]      1        1         0       c2
# [1, 0]      1        1         0       c2
# [-1, 0]     1     sqrt(5)      >0       c1
# [0, -1]     1     sqrt(5)      >0       c1
#
# total = 1 + 1 + 1 + 1 = 4

import math


def center_assignment(points, c1, c2):
    def dist(p, c):
        horizontal_gap = p[0] - c[0]
        vertical_gap = p[1] - c[1]
        return math.sqrt(horizontal_gap ** 2 + vertical_gap ** 2)

    ordered = sorted(points, key=lambda p: dist(p, c2) - dist(p, c1))

    total = 0
    half = len(points) // 2
    for i, p in enumerate(ordered):
        if i < half:
            total += dist(p, c2)
        else:
            total += dist(p, c1)
    return total


# # Center Assignment

# You are given:

# 1. A list of points on a 2D plane, `points`, where each point is represented as `[x, y]` (floating-point coordinates). The list always contains an even number of points.
# 2. Two additional points, `center1` and `center2`, each also represented as `[x, y]`.

# Your task is to divide the points in `points` into two groups of equal size:

# - Assign half of the points to `center1`.
# - Assign the other half to `center2`.

# The goal is to minimize the sum of the (Euclidean) distance from each point to its assigned center. Return the sum of distances for an optimal assignment.

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/greedy-figure-7.png

# Example 1:
# points = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# center1 = [0, 0]
# center2 = [1, 1]

# Output: 4
# We can assign [-1, 0] and [0, -1] to center1 and [0, 1] and [1, 0] to center2.

# Example 2:
# points = [[0, 0], [0, 0]]
# center1 = [0, 0]
# center2 = [1, 1]

# Output: 1.414
# One of the points has to be assigned to center2, which is at distance sqrt(2) from [0, 0].

# Example 3:
# points = [[0, 0.5], [1, 0.5]]
# center1 = [0, 0]
# center2 = [1, 1]

# Output: 1

# Example 4:
# points = []
# center1 = [0.3, -3.3]
# center2 = [-1.6, 4.6]

# Output: 0

# Constraints:

# - `points.length` is even.
# - `0 <= points.length <= 10^5`.
# - All coordinates are between `-10^4` and `10^4`.
# - The answer should be a real-point within `10^-3` of the correct answer.