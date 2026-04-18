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

# print(largest_set_intersection([
#     [1, 2, 3], [3, 2, 1], [1, 4, 5], [1, 2]
# ]))



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