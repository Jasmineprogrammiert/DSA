# A better approach: exponential + binary search
# Exponential search: doubling the number of refills until the total volumn exceeds the capacity of the first container

# k: the max number of refills
# T: O(log k) - The exponential search takes O(log k) steps to find an upper bound, then the binary search takes another O(log k) to find the exact answer
# S: O(1) - no additional space is used regardless of input size

def water_refilling(a, b):
    def is_before(times):
        return times * b <= a
    
    # Exponential search (repeated doubling till an upper bound is found)
    k = 1
    while is_before(k * 2):
        k *= 2
    
    # Binary search between k and k*2
    l, r = k, k*2
    while r - l > 1:
        gap = r - l # calculate the total distance between left and r boundries
        half_gap = gap >> 1
        mid = l + half_gap
        # above is the "gap method" which prevents overflow issue
        # mid = (l + r) >> 1
        if is_before(mid):
            l = mid
        else:
            r = mid
            
    return l

# Binary search only
# The Goal: the max pours must fulfill: 
#       times * b <= a
# is_before(times) is True when times * b <= a
#       this func divides the search space into two parts:
#       - Before: all values of times where is_before(times) is True (valid pours)
#       - After: returns False, overflows

# Initialize l = 0, r = a. These are the range of possible times
#       - l represents the min number of pours
#       - r is the max possible pours (a safe overestimate)

# b >= a is not possible given the constraints

# while r - l > 1:
#       mid = (l + r) // 2
#       if is_before(mid):
#           l = mid         can pour at least mid times
#       else:
#           r = mid         pouring mid times overflows
# return l

# a: capacity of the large container
# T: O(log a) - The search space is [0, a]. Each iteration halves the range until r - l <= 1, so the number of iterations is porportional to log2(a)
# S: O(1) - no additional space is used regardless of input size

def water_refilling(a, b):
    def is_before(times):
        return times * b <= a
    
    l, r = 0, a
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
            
    return l
# print(water_refilling(10, 3))



# # Water Refilling

# You have an empty container with a capacity of `a` gallons of water and another container with a capacity of `b` gallons. Return how many times you can pour the second container full of water into the first one without overflowing. Assume that `a > b`.

# **Constraint:** You are not allowed to use the division operation, but you can still divide by powers of two with the right-shift operator, `>>`. Recall that `x >> 1` is the same as `x // 2`.

# Example 1: a = 18, b = 5
# Output: 3. After pouring 5 gallons three times, the first container will be at 15, and 5 more gallons would make it overflow.

# Example 2: a = 10, b = 2
# Output: 5

# Example 3: a = 10, b = 3
# Output: 3

# Constraints:

# - `1 <= b < a <= 10^9`
# - Division operation is not allowed (only right-shift for powers of 2)