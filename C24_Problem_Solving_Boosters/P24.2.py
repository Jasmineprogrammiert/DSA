# BRUTE FORCE + BOTTLENECK
#
# assumes     substrings counted by position, not distinct values
#             "abababa" -> 3 valid, all "b" - ask to confirm
#
# naive       enumerate all O(n^2) substrings, scan each for 'a' -> O(n^3)
# cheaper     track 'a' while extending the end -> O(n^2), still too slow
# lower       Omega(n) - output is one number, but a single 'a' anywhere
#             changes it, so every char must be read
# upper       O(n log n) - min(naive O(n^2), TLE)
#             n = 10^5 -> n^2 = 10^10 too slow, n log n = 1.7x10^6 fits
#             narrow gap -> aim at O(n)
#
# trigger     a forbidden element partitions the string
#
# bottleneck  most substrings contain an 'a' and are discarded on sight
#             "abababa" has 28 substrings, only 3 are valid
# booster     skip unnecessary work: never build the invalid ones


# METHOD - SPLIT + FORMULA
#
# key         a substring spanning an 'a' must contain that 'a',
#             so every valid one lies entirely inside one a-free section
# split       s.split('a') hands back those sections, empties included
# formula     a section of length k has k*(k+1)//2 non-empty substrings
#
# T           O(n) split + O(n) sections x O(1) per section = O(n)
# S           O(n) - split materialises the sections
# O(1) space  walk s once with a run counter instead


def count_substrings(s):
    sections = s.split('a')
    total = 0
    for section in sections:
        k = len(section)
        total += k * (k + 1) // 2
    return total


# # Count Substrings Without Letter

# Given a string, `s`, count the number of non-empty substrings of `s` that do not contain the letter 'a'.

# Example: "bcadefa"
# Output: 9. The 9 substrings without 'a' are: "b", "c", "bc", "d", "e", "f", "de", "ef", and "def".

# Constraints:

# - `0 <= s.length <= 10^5`
# - `s` consists of lowercase English letters only