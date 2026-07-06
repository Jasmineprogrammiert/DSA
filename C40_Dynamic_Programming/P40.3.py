# dp[i] = best rating sum over first i restaurants, no 2 consecutive stops
#   cur = max(skip i -> dp[i-1],  take i -> ratings[i] + dp[i-2])
# roll 2 vars a = dp[i-2], b = dp[i-1]; answer = b
#
# n: number of restaurants
# Subproblems: n — one per restaurant (dp[i])
# Non-recursive work: O(1) — max over 2 fixed choices
# T: O(n) — n subproblems * O(1) work
# S: O(1) — two rolling vars (a, b), not the full table

def resto_ratings(ratings):
    a = b = 0
    for r in ratings:
        cur = max(b, r + a)
        a, b = b, cur
    return b

# top-down: rating_sum(i) = best extra rating collectible from restaurants i..n-1
#   i = next restaurant we're deciding on (not one we've committed to eat at)
#   rating_sum(i) = max(skip i -> rating_sum(i+1),
#                       take i -> ratings[i] + rating_sum(i+2))  -> take blocks i+1
# base: i >= n -> 0 (walked past the last restaurant, no rating left to add)
# memo caches each i once; answer = rating_sum(0)
#
# n: number of restaurants
# Subproblems: n — one per restaurant i
# Non-recursive work: O(1) — max over 2 fixed choices
# T: O(n) — n subproblems * O(1) work
# S: O(n) — memo up to n entries + recursion depth

def restaurant_ratings(ratings):
    n = len(ratings)
    memo = {}

    def rating_sum(i):  # best extra rating collectible from i onward
        if i >= n:
            return 0  # nothing left to eat -> 0 rating to add
        if i in memo:
            return memo[i]
        memo[i] = max(rating_sum(i + 1), ratings[i] + rating_sum(i + 2))
        return memo[i]

    return rating_sum(0)


# # Restaurant Ratings

# We are doing a road trip and trying to plan where to stop to eat. There are `n` restaurants along the route. We are given an array, `ratings`, with the ratings of all the restaurants maximizing the sum of ratings of the places where we stop. The only constraint is that we don't want to stop at 2 consecutive restaurants, as we would be too full. Return the optimal sum of ratings.

# Example 1:
# ratings = [8, 1, 3, 9, 5, 2, 1]
# Output: 19. The optimal restaurants are: [*8*, 1, 3, *9*, 5, *2*, 1]

# Example 2:
# ratings = [8, 1, 3, 7, 5, 2, 4]
# Output: 20. The optimal restaurants are: [*8*, 1, *3*, 7, *5*, 2, *4*].

# Example 3:
# ratings = []
# Output: 0

# Constraints:

# - `n` is at least `0` and at most `10^6`.
# - `ratings[i]` is a floating-point number between `0` and `10` (inclusive).