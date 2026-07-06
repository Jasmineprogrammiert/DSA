# =============================== Approach 1 ===============================
# Top-down memoization (recursive, cached)
#
#   times=[8,1,2,3,9,6,2,4] (n=8), base = last 3 stops (5,6,7) coast to end:
#   Phase 1 - DIVE: rec(0) can't answer, so it keeps calling inward to a base:
#     rec(0)->rec(1)->rec(2)->rec(3)->rec(4)->rec(5)=6  (base times[5])
#                                           ->rec(6)=2, rec(7)=4  (base)
#   Phase 2 - FILL on the way back up (each return stores like a dp cell):
#     rec(4)=9+min(6,2,4)=11   -> memo{4:11}
#     rec(3)=3+min(11,6,2)=5   -> memo{4:11, 3:5}
#     rec(2)=2+min(5,11,6)=7   -> memo{..., 2:7}
#     rec(1)=1+min(7,5,11)=6   -> memo{..., 1:6}
#     rec(0)=8+min(6,7,5)=13   -> memo{..., 0:13}
#   Phase 3 - repeats are free: rec(1), rec(2) already in memo -> instant hits.
#   Answer = min(13, 6, 7) = 6.
#
# n: number of rest stops
# Subproblems: n — one per stop i
# Non-recursive work: O(1) — min over 3 fixed next choices
# T: O(n) — n subproblems * O(1) work
# S: O(n) — memo holds up to n entries + recursion stack up to n deep
# (recurses ~n deep, so RecursionError at n = 10^6 — do not use here)

def delay_memoized(times):
    n = len(times)
    if n <= 2:
        return 0

    memo = {}
    def delay_rec(i):
        if i >= n - 3:
            return times[i]
        if i in memo:
            return memo[i]
        memo[i] = times[i] + min(delay_rec(i + 1),
                                 delay_rec(i + 2),
                                 delay_rec(i + 3))
        return memo[i]

    return min(delay_rec(0), delay_rec(1), delay_rec(2))


# =============================== Approach 2 ===============================
# Bottom-up tabulation (fill an array instead of recursing)
#
#   Same table as memoization (dp[i] == memo[i]); only the fill order differs:
#   tabulation you pick it, memoization recursion discovers it.
#   dp[i] reads only 3 cells -> keep 3 rolling vars, not the whole array: O(n)->O(1).
#   Three variants below; each has its own trace right above it.
#
# Subproblems: n — one per stop (dp[i])
# Non-recursive work: O(1) — min over 3 fixed cells
# T: O(n) — n subproblems * O(1) work
# S: O(n) full array, or O(1) with 3 rolling vars


# --- front-to-back variant (the a,b,c version below): mirror direction ---
#   Flip the view: cur at stop i = min detour from the START, ending at stop i
#   -> looks at the 3 cells BEHIND, fills LEFT-TO-RIGHT.
#   a=b=c=0 = 3 free "virtual stops" before the start, so stops 0/1/2 can each
#   open a plan for free. Answer = min of the LAST 3 stops.
#
#   times=[8,1,2,3,9,6,2,4]:      a   b   c    cur = t + min(a,b,c)
#     start:                      0   0   0
#     stop0: 8+min(0,0,0)=8   -> (0,0,8)
#     stop1: 1+min(0,0,8)=1   -> (0,8,1)
#     stop2: 2+min(0,8,1)=2   -> (8,1,2)
#     stop3: 3+min(8,1,2)=4   -> (1,2,4)
#     stop4: 9+min(1,2,4)=10  -> (2,4,10)
#     stop5: 6+min(2,4,10)=8  -> (4,10,8)
#     stop6: 2+min(4,10,8)=6  -> (10,8,6)
#     stop7: 4+min(10,8,6)=10 -> (8,6,10)
#   answer = min(a,b,c) = min(8,6,10) = 6.
#
#   vs back-to-front (below): that measures stop i -> END (suffix); this measures
#   START -> stop i (prefix). Same trip, opposite halves, same answer.

def road_trip(times):
    n = len(times)
    if n <= 2:
        return 0

    a = b = c = 0
    for t in times:
        cur = t + min(a, b, c)
        a, b, c = b, c, cur
    return min(a, b, c)


