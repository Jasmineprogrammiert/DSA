# multiple IP addresses
# multiple domains can share the same IP address
# Each domain can have multiple subdomains

# ip_dom = {ip: {domain}}
# dom_subdom = {domain: {subdomain}}

# n: number of IPs
# m: number of domains
# k: number of subdomains
# T: O(1) - average per operation,  every step is a dict or set lookup/ insert
# S: O(n + m + k) - ip_dom O(n + m) + dom_subdom O(m + k)

from collections import defaultdict

class DomainResolver:
    def __init__(self):
        self.ip_dom = defaultdict(set)
        self.dom_subdom = defaultdict(set)
    
    def register_domain(self, ip, dom):
        self.ip_dom[ip].add(dom)
    
    def register_subdomain(self, dom, subdom):
        self.dom_subdom[dom].add(subdom)
    
    def has_subdomain(self, ip, dom, subdom):
        if dom in self.ip_dom.get(ip, set()) and subdom in self.dom_subdom.get(dom, set()):
            return True
        return False


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