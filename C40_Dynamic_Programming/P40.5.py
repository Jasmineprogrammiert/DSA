# bust_ways(total) = # of card sequences (draws 1..10) that bust from sum `total`
#   -> > 21: busted (1) | 16..21: stand (0) | else: sum over next card, memoized
# answer = bust_ways(0)
# 
# Subproblems: O(1) — only totals 0..15 recurse (<= 16 states)
# Non-recursive work: O(1) — 10 fixed card branches
# T: O(1) — O(1) subproblems * O(1) work
# S: O(1) — memo holds <= 16 totals; recursion depth <= 16

def magic_blackjack():
    memo = {}

    def bust_ways(total):
        if total > 21:
            return 1
        if 16 <= total <= 21:
            return 0
        if total in memo:
            return memo[total]
        res = 0
        for card in range(1, 11):
            res += bust_ways(total + card)
        memo[total] = res
        return res

    return bust_ways(0)


# # Magic Blackjack

# You're given a magic deck of cards.
# When one card is removed, an identical card spawns as a replacement.
# Each card is a number between `1` and `10` (suits do not matter).
# When a card is drawn, each value from `1` to `10` has a `10%` chance of appearing.

# A dealer repeatedly draws cards until one of two things happen:

# - The sum of the cards is between `16` and `21`.
# - The sum of the cards exceeds `21`. When this happens, we say the dealer busts.

# Return the number of different ways the dealer can bust.

# For instance, if the dealer draws `10`, `2`, `10`, they bust.
# If they draw `2`, `10`, `10`, that counts as a different way to bust.
# If the dealer draws `10`, `1`, `10`, they don't bust.

# Constraints:

# - No input parameters (the problem has fixed parameters)