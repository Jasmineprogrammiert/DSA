# n: the number of key-value pairs in the map
# T: 
#   Average case: O(1). With a uniform hash function and load factor ≈1, operations occur in constant time as bucket depth remains small
#   Amortized: O(1). The O(k) cost of resize() is spread over enough insertinos to maintain constant time per operation
#   String caveat: For string keys of lenght L, complexity scales to O(L) because hashing and equality comparisons must process each character
# S: Overall: O(n). The table scales linearly with the number of n key-value pairs, plus some overhead for dynamic resizing

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


# Problem 4 - Hash Map Class

# Implement a hash map data structure with the following API:
    # add(k, v): if k is not in the map, add key k to the map with value v. If k is already in the map, update its value to v.
    # remove(k): if k is in the map, remove it from the map
    # contains(k): return whether the key k is in the map
    # get(k): return the value for key k. If k is not in the map, return a null value
    # size(): return the number of keys in the map
    
# Hint: if you've already solved the HashSet Class problem, you can start with that and modify it to store key–value pairs.

# Constraints:
    # If your language is typed, you can either implement a hash map for integers, or make it generic.
    # The map will contain at most 10^6 key-value pairs.