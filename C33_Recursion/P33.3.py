# Given a, p, m, return a^p % m without storing huge numbers
# Can use a recursion, base case p == 0, return 1
# Why the formula works:
#   1. a^p = a * a^(p-1)
#   2. Apply % m both sides: a^p % m = (a * a^(p-1)) % m
#   3. Mod property: (a * b) % m = (a * (b % m)) % m
#   4. So: a^p % m = (a * (a^(p-1) % m)) % m
#   5. a^(p-1) % m is the same problem with smaller p, that's the recursive call
# Return (a * recurse(a, p-1, m)) % m
# Edge case: p = 0
# 
# n: p (the exponent)
# T: O(log p) - each call halves p, so log p calls. O(1) work each
# S: O(log p) - call stack depth
def power_mod_m(a, p, m):
    if p == 0: return 1
    half = power_mod_m(a, p // 2, m)
    if p % 2 == 0:
        return (half * half) % m
    else:
        return (a * half * half) % m

# Brute force: O(p) recursive calls, will stack overflow for large p
# n: p (the exponent)
# T: O(p) - p recursive calls, O(1) work each
# S: O(p) - call stack depth
def power_mod_m(a, p, m):
    if p == 0: return 1
    return (a * power_mod_m(a, p-1, m)) % m

# print(power_mod_m(2, 5, 100))



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