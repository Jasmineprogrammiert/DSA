# Greedy: sweep points left to right, jump the k largest gaps seen so far.
#   -> min-heap holds the jumped gaps; push each gap, pop smallest if size > k
#   -> aged = total gaps so far - heap sum (popped gaps are the ones we age)
#   -> when aged would exceed max_aging, stop; answer = that point + leftover
#
#   for each gap:
#       remember cost-to-reach-here      # aged
#       pretend we jump this gap          # push to heap
#       if we've jumped too many (> k):
#           un-jump the smallest one      # pop -> age it instead
#       if aging now blows the budget:
#           stop, walk the leftover       # return point + leftover
#
# n: number of jumping points
# k: number of jumps allowed
# T: O(n log k) — one pass, heap ops are O(log k)
# S: O(k) — the heap

import heapq

def latest_reachable_year(jumping_points, k, max_aging):
    gaps = []
    for i in range(1, len(jumping_points)):
        gaps.append(jumping_points[i] - jumping_points[i - 1])

    jumped_gaps = []
    total_years = 0
    jumped_years = 0
    for i, gap in enumerate(gaps):
        aged = total_years - jumped_years
        heapq.heappush(jumped_gaps, gap)
        jumped_years += gap
        total_years += gap
        if len(jumped_gaps) > k:
            jumped_years -= heapq.heappop(jumped_gaps)
        new_aged = total_years - jumped_years
        if new_aged > max_aging:
            return jumping_points[i] + (max_aging - aged) # stuck -> exit early

    aged = total_years - jumped_years
    return jumping_points[-1] + max_aging - aged # loop ended: spend the remaining ages


# Binary search (slower): reachability is monotonic, so binary search the point.
#   -> can_reach(i)? jump k largest gaps before i, age the rest, fits budget?
#   -> yes -> l = mid (go further); no -> r = mid; until l, r adjacent
#   -> answer = last reachable point + leftover budget
#
#   l, r = 0, n - 1
#   while r - l > 1:
#       mid = (l + r) // 2
#       if can_reach(mid): l = mid   # reachable -> go further
#       else:              r = mid   # not -> pull back
#   -> l is the last reachable point
#
# T: O(n log n) — O(n) check per guess, O(log n) guesses
# S: O(n) — sorted gaps


# # Time Traveler Max Year

# You are a time traveler who is trying to reach as far into the future as possible. In addition to just letting time pass naturally, you can use a system to jump forward in time -- but there are constraints:

# - **Jumping Points:** The system can only jump to the next year specified in a sorted list called `jumping_points`.
# - **Jumps:** You have a limited number of jumps `k`, which lets you instantly move forward to the next jumping point of your choice. Once you're out of jumps, you must live through the years naturally.
# - **Maximum Aging:** You want to avoid aging more than a certain limit, `max_aging`, which is the total number of years you live naturally during your journey.

# Your starting point is the first year in `jumping_points` and your goal is to reach as far into the future as possible. To achieve this, you can use any mix of:

# - Jumping to the next jumping point instantaneously (up to a limit of `k` jumps).
# - Let time pass naturally.

# Return the latest year you can reach without exceeding the `max_aging` limit.

# Example 1:
# jumping_points = [2020, 2024]
# k = 0
# max_aging = 2

# Output: 2022.
# We don't have jumps, so we age naturally from 2020 to 2022.

# Example 2:
# jumping_points = [2020, 2024]
# k = 1
# max_aging = 1

# Output: 2025.

# Example 3:
# jumping_points = [1803, 1861, 1863, 1865, 1920, 1929, 1941, 1964, 2001, 2021]
# k = 4
# max_aging = 45

# Output: 2021.
# We start at 1803. We use our first jump to get to 1861. We let time flow naturally for four years, carrying us to 1865. We use our second jump to fast forward to 1920. We bide our time until 1941. The third jump takes us to 1964, and we jump again immediately to 2001. Out of jumps, we endure the final stretch of 20 long years. In total, we have aged 4 + 9 + 12 + 20 = 45 years, the maximum we could afford.

# Example 4:
# jumping_points = [1, 10, 30]
# k = 1
# max_aging = 5

# Output: 15

# Example 5:
# jumping_points = [1, 3, 6, 7, 11, 16, 17, 19]
# k = 2
# max_aging = 4
# Output: 12

# Constraints:

# - `0 ≤ k ≤ n-1`
# - `0 < max_aging ≤ 10^9`
# - `2 ≤ jumping_points.length ≤ 10^5`
# - `0 ≤ jumping_points[i] ≤ 10^9`
# - The list of jumping points is sorted in ascending order (no duplicates).