# state = (h, r)       h = untrained hires, r = recruiters
# HIRE:  h += r
# TRAIN: r += h, h = 0 (needs h > 0)
# 
# h is alwyas a multiple of r
# Use backtracking to check all possibilities and only record 
# the best = min(
#     1 + visit(state after HIRE),
#     1 + visit(state after TRAIN),
# )
# STOPS when r == n returns 0, OR h + r > n returns math.inf
# LOOKUP memo = {}, memo[(h, r)] = best
# CHOOSE min over branches
# STORE the val of (h, r)
# 
# n = 12
# day   action   h   r
# 0     start    0   1
# 1     HIRE     1   1
# 2     TRAIN    0   2
# 3     H        2   2
# 4     T        0   4
# 5     H        4   4
# 6     H        8   4
# 7     T        0   12

# n: target number of recruiters
# T: O(n^2) — states x work per state; (h, r) keys capped by h + r <= n, O(1) each
# S: O(n^2) — one memo entry per state; call stack is O(n) on top

def days_required(n):
    memo = {}
    
    def visit(h, r):
        if r == n:
            return 0
        if r + h > n:
            return float('inf')
        if (h, r) in memo:
            return memo[(h, r)]
        
        days = 1 + visit(h + r, r) # HIRE
        if h > 0:
            days = min(days, 1 + visit(0, h + r)) # TRAIN
            
        memo[(h, r)] = days
        return days

    return visit(0, 1)


# # Hiring And Training

# Your startup company starts with a single recruiter, and your goal is to grow it to exactly `n` recruiters, for some given `n > 1`. Each day, you can do one of two things:

# - HIRE: Hire new employees. You send each recruiter to hire one new employee (you don't send employees that have not been trained as recruiters yet).
# - TRAIN: Train all the new hires to become recruiters themselves (you can't train only a few of them).

# How many days do you need to get to `n` recruiters?

# Constraint: you must not hire more than `n` people.

# Example: n = 3
# Output: 3. On the first two days, you can send your recruiter to hire one new employee. On the third day, you train both of them to become recruiters.

# Example: n = 12
# Output: 7.
# We can follow these actions: Hire, Train, Hire, Train, Hire, Hire, Train

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/hire_and_train0.png

# Constraints:

# - `1 < n <= 10^4`