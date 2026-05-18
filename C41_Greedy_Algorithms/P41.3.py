# git commit -m "add: Chap. 41 Greedy Algorithms"


# Problem 41.3 - Center Assignment
# You are given:
# - A list of points on a 2D plane, points, where each point is [x, y]
#   (floating-point coordinates). The list always contains an even number of points.
# - Two additional points, center1 and center2, each also [x, y].
#
# Divide the points into two groups of equal size:
# - Assign half of the points to center1.
# - Assign the other half to center2.
#
# Minimize the sum of the Euclidean distance from each point to its assigned
# center. Return the sum of distances for an optimal assignment.
#
# Example 1:
# points = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# center1 = [0, 0], center2 = [1, 1]
# Output: 4
#
# Example 2:
# points = [[0, 0], [0, 0]]
# center1 = [0, 0], center2 = [1, 1]
# Output: 1.414
#
# Example 3:
# points = [[0, 0.5], [1, 0.5]]
# center1 = [0, 0], center2 = [1, 1]
# Output: 1
#
# Example 4:
# points = []
# center1 = [0.3, -3.3], center2 = [-1.6, 4.6]
# Output: 0
#
# Constraints:
# - points.length is even
# - 0 <= points.length <= 10^5
# - All coordinates are between -10^4 and 10^4
# - Answer should be within 10^-3 of the correct answer
