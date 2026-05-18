# Problem 38.9 - Ad Campaign Boost
# Given projected_sales and k days to boost (+20 sales each), find the
# maximum consecutive good days (>= 10 sales) achievable.
#
# Example 1: projected_sales = [5,0,20,0,5], k = 2 -> 3
# Example 2: projected_sales = [0,10,0,10], k = 1 -> 3
# Example 3: projected_sales = [5,5,5], k = 3 -> 3
#
# Constraints:
# - 1 <= k <= len(projected_sales) <= 10^5
# - 0 <= projected_sales[i] <= 10^3