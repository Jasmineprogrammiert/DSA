# Problem 33.3 - Powers Mod M
# Given three integers a > 1, p >= 0, and m > 1, compute a^p % m while avoiding
# storing intermediate values much larger than m.
#
# Recurrence:
# a^0 % m = 1
# For p > 0, a^p % m = (a * (a^(p-1) % m)) % m
#
# Example 1: a = 2, p = 5, m = 100 -> 32
# Example 2: a = 2, p = 5, m = 30 -> 2
# Example 3: a = 123456789, p = 987654321, m = 1000000007 -> 652541198
# Example 4: a = 3, p = 1, m = 5 -> 3
# Example 5: a = 5, p = 3, m = 7 -> 6
#
# Constraints:
# - 1 < a <= 10^9
# - 0 <= p <= 10^9
# - 1 < m <= 10^9