# Problem 38.11 - Boosting Days Multiple Times
# Given projected_sales and k total boosts (+1 each), same day can be boosted
# multiple times. Find max consecutive good days (>= 10).
#
# Example 1: projected_sales = [5,5,15,0,10], k = 12 -> 3
# Example 2: projected_sales = [5,5,15,0,10], k = 15 -> 4
# Example 3: projected_sales = [0,0,0], k = 29 -> 2
#
# Constraints:
# - 0 <= len(projected_sales) <= 10^5
# - 0 <= projected_sales[i] <= 10^3
# - 0 <= k <= 10^7