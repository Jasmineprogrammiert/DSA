# Problem 38.17 - Strong Start and Ending
# Given projected_sales and k days to boost (+20), maximize the combined
# count of initial consecutive good days + final consecutive good days.
# Good day >= 10 sales.
#
# Example 1: projected_sales = [10,0,0,0,10,0,0,10], k = 2 -> 5
# Example 2: projected_sales = [0,10,0,10], k = 1 -> 3
# Example 3: projected_sales = [5,5,5], k = 2 -> 2
#
# Constraints:
# - 0 <= len(projected_sales) <= 10^5
# - 0 <= projected_sales[i] <= 10^3
# - 0 <= k <= 10^5