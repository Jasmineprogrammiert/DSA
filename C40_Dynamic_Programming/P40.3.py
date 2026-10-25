# maximizing the sum of ratings of the places to stop
# don't want to stop at 2 consecutive restaurants
# Return the optimal sum of ratings.

# IDX           0  1   2   3   4   5   6
# RATINGS       8  1   3   9   5   2   1

# a             0  8   8  11  17  17  19
# b             8  8  11  17  17  19  19
# curr          8  8  11  17  17  19  19

# n: number of restaurants
# T: O(n) - one pass, O(1) work per restaurant
# S: O(1) - a fixed number of variables

def restaurant_ratings(ratings):
    a = b = 0
    for rating in ratings:
        curr = max(b, rating + a)
        a, b = b, curr
    return b


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