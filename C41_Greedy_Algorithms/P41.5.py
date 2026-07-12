# Greedy: to capture every meeting with the fewest runs, place each run
# at the earliest end time -> the smallest right endpoint still uncovered.
#   -> sort by right endpoint r
#   -> scan left to right, spend a new run when a meeting starts
#      after the last run's time (l > last_run)
#   -> placing the run at the earliest end never misses a meeting a
#      later point would have caught -> safe exchange argument
#
# n: number of meetings
# T: O(n log n) — sort dominates, single linear pass after
# S: O(n) — Python's sort needs extra space; only scalars beyond that

def fewest_script_runs(meetings):
    meetings.sort(key=lambda x: x[1])
    runs = 0
    last_run = float("-inf")
    for l, r in meetings:
        if l > last_run:
            runs += 1
            last_run = r
    return runs


# # Fewest Script Runs

# There are `n` meetings scheduled, each with a start time and an end time. We have a script that, when run, captures some information about all ongoing meetings. Given an array, `meetings`, where each element is a tuple `[l, r]` with `l < r`, what's the minimum number of times we need to run the script to capture information from all meetings?

# If the script runs at the same time that a meeting starts or ends, it captures the information for that meeting.

# Example 1:
# meetings = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 10]]

# Output: 2
# We can run the script at t = 3 and t = 9.

# Constraints:

# - `0 <= n <= 10^5`
# - `0 <= meetings[i][0] < meetings[i][1] <= 10^9`