# --- full array (back-to-front): dp[i] from the 3 cells AHEAD ---
#   dp[i] = min detour from stop i to end; reads the 3 cells AHEAD,
#   so fill RIGHT-TO-LEFT. times=[8,1,2,3,9,6,2,4] (n=8):
#     base (last 3):  dp = [_, _, _, _, _, 6, 2, 4]   (dp[5..7] = times[5..7])
#     i=4: 9+min(6,2,4)=11   dp = [_,_,_,_,11,6,2,4]
#     i=3: 3+min(11,6,2)=5   dp = [_,_,_,5,11,6,2,4]
#     i=2: 2+min(5,11,6)=7   dp = [_,_,7,5,11,6,2,4]
#     i=1: 1+min(7,5,11)=6   dp = [_,6,7,5,11,6,2,4]
#     i=0: 8+min(6,7,5)=13   dp = [13,6,7,5,11,6,2,4]
#   Answer = min(dp[0],dp[1],dp[2]) = min(13,6,7) = 6.

def road_trip(times):
    n = len(times)
    if n <= 2:
        return 0

    dp = [0]*n
    dp[n-1], dp[n-2], dp[n-3] = times[n-1], times[n-2], times[n-3]
    for i in range(n-4, -1, -1):
        dp[i] = times[i] + min(dp[i+1], dp[i+2], dp[i+3])
    return min(dp[0], dp[1], dp[2])


# --- space optimization: rolling 3 vars (O(n) -> O(1)) ---
#   Each dp[i] reads only dp[i+1..i+3] (the 3 cells ahead). Past them the older
#   cells are dead weight -> only 3 are ever live. Keep them as a sliding window
#   (dp1, dp2, dp3) instead of the whole array.
#
#   times=[8,1,2,3,9,6,2,4]:      dp1 dp2 dp3  = which dp cells
#     start (i=4 next):             6   2   4    dp[5..7]
#     i=4: cur=9+min(6,2,4)=11 ; slide -> 11  6  2   dp[4..6]
#     i=3: cur=3+min(11,6,2)=5 ; slide ->  5 11  6   dp[3..5]
#     i=2: cur=2+min(5,11,6)=7 ; slide ->  7  5 11   dp[2..4]
#     i=1: cur=1+min(7,5,11)=6 ; slide ->  6  7  5   dp[1..3]
#     i=0: cur=8+min(6,7,5)=13 ; slide -> 13  6  7   dp[0..2]
#   answer = min(dp1,dp2,dp3) = min(13,6,7) = 6   (same numbers as the array)
#
#   slide  dp1,dp2,dp3 = cur,dp1,dp2 : new cell in front, shift right, drop the
#   3-ahead cell (never needed again). Same T; space O(n) -> O(1).

def road_trip(times):
    n = len(times)
    if n <= 2:
        return 0

    dp1, dp2, dp3 = times[n-3], times[n-2], times[n-1]
    for i in range(n-4, -1, -1):
        cur = times[i] + min(dp1, dp2, dp3)
        dp1, dp2, dp3 = cur, dp1, dp2
    return min(dp1, dp2, dp3)


# # Road Trip

# We are driving down a road with `n` rest stops between us and our destination. For each rest stop, our mapping software tells us how long of a detour it would be to stop there. We start before the first rest stop and our destination is past the last one.

# We are given an array of `n` positive integers, `times`, indicating the delay incurred to stop at each rest stop. If we don't want to go more than 2 rest stops without taking a break, what's the least amount of time we have to spend on detours?

# Example 1:
# times = [8, 1, 2, 3, 9, 6, 2, 4]
# Output: 6. The optimal rest stops are: [8, *1*, 2, *3*, 9, 6, *2*, 4]

# Example 2:
# times = [8, 1, 2, 3, 9, 3, 2, 4]
# Output: 5. The optimal rest stops are: [8, 1, *2*, 3, 9, *3*, 2, 4]

# Example 3:
# times = [10, 10]
# Output: 0. We don't need to make any stops.

# Example 4:
# times = [10]
# Output: 0. We don't need to make any stops.

# Example 5:
# times = []
# Output: 0. We don't need to make any stops.

# Check out the figure below for an illustration of the first example:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/road-trip-1.png

# Constraints:

# - `n` is at least `0` and at most `10^6`.
# - `times[i]` is at least `1` and at most `10^3`.