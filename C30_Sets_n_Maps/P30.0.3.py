# Multiset: a collection of items where duplicated are allowed. Primarily used to count occurences of unique items
# Map<Element, Count>

# Assume a string of length k is added to a multiset n times

# Approach 1: Modified HashSet
#       Remove the duplicate check in add(), so that length k is stored n times. Space used: O(k * n)
# Approach 2: HashMap
#       Store the string once as a key and use an integer value to track the count. Space used: O(k)

# n: the number of elements in the multiset
# k: the number of unique elements
# T: 
#   Average case: O(1). With a uniform hash function and load factor ≈1, operations occur in constant time as bucket depth remains small
#   Amortized: O(1). The O(k) cost of resize() is spread over enough insertinos to maintain constant time per operation
#   String caveat: For string keys of lenght L, complexity scales to O(L) because hashing and equality comparisons must process each character
# S: 
#   Overall: O(k). The table scales linearly with the number of unique elements k
#   Overhead: Includes O(k) for bucket pointers and a growth factor (e.g. doubling) during resizing to ensure the load factor stays within bounds
class HashMap:
    def __init__(self, h):
        self.h = h
        self.capacity = 10
        self._size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def size(self):
        return self._size
    
    def contains(self, k):
        hash = self.h(k, self.capacity)
        for key, _ in self.buckets[hash]:
            if key == k:
                return True
        return False
    
    def get(self, k):
        hash = self.h(k, self.capacity)
        for key, val in self.buckets[hash]:
            if key == k:
                return val
        return None

    def add(self, k, v):
        hash = self.h(k, self.capacity)
        for i, (key, _) in enumerate(self.buckets[hash]):
            if key == k: 
                self.buckets[hash][i] = (k, v)
                return
        self.buckets[hash].append((k, v))
        self._size += 1
        load_factor = self._size / self.capacity
        if load_factor > 1:
            self.resize(self.capacity * 2)

    def resize(self, new_capacity):
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self.buckets:
            for k, v in bucket:
                hash = self.h(k, new_capacity)
                new_buckets[hash].append((k, v))
        self.buckets = new_buckets
        self.capacity = new_capacity
    
    def remove(self, k):
        hash = self.h(k, self.capacity)
        for i, (key, _) in enumerate(self.buckets[hash]):
            if key == k:
                self.buckets[hash].pop(i)
                self._size -= 1
                load_factor = self._size / self.capacity
                if load_factor < 0.25 and self.capacity > 10:
                    self.resize(self.capacity // 2)
                return 

class Multiset:
    def __init__(self, h):
        self.map = HashMap(h)
        self._size = 0
    
    def size(self):
        return self._size
    
    def contains(self, x):
        return self.map.contains(x)
    
    def add(self, x):
        count = self.map.get(x)
        if count is None:
            self.map.add(x, 1)
        else:
            self.map.add(x, count + 1)
        self._size += 1
    
    def remove(self, x):
        count = self.map.get(x)
        if count is None:
            return
        if count == 1:
            self.map.remove(x)
        else:
            self.map.add(x, count - 1)
        self._size -= 1


# Problem 3 - Multiset

# A multiset is a set that allows multiple copies of the same element. Implement a multiset data structure with the following API:
    # add(x): adds a 'copy' of x to the multiset
    # remove(x): removes a 'copy' of x from the multiset
    # contains(x): returns whether x is in the multiset (at least one copy)
    # size(): returns the number of elements in the multiset (including copies)
    
# Constraints:
    # If your language is typed, you can either implement a multiset for integers, or make it generic.
    # The multiset will contain at most 10^6 elements.