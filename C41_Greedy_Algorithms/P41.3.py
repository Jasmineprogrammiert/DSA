# Greedy: everyone prefers whichever center is nearer, but exactly half must
# go to each -- so rank points by how much they lean toward C2 vs C1.
#   -> forward lean = d2 - d1: how much closer a point is to C1 than to C2
#      negative -> nearer C2, so it leans toward (prefers) C2
#      positive -> nearer C1, so it leans toward (prefers) C1
#   -> sort by forward lean ascending: strongest C2-preferrers first, C1-preferrers last
#   -> send the front half to C2, keep the back half at C1
#   -> cutting the sorted list in half gives the equal sizes for free
#
# n: number of points
# T: O(n log n) — sort dominates
# S: O(n) — the scored list

import math


def minimize_center_distance(points, c1, c2):
    def dist(p, c):
        # math.hypot(dx, dy) = sqrt(dx^2 + dy^2), the straight-line distance
        return math.hypot(p[0] - c[0], p[1] - c[1])

    scored = []
    for p in points:
        d1, d2 = dist(p, c1), dist(p, c2)
        scored.append((d2 - d1, d1, d2))  # one tuple: (lean, dist to C1, dist to C2)
    scored.sort()

    total = 0
    half = len(points) // 2
    for i, (_, d1, d2) in enumerate(scored):
        if i < half:
            total += d2   # most C2-leaning half -> C2
        else:
            total += d1   # the rest stay at C1
    return total


# Alt approach: assign each point to its nearer center for a baseline, then rebalance.
#   -> one side may be overloaded (more than half the points)
#   -> move the cheapest-to-switch points from the overloaded side
#      until both halves are equal
#   -> same O(n log n), more branches
#
# T: O(n log n) — sort the overloaded side's switch costs
# S: O(n) — the switch-cost list


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