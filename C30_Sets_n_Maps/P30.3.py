# Use a dict to store the octet in each ip, then count its re-occurences. Return the octet with the most count
# n: length of ips
# T: O(n) - at most the dict is passed n times
# S: O(n) - the length of dict is at most n // WRONG
#    O(1) - the first octet is always a number between 0 and 255, so seen dict can have at most 256 entries, no matter how large ip is

def most_frequent_octet(ips):
    seen = {}
    
    for ip in ips:
        octet = ip.split(".")[0]
        if not octet in seen:
            seen[octet] = 0
        seen[octet] += 1
    
    most_seen = None
    most_count = 0
    for octet, count in seen.items():
        if most_count < count:
            most_seen = octet
            most_count = count
    return most_seen



# # Most Frequent Octet

# You've compiled a list of IP addresses of all the clients connected to your service. Assume all IPs are unique and follow the IPv4 format, which consists of four 8-bit numbers (called octets) separated by dots. Return the most common first octet among the connections.

# Example 1: ips = ["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"]
# Output: "203". 203 appears twice as the first octet.

# Example 2: ips = ["10.0.0.1", "10.0.0.2", "192.168.1.1"]
# Output: "10". 10 appears twice as the first octet, while 192 appears once.

# Example 3: ips = []
# Output: None. There are no IP addresses.

# Constraints:

# - The length of `ips` is at most 10^5
# - All IPs are unique and follow the IPv4 format
# - Each octet is a number between `0` and `255`