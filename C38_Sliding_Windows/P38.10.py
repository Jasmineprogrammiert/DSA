# Problem 38.10 - Ad Campaign With Small Boosts
# Given projected_sales, pick k days to boost by +5 (each day at most once).
# Find the maximum consecutive good days (>= 10).
#
# Example 1: projected_sales = [8,4,8], k = 3 -> 1
# Example 2: projected_sales = [10,5,8], k = 1 -> 2
# Example 3: projected_sales = [8,8,8], k = 3 -> 3
#
# Constraints:
# - 0 <= len(projected_sales) <= 10^5
# - 0 <= projected_sales[i] <= 10^3
# - 0 <= k <= len(projected_sales)