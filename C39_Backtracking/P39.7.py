# budget = 20
# 0  1 2  3 4       INDEX
# 10 5 15 8 3       PRICES
# 7  3 9  6 2       RATINGS

# i = 5
# buy = [4]
# spent = 3
# score = 2
# best_buy = [4]
# best_score = 2

# maximizing the sum of style ratings of the items we buy
# don't want to pick more than one of each item

# Return an array with the indices of the items that we should buy.


# Each item: skip, or buy if it fits (append -> recurse -> pop)
# At i == n: copy buy if score improves; return best_buy

# n: number of items
# T: O(n * 2^n) - up to 2^n baskets, O(n) to copy each improving basket
# S: O(n) - call stack, buy and best_buy each hold at most O(n)

def ikea_shopping(budget, prices, ratings):
    buy = []
    best_buy = []
    best_score = 0

    def visit(i, spent, score):
        nonlocal best_buy, best_score

        if i == len(prices):
            if score > best_score:
                best_score = score
                best_buy = buy.copy()
            return

        visit(i + 1, spent, score)

        if spent + prices[i] <= budget:
            buy.append(i)
            visit(i + 1, spent + prices[i], score + ratings[i])
            buy.pop()

    visit(0, 0, 0)
    return best_buy


# # IKEA Shopping

# A magazine has rated every IKEA item from 1 to 10 in terms of style. We have gone to IKEA with a limited budget and the goal of maximizing the sum of style ratings of the items we buy. We also don't want to pick more than one of each item. We are given 3 things:

# - `budget`, a positive integer,
# - `prices`, an array of `n` positive integers,
# - `ratings`, an array of `n` positive floating-point numbers between `0` and `10` (inclusive).

# There are `n` items. Item `i` has price `prices[i]` and style rating `ratings[i]`. Return an array with the indices of the items that we should buy.

# Example 1:
# budget = 20
# prices =  [10,  5,   15,  8,   3]
# ratings = [7.0, 3.5, 9.0, 6.0, 2.0]
# Output: [0, 3]. With items 0 and 3, we get a rating sum of 13 without exceeding the budget.

# Example 2:
# budget = 10
# prices =  [2,   3,   4,   5]
# ratings = [1.0, 2.0, 3.5, 4.0]
# Output: [2, 3]

# Constraints:

# - `n <= 15`
# - `budget <= 10^6`
# - `prices[i] <= 10^4` for all `i`
# - `ratings[i]` is a floating-point number between `0` and `10` (inclusive)