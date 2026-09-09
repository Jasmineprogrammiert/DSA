# intersection: the set of elements that appears in every set
# Return the index of the set that should be excluded to maximize intersection
# tie -> return the smallest index


# in all k sets          -> in every answer, doesn't help choose
# in exactly k-1         -> votes for the ONE set it's missing from
# in fewer than k-1      -> never in, ignore

# sets = [[1, 2, 3], [3, 2, 1], [1, 4, 5], [1, 2]]
#
# Loop 1 - build freq_map, one (count, seen_idx_sum) per element:
#   idx=0  [1,2,3]   1:(1,0)  2:(1,0)  3:(1,0)
#   idx=1  [3,2,1]   3:(2,1)  2:(2,1)  1:(2,1)
#   idx=2  [1,4,5]   1:(3,3)  4:(1,2)  5:(1,2)
#   idx=3  [1,2]     1:(4,6)  2:(3,4)
#   final:           1:(4,6)  2:(3,4)  3:(2,1)  4:(1,2)  5:(1,2)
#   read 2:(3,4) as "in 3 sets, whose indices add to 4 (0+1+3)"
#
# Setup: n = 4, all_idx_sum = 0+1+2+3 = 6, gains = [0,0,0,0]
#
# Loop 2 - the votes, only count == n-1 matters:
#   1:(4,6)   count 4     skip
#   2:(3,4)   count 3  -> missing = 6 - 4 = 2  -> gains[2] += 1  -> [0,0,1,0]
#   3:(2,1)   count 2     skip
#   4:(1,2)   count 1     skip
#   5:(1,2)   count 1     skip
#
# Return: max([0,0,1,0]) is 1, and the value 1 sits at position 2 -> gains.index(1) = 2

# n: number of elements across all sets
# k: number of sets
# T: O(n) - the first loop visits every element once; the 2nd visits each unique element once, which is <= n. Dict and list operations like lookup and append are O(1)
# S: O(n + k) - freq_map holds at most n entries, gains holds k

from collections import defaultdict

def largest_set_intersection(sets):
    freq_map = defaultdict(lambda: (0, 0))
    for idx, arr in enumerate(sets):
        for elem in arr:
            count, seen_idx_sum = freq_map[elem]
            freq_map[elem] = (count + 1, seen_idx_sum + idx)
    
    n = len(sets)
    all_idx_sum = sum(range(n))
    gains = [0] * n
    for count, seen_idx_sum in freq_map.values():
        if count == n - 1:
            missing = all_idx_sum - seen_idx_sum
            gains[missing] += 1
    return gains.index(max(gains))


# ---- Reference: the sort-to-group version (backs the § 30 line) ----

# Trigger: the map only GROUPS equal elements for per-group stats (count, seen_idx_sum), never a random lookup
#          -> sort instead: equal elements become adjacent, each group is one run, a running sum replaces the map entry
# Same votes as above; only the bookkeeping changes. Worth it when hashing is off the table

# n: total number of elements across all sets
# k: number of sets
# T: O(n log n) - the sort dominates; the run scan is O(n). Trades a log factor for no hashing
# S: O(n + k) - the flattened pairs, plus gains

def largest_set_intersection_sorted(sets):
    k = len(sets)
    all_idx_sum = sum(range(k))
    pairs = sorted((elem, idx) for idx, arr in enumerate(sets) for elem in arr)

    gains = [0] * k
    i = 0
    while i < len(pairs):
        elem = pairs[i][0]
        count, seen_idx_sum = 0, 0
        while i < len(pairs) and pairs[i][0] == elem:   # one run = one element
            seen_idx_sum += pairs[i][1]
            count += 1
            i += 1
        if count == k - 1:
            gains[all_idx_sum - seen_idx_sum] += 1
    return gains.index(max(gains))


# # Largest Set Intersection

# You are given a non-empty array, `sets`, where each element is an array of unique integers representing a set.
# The _intersection_ of a list of sets is the set of elements that appears in every set.
# Return the index of the set that should be excluded to maximize the size of the intersection of the remaining sets.
# In case of a tie, return the smallest index.

# Example 1: sets = [[1, 2, 3], [3, 2, 1], [1, 4, 5], [1, 2]]
# Output: 2
# Explanation: Excluding the third set (index 2)
# yields a set intersection of size 2: {1, 2}.

# Example 2: sets = [[1, 2], [3, 4], [5, 6]]
# Output: 0
# Explanation: The sets don't have any elements in common,
# so the intersection will be empty regardless of which set you exclude.

# Example 3: sets = [[1, 2, 3], [4, 5]]
# Output: 1
# Explanation: After excluding a set, there will be only one set left,
# so the intersection is the remaining set.

# Example 4: sets = [[1, 2, 3]]
# Output: 0
# Explanation: There is only one set, so after excluding it,
# the intersection is empty.

# Constraints:

# - `1 ≤ sets.length ≤ 10^5`
# - `0 ≤ sets[i].length ≤ 10^5`
# - The total number of elements across all sets is at most `10^5`
# - All integers in each set are unique
# - `-10^9 ≤ sets[i][j] ≤ 10^9`