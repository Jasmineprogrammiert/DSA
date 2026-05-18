# Problem 37.8 - Sum of First K Prime Powers
# Given an array of distinct primes and a positive number k, return the sum
# of the first k numbers that are a positive power of a number in primes.
# If answer > 10^9+7, return it modulo 10^9+7.
#
# Example 1: primes = [2], k = 1 -> 2
# Example 2: primes = [5], k = 3 -> 155 (5 + 25 + 125)
# Example 3: primes = [2,3], k = 7 -> 69 (2,3,4,8,9,16,27)
#
# Constraints:
# - 1 <= primes.length <= 10^4
# - Each element is a distinct prime
# - 0 <= k <= 10^6