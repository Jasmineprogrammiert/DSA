# min-heap of (current value, base prime)
#   seed the heap with every prime
#   pop the root (smallest), add it to the running sum
#   push root * its_prime back -> the next power of that prime
#   repeat until k numbers are popped
#
# n: length of primes
# k: how many smallest prime-powers to sum
# T: O((n + k) * log n) - heapify seed O(n) + k pop/push rounds, each heap op O(log n)
# S: O(n) - heap holds exactly one entry per prime

# NB: val = p^i grows unboundedly, so val*prime is not O(1), and it would overflow in Java/C++. To fix it, order the heap by exp*log(p) and carry val % m separately

import heapq


def sum_of_first_k(primes, k):
    res = 0
    heap = [(p, p) for p in primes]
    heapq.heapify(heap)
    
    for _ in range(k):
        val, prime = heapq.heappop(heap)
        heapq.heappush(heap, (val * prime, prime))
        res += val
    return res if res <= 10**9+7 else res % (10**9+7)


# # Sum Of First K Prime Powers

# Given a non-empty array, `primes`, of **distinct prime** numbers, and a positive number `k`, return the sum of the first `k` numbers that are a positive power of a number in `primes`.

# If the answer is larger than `10^9+7`, return it modulo `10^9+7`.

# Example 1: primes = [2], k = 1
# Output: 2
# The first positive power of 2 is 2^1 = 2.

# Example 2: primes = [5], k = 3
# Output: 155
# The first 3 positive powers of 5 are 5, 25, and 125.

# Example 3: primes = [2, 3], k = 7
# Output: 69
# The first 7 numbers that are a positive power of 2 or 3 are 2, 3, 4, 8, 9, 16, and 27.

# Constraints:

# - `1 <= primes.length <= 10^4`
# - Each element in `primes` is a distinct prime number
# - `0 <= k <= 10^6`