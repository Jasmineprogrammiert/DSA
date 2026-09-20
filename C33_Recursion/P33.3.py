# compute `a^p % m`
# avoiding storing intermediate values much larger than `m`
# a = 2, p = 5, m = 100 --> 32

# 2^5 -> 2 · (2^2)²
# 2^2 --> (2^1)²
# 2^1 --> 2

# n: p, the exponent
# T: O(log p) - p halves every call, O(1) work each
# S: O(log p) - the call stack, one frame per halving

def powers_mod_m(a, p, m):
    if p == 0:
        return 1
    half = powers_mod_m(a, p // 2, m)
    res = half * half % m
    if p % 2 == 1:
        res = a * res % m
    return res


# # Powers Mod M

# Given three integers `a > 1`, `p ≥ 0`, and `m > 1`, compute `a^p % m` while avoiding storing intermediate values much larger than `m`.

# The basic recurrence relation for powers is:
# - `a^0 = 1`
# - For `p > 0`, `a^p = a * a^(p-1)`

# When it comes to the modulo operation, we can apply it at each step without affecting the result:
# - `a^0 % m = 1`
# - For `p > 0`, `a^p % m = (a * (a^(p-1) % m)) % m`

# Example 1: a = 2, p = 5, m = 100
# Output: 32

# Example 2: a = 2, p = 5, m = 30
# Output: 2

# Example 3: a = 123456789, p = 987654321, m = 1000000007
# Output: 652541198

# Example 4: a = 3, p = 1, m = 5
# Output: 3

# Example 5: a = 5, p = 3, m = 7
# Output: 6

# Constraints:

# - `1 < a ≤ 10^9`
# - `0 ≤ p ≤ 10^9`
# - `1 < m ≤ 10^9`