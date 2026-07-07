# Intuition: for each item make one binary choice - buy it or skip it (0/1 subset selection).
#   Carry a running spent (price so far) and score (rating sum so far) down each path. At a leaf
#   (every item decided) compare score against the best seen; if it wins, snapshot picked.copy().
#   Guard the buy branch with the budget so an over-budget basket is never completed.
#   Unlike a "collect every node" problem, here we keep only the single max-scoring basket.
#
# Rigor checklist (reusable backtracking template):
#   State:  idx = item being decided; spent = price so far; score = rating so far; picked = indices chosen
#   Child:  two branches - skip (idx+1, unchanged) or buy (idx+1, spent+price, score+rating)
#   Prune:  spent + prices[idx] > budget -> don't take the buy branch
#   Leaf:   idx == n -> all decided; if score > best, snapshot picked.copy()
#   Work:   O(1) per node, O(n) to copy picked at a winning leaf
#
# n: number of items; up to 2^n baskets (n <= 15 -> <= 32768)
# T: O(n * 2^n) — 2^n leaves, plus an O(n) copy at each improving leaf
# S: O(n) recursion depth + O(n) best basket

def ikea_shopping(budget, prices, ratings):
    n = len(prices)
    picked = []            
    best_score = -1       
    best_picked = []  

    def visit(idx, spent, score):   # spent, score flow down each path
        nonlocal best_score, best_picked
        if idx == n:   # every item decided
            if score > best_score:
                best_score = score
                best_picked = picked.copy()
            return
        # Branch 1: skip item idx
        visit(idx + 1, spent, score)
        # Branch 2: buy item idx (only if it fits)
        if spent + prices[idx] <= budget:
            picked.append(idx)
            visit(idx + 1, spent + prices[idx], score + ratings[idx])
            picked.pop()

    visit(0, 0, 0.0)
    return best_picked


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