# An IP can be shared by multiple domains, a subdomain can be registered with different domains
# Can put IP and domain as key-value pairs. The key is IP, the value is a set of domains
# {
#     "192.168.1.1": {"example.com", "example.org"},
#     "192.168.1.2": {"domain.com"}
# }
# Can put domain and subdomain as key-value pairs. The key is domain, the value is a set of subdomains
# {
#     "example.com": {"www", "a"},
#     "example.org": {"bbb", "b", "c"},
# }

# n: the number of IPs
# m: the number of domains
# k: the number of subdomains
# T: O(1) - all dictionary lookups and set operations (add, lookup) are O(1) on average
# S: O(n + m + k)
#       ip_to_domain: at most n keys, with m total domains across all sets -> O(n + m)
#       domain_to_subdomain: at most m keys, with k total subdomains across all sets -> So O(m + k)
#       Combined: O(n + 2m + k) -> O(n + m + k)

class domain_resolver:
    def __init__(self):
        self.ip_to_domain = dict()
        self.domain_to_subdomain = dict()
    
    def register_domain(self, ip, domain):
        if ip not in self.ip_to_domain:
            self.ip_to_domain[ip] = set()
        self.ip_to_domain[ip].add(domain)

    def register_subdomain(self, domain, subdomain):
        if domain not in self.domain_to_subdomain:
            self.domain_to_subdomain[domain] = set()
        self.domain_to_subdomain[domain].add(subdomain)
    
    def has_subdomain(self, ip, domain, subdomain):
        if ip not in self.ip_to_domain:
            return False
        if domain not in self.ip_to_domain[ip]:
            return False
        if domain not in self.domain_to_subdomain:
            return False
        return subdomain in self.domain_to_subdomain[domain]



# # Domain Resolver

# You manage a shared web hosting server with multiple IP addresses, and where multiple domains can share the same IP address. Each domain can have multiple subdomains.

# Implement a class, `DomainResolver`, that supports three methods:

# - `register_domain(ip, domain)`: associates a domain with an IP. You can assume that this function will be called at most once for a given domain.
# - `register_subdomain(domain, subdomain)`: adds a subdomain to a domain. You can assume that the domain will have been previously registered. Different domains can have a subdomain with the same name.
# - `has_subdomain(ip, domain, subdomain)`: returns whether there is a domain registered at that IP that has the given subdomain.

# `IPs`, `domains`, and `subdomains` are strings.

# Example 1:
# resolver = DomainResolver()
# resolver.register_domain("192.168.1.1", "example.com")
# resolver.register_domain("192.168.1.1", "example.org")
# resolver.register_domain("192.168.1.2", "domain.com")
# resolver.register_subdomain("example.com", "a")
# resolver.register_subdomain("example.com", "b")
# resolver.has_subdomain("192.168.1.1", "example.com", "a")  # Returns True
# resolver.has_subdomain("192.168.1.1", "example.com", "c")  # Returns False
# resolver.has_subdomain("127.0.0.1", "example.com", "a")    # Returns False
# resolver.has_subdomain("192.168.1.1", "example.org", "a")  # Returns False
# resolver.has_subdomain("192.168.1.2", "example.com", "a")  # Returns False

# Example 2:
# resolver = DomainResolver()
# resolver.register_domain("1.1.1.1", "test.com")
# resolver.register_subdomain("test.com", "www")
# resolver.has_subdomain("1.1.1.1", "test.com", "www")  # Returns True

# Example 3:
# resolver = DomainResolver()
# resolver.has_subdomain("1.1.1.1", "test.com", "www")  # Returns False

# Constraints:

# - The number of calls to `register_domain` and `register_subdomain` will be at most `10^5`
# - The number of calls to `has_subdomain` will be at most `10^5`
# - All `IPs` follow the IPv4 format
# - Each octet is a number between `0` and `255`
# - All domains and subdomains are non-empty strings of length at most `100`