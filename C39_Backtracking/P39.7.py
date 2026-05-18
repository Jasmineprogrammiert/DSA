# Problem 39.7 - IKEA Shopping
# Given a budget, prices array, and ratings array, maximize the sum of style
# ratings without exceeding the budget. At most one of each item.
# Return array of indices to buy.
#
# Example 1:
# budget = 20, prices = [10,5,15,8,3], ratings = [7.0,3.5,9.0,6.0,2.0]
# Output: [0,3] (rating sum 13)
#
# Example 2:
# budget = 10, prices = [2,3,4,5], ratings = [1.0,2.0,3.5,4.0]
# Output: [2,3]
#
# Constraints:
# - n <= 15
# - budget <= 10^6
# - prices[i] <= 10^4
# - 0 <= ratings[i] <= 10