# git commit -m "add: Chap. 41 Greedy Algorithms"


# Problem 41.6 - Time Traveler Max Year
# You are a time traveler trying to reach as far into the future as possible.
# In addition to letting time pass naturally, you can use a system to jump
# forward in time with constraints:
#
# - Jumping Points: The system can only jump to the next year specified in a
#   sorted list called jumping_points.
# - Jumps: You have a limited number of jumps k.
# - Maximum Aging: You want to avoid aging more than max_aging years naturally.
#
# Your starting point is the first year in jumping_points. Return the latest
# year you can reach without exceeding the max_aging limit.
#
# Example 1:
# jumping_points = [2020, 2024], k = 0, max_aging = 2
# Output: 2022
#
# Example 2:
# jumping_points = [2020, 2024], k = 1, max_aging = 1
# Output: 2025
#
# Example 3:
# jumping_points = [1803, 1861, 1863, 1865, 1920, 1929, 1941, 1964, 2001, 2021]
# k = 4, max_aging = 45
# Output: 2021
#
# Example 4:
# jumping_points = [1, 10, 30], k = 1, max_aging = 5
# Output: 15
#
# Example 5:
# jumping_points = [1, 3, 6, 7, 11, 16, 17, 19], k = 2, max_aging = 4
# Output: 12
#
# Constraints:
# - 0 <= k <= n-1
# - 0 < max_aging <= 10^9
# - 2 <= jumping_points.length <= 10^5
# - 0 <= jumping_points[i] <= 10^9
# - jumping_points is sorted in ascending order (no duplicates)
