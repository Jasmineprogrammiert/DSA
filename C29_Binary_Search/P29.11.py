# page_counts = [20, 15, 17, 10], days = 14

# 0  1  2  3  4  5  6 ... 20      RATE (pages/day)
# x  x  x  x  x  o  o ... o       FITS
#             l
#                r

# binary search on the answer, l, r = 0 (never fits), max(page_counts) (always fits)
# is_before(rate): days_needed(rate) > days

# n: number of chapters
# M: max(page_counts), the size of the answer range
# T: O(n log M) - log M probes, each an O(n) pass over the chapters
# S: O(1) - a few counters, nothing stored

import math

def min_pages_per_day(page_counts, days):
    def days_needed(daily_p):
        total = 0
        for pages in page_counts:
            total += math.ceil(pages / daily_p)
        return total

    def is_before(daily_p):
        return days_needed(daily_p) > days

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