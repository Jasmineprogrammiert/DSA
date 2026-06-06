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