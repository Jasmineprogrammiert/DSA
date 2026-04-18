# Sort each IP list, then convert the sorted list to tuple (lists are mutable, so they can't be set keys) to use it as a set key
# If the tuple already exists in the set, return True (duplicate found)
# Otherwise, add it and continue; return False if no duplicates found after all users are checked
# n: the number of users
# k: the number of IPs per user, topped at 10
# T: O(n) - for each user, sort their IP list O(k log k) and check the record in the set, so O(n * k log k). Since k <= 10, simplifies to O(n)
# S: O(n) - in the worst case, the set stores n*k IPs, O(n * k) is simplified to O(n)

def multi_account_cheating(users):
    checking = set()
    for _, IPs in users:
        immutable_list = tuple(sorted(IPs))
        
        if immutable_list in checking:
            return True
        checking.add(immutable_list)
    return False

    

# # Multi-Account Cheating

# Our company runs an online game where the terms of service state that each person can only have one account. We have a list of usernames and the (unordered) list of IP addresses that they have ever connected from. We say two users are suspected of belonging to the same person if the list of IPs is the same. Return whether any two lists contain the exact same set of IPs.

# Example 1: users = [
#   ("mike", ["203.0.3.10", "208.51.0.5", "52.0.2.5"]),
#   ("bob", ["111.0.0.10", "222.0.0.5", "222.0.0.8"]),
#   ("bob2", ["222.0.0.5", "222.0.0.8", "111.0.0.10"])
# ]
# Output: True. Users "bob" and "bob2" have the same IPs.

# Example 2: users = [
#   ("alice", ["1.1.1.1"]),
#   ("bob", ["2.2.2.2"])
# ]
# Output: False. No two users have the same IPs.

# Example 3: users = []
# Output: False. There are no users.

# Constraints:

# - The length of users is at most `10^5`
# - Each username is non-empty and unique
# - Each list of IPs has between `1` and `10` IPs
# - All IPs are unique and follow the IPv4 format
# - Each octet is a number between `0` and `255`