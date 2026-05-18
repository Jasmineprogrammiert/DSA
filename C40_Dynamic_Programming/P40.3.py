# Problem 40.3 - Restaurant Ratings
# Given ratings of n restaurants, maximize sum of ratings of places we stop.
# Constraint: can't stop at 2 consecutive restaurants.
#
# Example 1: ratings = [8,1,3,9,5,2,1] -> 19
# Example 2: ratings = [8,1,3,7,5,2,4] -> 20
# Example 3: ratings = [] -> 0
#
# Constraints:
# - 0 <= n <= 10^6
# - ratings[i] is a float between 0 and 10