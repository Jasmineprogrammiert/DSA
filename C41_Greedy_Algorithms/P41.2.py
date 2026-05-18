# git commit -m "add: Chap. 41 Greedy Algorithms"


# Problem 41.2 - Time Traveler
# You are a time traveler stuck in the past trying to reach a future point.
# In addition to letting time pass naturally, you can use an emergency system
# to jump forward in time with constraints:
#
# - Jumping Points: The system can only jump to the next year specified in a
#   sorted list called jumping_points.
# - Jumps: You have a limited number of jumps k, which lets you instantly move
#   forward to the next jumping point. Once out of jumps, you must live through
#   the years naturally.
# - Maximum Aging: You want to avoid aging more than max_aging years naturally.
#
# Your starting point is the first year in jumping_points and your goal is to
# reach the last year in the list. Return whether you can reach the final
# jumping point without exceeding the max_aging limit.
#
# Example 1:
# jumping_points = [2020, 2024], k = 0, max_aging = 3
# Output: False
# No jumps, aging naturally from 2020 to 2024 would take 4 years.
#
# Example 2:
# jumping_points = [2020, 2024], k = 1, max_aging = 1
# Output: True
# Use the jump to go from 2020 to 2024, aging 0 years.
#
# Example 3:
# jumping_points = [1803, 1861, 1863, 1865, 1920, 1929, 1941, 1964, 2001, 2021]
# k = 4, max_aging = 45
# Output: True
#
# Constraints:
# - 0 <= k <= n-1
# - 0 < max_aging <= 10^9
# - 2 <= jumping_points.length <= 10^5
# - 0 <= jumping_points[i] <= 10^9
# - jumping_points is sorted in ascending order (no duplicates)
