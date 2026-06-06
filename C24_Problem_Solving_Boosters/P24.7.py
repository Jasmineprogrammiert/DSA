# # Interval XOR

# Given two intervals, `a = [a_s, a_e]` and `b = [b_s, b_e]` with `a_s < a_e` and `b_s < b_e`, return a list of intervals representing `a xor b`, defined as the sections of `a` that are not in `b` and the sections of `b` that are not in `a`. The output intervals should be sorted from left to right, non-overlapping, and not sharing an endpoint.

# Only the left endpoint of an interval is considered part of it: `[s, e]` represents the set of values `x` such that `s ≤ x < e`.

# Example: a = [5, 15], b = [10, 30]
# Output: [[5, 10], [15, 30]]. a and b overlap in the interval [10, 15]. It would not be correct to return [[15, 30], [5, 10]] because the intervals are not ordered from left to right.

# Example: a = [15, 30], b = [5, 15]
# Output: [[5, 30]]. It would not be correct to return [[5, 15], [15, 30]] because the two intervals share an endpoint and can be consolidated.

# Example: a = [5, 15], b = [5, 15]
# Output: [].

# Constraints:

# - The endpoints of the intervals are integers
# - `-10^9 <= a_s < a_e <= 10^9`
# - `-10^9 <= b_s < b_e <= 10^9`