# Goal: find minimum 'daily_pages' to finish all chapters within 'days'
#       1 <= daily_pages <= max(page_counts)

# Use transition_point_recipe() to find the transition point, 
# where 'daily_pages' goes from unable to finish all the pages (too small),
# to where it can finish the pages (the first 'r' is the answer)

# is_before() when 
# sum(math.ceil(pages in page_counts / daily_pages)) > days

# n: the number of chapters (len(page_counts))
# M: the maximum number of pages in any chapter (max(page_counts))
# T: O(n * log(M)) - O(log M) iteration of binary search is performed, and in each iteration, n chapters are looped
# S: O(1) - a constant amount of extra space is used regardless of the input size

import math

def min_pages_per_day(page_counts, days):
    def days_to_finish(daily_pages):
        d = 0
        for pages in page_counts:
            d += math.ceil(pages / daily_pages)
        return d
            
    def is_before(daily_pages):
        return days_to_finish(daily_pages) > days

    # l, r = 1, max(page_counts)   
    # The above is WRONG. In the transition point pattern, l and r act as boundaries for two distinct "territories". To guarantee the loop finds the exact boundry, l should ideally start at a value known to be in the 'Before' (false) zone, and r in the 'After' (True) zone
    l, r = 0, max(page_counts) 
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    return r



# # Min Pages Per Day

# You have upcoming interviews and have selected specific chapters from BCtCI to read beforehand. Given an array, `page_counts`, where each element represents a chapter's page count, and the number of days, `days`, until your interview, determine the minimum number of pages you must read daily to finish on time. Assume that:

# - You must read all the pages of a chapter before moving on to another one.
# - If you finish a chapter on a given day, you practice for the rest of the day and don't start the next chapter until the next day.
# - `len(page_counts) <= days`.

# Example 1: page_counts = [20, 15, 17, 10], days = 14
# Output: 5. We can read 5 pages daily and finish all chapters. At a maximum of 5 pages per day, we spend:
# - 4 days on the first chapter.
# - 3 days on the second chapter.
# - 4 days on the third chapter (stopping when we finish early).
# - 2 days on the fourth chapter.
# In total, we spent 13 days reading 5 pages a day, which is the lowest amount we can read daily and still finish on time.

# Example 2: page_counts = [20, 15, 17, 10], days = 5
# Output: 17

# Constraints:

# - `1 <= len(page_counts) <= days <= 10^6`
# - `1 <= page_counts[i] <= 10^4`