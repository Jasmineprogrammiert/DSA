# BRUTE FORCE + BOTTLENECK
#
# naive       test every candidate 1..n with n % c == 0 -> O(n)
# lower       Omega(d(n)) - d(n) = the divisor count, just the output size
#             it stays tiny: at most 1344 for n <= 10^9
# upper       O(sqrt n) - min(naive O(n), TLE)
#             n = 10^9 -> O(n) too slow, sqrt n = 3.2x10^4 fits
#             bounds don't meet -> aim at the lower end
#
# trigger     enumerate every divisor of a single number
#
# bottleneck  divisors are sparse, but the naive tests all n candidates
# booster     hunt for properties - DIY on n = 40, write the answer out
#             and read it from both ends inward


# METHOD - PAIR UP TO SQRT
#
# key         c divides n -> n/c divides n too, so divisors come in pairs
# straddle    every pair has one member below sqrt(n) and one above,
#             or the two would multiply past n
# scan        so test c = 1..sqrt(n) and take n//c for free
# square      c*c == n makes the pair one number - add it once
# integer     loop on c*c <= n, not c <= sqrt(n), which rounds wrong
#
# T           O(√n) scan + O(d(n) log d(n)) sort
# S           O(d(n)) - the output itself
# no sort     collect smalls ascending, larges in a second list,
#             return smalls + reversed(larges) -> drops the log factor

def list_of_divisors(n):
    divisors = []
    c = 1
    while c * c <= n:
        if n % c == 0:
            divisors.append(c)
            if c * c != n:
                divisors.append(n // c)
        c += 1
    divisors.sort()
    return divisors


# # List of Divisors

# Given a positive integer `n`, find all its divisors in ascending order.

# A divisor (or factor) of a number `n` is an integer that divides `n` evenly (with no remainder).

# Example 1: n = 40
# Output: [1, 2, 4, 5, 8, 10, 20, 40]

# Example 2: n = 1
# Output: [1]

# Example 3: n = 17
# Output: [1, 17]

# Constraints:

# - `1 <= n <= 10^9`