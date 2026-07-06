# same as 40.1 but up to k skips in a row -> window of last k+1 dp states
#   dp[i] = times[i] + min(dp[i-1 .. i-k-1])
# deque(maxlen=k+1) auto-drops the stale state; answer = min over the window
#
# n: number of rest stops
# k: max consecutive stops allowed to skip
# Subproblems: n — one per stop (dp[i])
# Non-recursive work: O(k) — min over the k+1 wide window
# T: O(n * k) — n subproblems * O(k) work
# S: O(k) — deque holds a k+1 wide window (not the full table)

from collections import deque


def road_trip(times, k):
    window = deque([0] * (k + 1), maxlen=k + 1)
    for t in times:
        cur = t + min(window)
        window.append(cur)
    return min(window)

# top-down: delay(i) = least detour if stop i is the next stop we take
#   delay(i) = times[i] + min(delay(i+1 .. i+k+1))  -> skip at most k before next
# base: i >= n      -> 0        (coasted past the last stop)
#       i >= n-k-1  -> times[i] (<= k stops left, so coast to the end from here;
#                                times are +ve, so never worth taking more)
# answer: min(delay(0 .. k))    -> skip at most k before the first stop
#
# n: number of rest stops
# k: max consecutive stops we can skip
# Subproblems: n — one per stop i
# Non-recursive work: O(k) — min over k+1 next choices
# T: O(n * k) — n subproblems * O(k) work
# S: O(n) — memo up to n entries + recursion depth

def road_trip_memo(times, k):
    n = len(times)
    memo = {}

    def delay(i):
        if i >= n:
            return 0
        if i >= n - k - 1:  # n-k-1: the first idx from which only k stops remain
            return times[i]
        if i not in memo:
            # p walks 1..k+1 (skip 0..k stops), so next stop = i+p
            # delay(i+p) = cost of continuing from each legal next stop
            # take times[i] + the cheapest of those continuations
            memo[i] = times[i] + min(delay(i + p) for p in range(1, k + 2))
        return memo[i]

    return min(delay(p) for p in range(k + 1))


# # Minivan Road Trip

# We are driving down a road with `n` rest stops between us and our destination. For each rest stop, our mapping software tells us how long of a detour it would be to stop there. We start before the first rest stop and our destination is past the last one.

# We are given an array of `n` positive integers, `times`, indicating the delay incurred to stop at each rest stop. We are also given a positive integer `k`, indicating the number of consecutive rest areas we can skip.

# If we don't want to go more than `k` rest stops without taking a break, what's the least amount of time we have to spend on detours?

# Example 1:
# times = [8, 1, 2, 3, 9, 6, 2, 4]
# k = 2
# Output: 6.
# The optimal rest stops are: [8, *1*, 2, *3*, 9, 6, *2*, 4].

# Example 2:
# times = [8, 1, 2, 3, 9, 6, 2, 4]
# k = 3
# Output: 4
# The optimal rest stops are: [8, 1, *2*, 3, 9, 6, *2*, 4].

# Example 3:
# times = [10, 10]
# k = 2
# Output: 0

# Constraints:

# - `n` is at least `0` and at most `1000`.
# - `times[i]` is at least `1` and at most `1000`.
# - `k` is at least `1` and at most `1000`.