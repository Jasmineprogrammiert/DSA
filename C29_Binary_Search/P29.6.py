# need to find the index where the value of p2 is larger than p1

# traisition_point_recipe:
    # is_before() when p1[i] > p2[i]
    # l, r = 0, len.arr(p1)
    # handle three edge cases:
        # 1. the range is empty (not applicable)
        # 2. l is after (not applicable)
        # 3. r is before (not applicable)
    
    # where l and r are not next to each other (r - l > 1)
#        mid = (l + r) // 2
#        if is_before(mid):
#            l = mid
#        else:
#            r = mid
#    return l (last 'before'), r (first 'after'), or something else,
#    depending on the problem

# n: the length of p1 or p2
# T: O(log n) - binary search
# O: O(1)

def race_overtaking(p1, p2):
    def is_before(i):
        return p1[i] > p2[i]
    
    l, r = 0, len(p1) - 1
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    return r



# # Race Overtaking

# You are given two arrays of positive integers, `p1` and `p2`, representing players in a racing game. The two arrays are sorted, non-empty, and have the same length, `n`. The `i`-th element of each array corresponds to where that player was on the track at the `i`-th second of the race. We know that:

# 1. Player 1 started ahead (`p1[0] > p2[0]`)
# 2. Player 2 overtook player 1 _once_.
# 3. Player 2 remained ahead until the end (`p1[n - 1] < p2[n - 1]`).

# Assume the arrays have no duplicates, and that `p1[i] != p2[i]` for any index.

# Return the index at which player 2 overtook player 1.

# Example 1: p1 = [2, 4, 6, 8, 10], p2 = [1, 3, 5, 9, 11]
# Output: 3. At index 3, p2 (9) becomes greater than p1 (8).

# Example 2: p1 = [2, 3, 4, 5, 6], p2 = [1, 2, 3, 6, 7]
# Output: 3. At index 3, p2 (6) becomes greater than p1 (5).

# Example 3: p1 = [3, 4, 5], p2 = [2, 5, 6]
# Output: 1. At index 1, p2 (5) becomes greater than p1 (4).

# Constraints:

# - `2 ≤ p1.length = p2.length ≤ 10^6`
# - `0 ≤ p1[i], p2[i] ≤ 10^9`
# - `p1` and `p2` are strictly increasing
# - There is exactly one point where `p2` overtakes `p1`