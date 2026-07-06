# Signature: num_steps(i) — one arg: the current value
# Description: min ops to reduce the value n down to 1
# Base case: n == 1 -> 0  (already there; n never drops below 1)
# General case:
#   choices: subtract 1 (always); //2 if n % 2 == 0; //3 if n % 3 == 0
#   subproblems: each move lands on a smaller value -> f(n-1), f(n//2), f(n//3)
#   recurse: cost of a move = 1 (the step) + f(that value)
#   aggregate: min over legal moves (minimization problem)
# Original: answer = f(n) directly; subproblem IS the original shape
# DP: overlapping subproblems (f(3), f(4)... recomputed) -> memoize, each of 1..n solved once
# 
# Subproblems: n — one per value 1..n
# Non-recursive work: O(1) — min over <= 3 fixed moves
# T: O(n) — n subproblems * O(1) work
# S: O(n) — memo up to n entries + recursion stack (depth up to n)


def min_step_to_one(n):
    memo = {}

    def num_steps(i):
        if i == 1:
            return 0
        if i in memo:
            return memo[i]

        best = num_steps(i - 1)
        if i % 2 == 0:
            best = min(best, num_steps(i // 2))
        if i % 3 == 0:
            best = min(best, num_steps(i // 3))

        memo[i] = 1 + best
        return memo[i]

    return num_steps(n)


# # Minimum Steps to One

# Write a function that accepts a positive integer, `n`, and returns the minimum number of operations to get to `1`, assuming we can choose between the following operations:

# - Subtract `1`.
# - Divide by `2`. We can only do this if the number is divisible by `2`.
# - Divide by `3`. We can only do this if the number is divisible by `3`.

# Example 1:
# n = 10
# Output: 3. We can do 10 -> 9 -> 3 -> 1.

# Example 2:
# n = 1
# Output: 0

# Example 3:
# n = 15
# Output: 4

# Constraints:

# - `n` is at least `1` and at most `10^6`.