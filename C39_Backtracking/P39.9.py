# Count DISTINCT sum-0 submultisets -> group into {number: count}, then per distinct number pick
#   how many copies to take (k = 0..count). Choosing quantities, not positions, builds no duplicate.
#   Count is an UP quantity: visit() returns its subtree's sum-0 leaf count, parents sum children.
#
# Tree for S = [1, 1, -1, -1]  ->  values = [(1, 2), (-1, 2)]. Pick #1s, then #(-1)s; sum = #1s - #(-1)s:
#
#   0 ones ─┬─ 0 neg → {}            0  *
#           ├─ 1 neg → {-1}         -1
#           └─ 2 neg → {-1,-1}      -2
#   1 one  ─┬─ 0 neg → {1}           1
#           ├─ 1 neg → {1,-1}        0  *
#           └─ 2 neg → {1,-1,-1}    -1
#   2 ones ─┬─ 0 neg → {1,1}         2
#           ├─ 1 neg → {1,1,-1}      1
#           └─ 2 neg → {1,1,-1,-1}   0  *
#
#   3 x 3 = 9 submultisets (one per leaf, no duplicates); 3 sum to 0 (*) -> answer 3.
#
# n: length of S
# T: O(2^n) — worst case all-distinct (branch 2, depth n); duplicates only shrink the tree
# S: O(n) — call stack depth + frequency map

from collections import Counter


def count_unique_submultisets(S):
    values = list(Counter(S).items())   # (number, count) pairs, looked up once

    def visit(idx, cur_sum):
        if idx == len(values):          # every distinct number decided
            if cur_sum == 0:
                return 1
            return 0
        val, count = values[idx]
        total = 0
        for k in range(count + 1):      # take k copies of this number
            total += visit(idx + 1, cur_sum + k * val)
        return total

    return visit(0, 0)


# # Count Unique Submultisets With Sum Zero

# A _multiset_ is a set that allows repeated elements. A _submultiset_ of a multiset `S` is another multiset obtained by removing any number of elements from `S`.

# We are given an array with `n` integers representing a multiset (it can have duplicates).

# Return the number of **unique** submultisets of `S` with sum `0`, ignoring which position in `S` the values came from.

# Example 1: S = [1, 1, -1, -1]
# Output: 3. The unique submultisets with sum 0 are [], [1, 1, -1, -1] and [1, -1]. The last one can be obtained in more than one way.

# Example 2: S = []
# Output: 1. [] is a submultiset of [] with sum 0.

# Example 3: S = [-1, 2, 1, 0, 3]
# Output: 4. The unique submultiset with sum 0 are [-1, 1], [-1, 1, 0], [0], and [].

# Constraints:

# - The length of `S` is at most `20`.
# - The elements in `S` are integers.