# # Pattern — Sort to Group (hash-free grouping, same total-minus identity)
#
# Trigger:
#     the map is only used to GROUP equal elements and take per-group bulk
#     stats (freq, idx sum) — never random lookups
#     -> sort instead: equal elements become ADJACENT, each group is one run,
#        and a running sum over the run replaces the map entry.
#
# Flatten to (elem, set_idx) pairs -> sort -> scan runs:
#     run length k   -> element in every set, no info for the argmax
#     run length k-1 -> missing from exactly one set:
#         missing_idx = (0 + 1 + ... + k-1) - idx_sum of the run
#     gains is a plain array indexed by set -> left-to-right argmax gives the
#     smallest-index tie-break for free.
#
# n: total number of elements across all sets
# k: number of sets
# T: O(n log n) — the sort dominates; the run scan is O(n). The map version
#    below is O(n) average — this trades a log factor for no hashing and
#    simpler bookkeeping.
# S: O(n + k) — the flattened pairs and the gains array

def largest_set_intersection_sorted(sets):
    k = len(sets)
    pairs = sorted((elem, i) for i, s in enumerate(sets) for elem in s)
    total_idx_sum = k * (k - 1) // 2

    gains = [0] * k
    pair_idx = 0
    while pair_idx < len(pairs):
        elem = pairs[pair_idx][0]
        freq, idx_sum = 0, 0
        while pair_idx < len(pairs) and pairs[pair_idx][0] == elem:
            idx_sum += pairs[pair_idx][1]
            freq += 1
            pair_idx += 1
        if freq == k - 1:
            # run misses exactly one set -> total minus finds it
            gains[total_idx_sum - idx_sum] += 1

    best = 0
    for i in range(k):
        if gains[i] > gains[best]:
            best = i
    return best


# freq_map: {element: (freq, idx_sum)}
# gains = {}
# n = len(sets)
# total_idx_sum = sum(range(n))
#
# 1. Loop through each element in the set to build the freq_map, idx_sum is the sum of the index of the set the element is in
# 2. For each element where freq == n-1:
#   n-1: element missing from exactly one set, removing that set adds it to the intersection
#   missing_idx = total_idx_sum - idx_sum
#   gains[missing_idx] += 1 => removing this set gain x elements
#
# Return idx with max gains (smallest idx on tie, 0 if none)
#
# n: total number of elements across all sets
# k: number of sets
# T: O(n) - iterate over every element once to build freq_map, then scan unique entries (<= n)
# S: O(n + k) - freq_map has at most n entries, gains has at most k entries

def largest_set_intersection(sets):
    freq_map = {}
    gains = {}
    n = len(sets)
    total_idx_sum = sum(range(n))

    for i, s in enumerate(sets):
        for elem in s:
            if elem not in freq_map:
                freq_map[elem] = (1, i)
            else:
                freq, idx_sum = freq_map[elem]
                freq_map[elem] = freq + 1, idx_sum + i

    for freq, idx_sum in freq_map.values():
        if freq == n - 1:
            missing_idx = total_idx_sum - idx_sum
            gains[missing_idx] = gains.get(missing_idx, 0) + 1

    if not gains:
        return 0

    max_gain = max(gains.values())
    return min(idx for idx, g in gains.items() if g == max_gain)


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